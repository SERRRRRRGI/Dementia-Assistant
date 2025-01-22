from datetime import datetime
from function_calling.function_parent_class import OpenAIFunction

description = {
    "name": "get_tdr_conclusions",
    "description": "Returns the TDR conclusions with a brief explanation.",
}


class GetTDRConclusions(OpenAIFunction):

    @staticmethod
    def getName():
        return description["name"]
    
    def __init__(self):
        self.description = description
        self.meanwhile = ["Mmm...", "Deixam pensar..."]

    def apply(self, _):
        
        return """
Per explicar la conclusió reflexionarem sobre si s'han comprovat les hipòtesis o no.
    3. És possible crear un assistent de veu que parli en català?
    Aquesta hipòtesi és certa perquè jo (la Clara) soc un assistent de veu intel·ligent i parlo en català.
    2. És possible crear una assistent de veu intel·ligent propi a partir de les tecnologies de l'actualitat?
    Aquesta hipòtesi també és certa perquè jo (la Clara) soc una intel·ligència artificial creada per l'Eloi, l'autor d'aquest TDR, i per crear-me ha utilitzat les tecnologies que tenim disponibles en l'actualitat.
    1. És possible millorar l'autonomia de les persones de la tercera edat utilitzant la intel·ligència artificial?
    Aquesta hipòtesi no l'hem pogut acaba de comprovar. Al principi vam fer un llistat amb les funcionalitats que hauria de tindre jo (la Clara) per poder ajudar a una persona amb demència a ser més autonoma, però la realitat és que, per desgràcia, encara no he pogut parlar amb cap pacient de demència. Així doncs, teòricament sí que és possible, però com que no s'ha comprovat de manera empírica no la podem afirmar.
"""