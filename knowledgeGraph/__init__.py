import spacy
model = "en_core_web_sm"
nlp = spacy.load(model)
from knowledgeGraph.information import InformationExtraction
infor_Extract = InformationExtraction()
get_entity = infor_Extract.get_entities
get_relation = infor_Extract.get_relations
