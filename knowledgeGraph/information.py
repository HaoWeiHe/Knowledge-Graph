import knowledgeGraph

class InformationExtraction():
	def __init__(self):
		self.nlp = knowledgeGraph.nlp

	def get_entities(self,sent):
		ent1, ent2 = [],[]
		cpmds, mods = [],[] #for compound and modifier
		for token in self.nlp(sent):
			if token.dep_ == "punct": #if current token is a punctuation mark, move to the next token
				continue 
			if token.dep_ == "compound":
				cpmds.append(token.text)
			if token.dep_[-3:]== "mod":
				mods.append(token.text)
			if "subj" in token.dep_:
				ent1 = cpmds + mods + [token.text]
				cpmds, mods = [],[] 
			if "obj" in token.dep_:
				ent2 = cpmds + mods + [token.text]
				cpmds, mods = [],[] 
		return " ".join(ent1), " ".join(ent2)


	def get_relations(self, sent):
		import spacy
		from spacy.matcher import Matcher
		res = []
		matcher = Matcher(self.nlp.vocab)
		pattern = [{'DEP':'ROOT'}]
		
		matcher.add("Rule_1", None, pattern) 
		doc = self.nlp(sent)
		matches = matcher(doc)
		for match_id, start, end in matches:
			string_id = self.nlp.vocab.strings[match_id]	
			for idx in range(start, end):
				res.append(doc[idx].lemma_)
		
		return res[0]

if __name__ == '__main__':
	IE = InformationExtraction()
	# nlp = spacy.load("en_core_web_sm")
	# kg = KG(nlp)
	# text = "the milky way has spiral arms"
	# print(kg.get_entities(text))
	# print(kg.get_relations(text))
