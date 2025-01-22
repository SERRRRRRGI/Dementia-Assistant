from pydantic import BaseModel
from typing import Optional
import re
import uuid

from  program_settings import verbose
from openai_client import OPENAI_CLIENT


class OutputFormat(BaseModel):
    corrected_text: str
    confidential: Optional[dict[str, str]]

class Handler:
    def __init__(self, assistant):
        self.assistant = assistant
        self.client = OPENAI_CLIENT
        
        self.OutputFormat = OutputFormat

    def _convert_confidential_keys(self, cured_text_obj: OutputFormat, speaker): 
        text = cured_text_obj.corrected_text
        confidential = cured_text_obj.confidential

        if verbose: print("text: ", type(text), "confidential: ", type(confidential))
        if not confidential: return cured_text_obj

        new_confidential= {}

        def replace_placeholder(text: str, replacement_func):
            # This regex pattern matches substrings in the format <<something>>
            pattern = r'<<(.+?)>>'
            
            # Function to replace the matched pattern with the result from replacement_func
            def replacer(match):
                # Extract the 'something' part (inside the << >>)
                something = match.group(1)
                # Pass 'something' to the replacement function and return the result
                return replacement_func(something)

            # Use re.sub to find and replace all <<something>> with the result of replacement_func
            return re.sub(pattern, replacer, text)
        
        def replace_fn(key):
            new_key = "<<" + speaker.strip().upper().replace(" ", "_") + "_" + key.upper().strip().replace(" ", "_") + "_" + str(uuid.uuid4().int)[:4] + ">>"

            new_confidential[new_key] = confidential[key]
            return new_key
        
        new_text = replace_placeholder(text, replace_fn)

        return OutputFormat(
            corrected_text = new_text,
            confidential = new_confidential
        )
    
    def _eliminate_confidentiality(self, text, speaker, temperature=.6):
        system_prompt= """A continuació es mostraran uns missatges procedents de la veu enregistrada de l'usuari. En aquests missatges és possible que aparegui contingut confidencial (números de compte bancari, números de targeta, número de DNI, etc.).
Els passos per acomplir aquesta tasca són:
    - Identificar el contingut confidencial
    - Assegurar-se que realment és confidencial
    - Substituir el contingut confidencial per un nom que el representi, posat entre <<nom clau>>.
    - Assegurar-se que el nom sigui ben descriptiu: NUMERO_TARGETA_BANCARIA, PIN_TARGETA_DE_CREDIT.
    - Afegir el nom clau com a clau al diccionari de sortida ("confidential") i al valor que oculta com el seu valor.
 
En el cas que no hi hagi contingut confidencial, s'ha de deixar la clau "confidential" buida.
Els missatges rebuts per dur a terme aquesta feina van dirigits a una tercera persona, així que no han de ser resposts, només s'ha d'analitzar la seva confidencialitat."""
        result = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": text
                }
            ],

            response_format=self.OutputFormat
        )

        parsed: OutputFormat = result.choices[0].message.parsed

        new_parsed = self._convert_confidential_keys(parsed, speaker=speaker)
        if verbose: print("parsed confidential and curated_text obj: ", new_parsed)
        return new_parsed
    
    def handle(self, metadated_text, speaker): 
        text = metadated_text["text"]     
        if (not len(text)): return

        cured_text_obj = self._eliminate_confidentiality(text=text, speaker=speaker)
    
        new_metadated_text = {
            "text": cured_text_obj.corrected_text,
            "tokens": metadated_text["tokens"]
        }
        self.assistant.handle(new_metadated_text, confidential=cured_text_obj.confidential, speaker=speaker)