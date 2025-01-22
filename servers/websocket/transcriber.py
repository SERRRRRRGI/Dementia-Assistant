from openai_client import OPENAI_CLIENT
from essential_data import ASSISTANT_NAME, USER_NAME, IMPORTANT_WORDS

from  program_settings import verbose

class Transcriber:

    def __init__(self, model="whisper-1", response_format="json"):
        self.client = OPENAI_CLIENT
        self.model = model
        self.response_format = response_format

        self.transcribed_text_buffer = []

        self.system_prompt = f"""A continuació es mostraran uns missatges enviats per l'usuari procedents de la transcripció de la seva veu feta automàticament. Aquests textos probablement presenten errors d'ortografia i ambigüitat, així que han de ser corregits en aquests aspectes.
S'han de seguir les següents instruccions rigorosament per fer aquesta feina:
    - Els següents mots han d'estar escrits correctament (tal com es mostra a continuació): {", ".join([ASSISTANT_NAME, USER_NAME, *IMPORTANT_WORDS])}.
    - Només es poden afegir els signes de puntuació necessaris (punts, comes, majúscules).
    - Només es pot utilitzar el context que dona en el missatge de l'usuari per dur a terme la tasca.
    - No es poden eliminar les interjeccions que utilitza l'usuari, ja que aporten valor semàntic al missatge.
    - No es poden de traduir paraules d'idioma si es tracta d'una seqüència sencera o d'un modernisme concret.
    - Si el missatge està buit, no s'ha de respondre res.
    - Els missatges de l'usuari van dirigits a una tercera persona, així que no han de ser resposts, sinó només corregits.

Aquest símbol ("|") es troba on l'àudio s'ha tallat per ser transcrit. L'inici i el final d'aquestes cadenes és el mateix, així que s'han de realitzar retocs per ajuntar ambdues seqüències."""

    def _correct_transcript(self, system_prompt, transcript, temperature=.5):
        if verbose: print(transcript)
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": transcript
                }
            ],
        )

        return {
            "text": response.choices[0].message.content,
            "tokens": response.usage.completion_tokens
        }
    

    def transcribe(self, audio_data, language=None, prompt="", continuation=False):
        
        transcription = self.client.audio.transcriptions.create(
            model=self.model,
            file=audio_data,
            response_format=self.response_format,
            language=language,
            prompt=prompt
        )

        if not continuation:
            if len(self.transcribed_text_buffer) == 0:
                correct_transcription = self._correct_transcript(transcript=transcription.text, system_prompt=self.system_prompt)
            
            else:
                self.transcribed_text_buffer.append(transcription.text)
                
                correct_transcription = self._correct_transcript(transcript=" | ".join(self.transcribed_text_buffer), system_prompt=self.system_prompt)
                self.transcribed_text_buffer = []

            return correct_transcription
        
        else:
            self.transcribed_text_buffer.append(transcription.text)
            
            return transcription.text
    
class transcriber_utils:
    personal_pronouns = {
        "masc": "el",
        "fem": "la",
        "neutre": "li"
    }

    @staticmethod
    def starts_in_vowel(string: str):
        return string[0].lower() in ["a", "à", "e", "è", "é", "i", "í", "o", "ò", "ó", "u", "ú"]
    
    @staticmethod
    def get_name_with_article(user_name: str = "", user_gender = "masc"):
        user_name = user_name.strip()
        if len(user_name) == 0: raise ValueError("user_name parameter required to generate the transcriber prompt")

        return f"""{"l'" if transcriber_utils.starts_in_vowel(user_name) else transcriber_utils.personal_pronouns[user_gender] + " "}{user_name}"""

    @staticmethod
    def generate_prompt(user_name: str = "", user_gender = "masc", assistant_name: str = "ChatGPT"):
        user_name = user_name.strip()
        if len(user_name) == 0: raise ValueError("user_name parameter required to generate the transcriber prompt")

        assistant_name = assistant_name.strip()
        return f"""Mmm... {assistant_name} estic pensant queeeeeee..., pffffff..., estava dient que, eeeeh, doncs que el que {"l'" if transcriber_utils.starts_in_vowel(user_name) else transcriber_utils.personal_pronouns[user_gender] + " "}{user_name} està és això."""