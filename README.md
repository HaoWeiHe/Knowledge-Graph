# Knowledge-Graph


A knowledge graph is a structured graph from multiple sources standardized to acquire and integrate human knowledge. Knowledge graphs are often used to store interlinked descriptions of entities – objects, events, situations or abstract concepts – with free-form semantics(from wiki). Here we demo one way of implementation using triples as our data format. (There are many various ways to implement KG, and this project demonstrates the automatic way based on the result of information extraction).


## Background Knowledge
Let's took the most common knowledge graph - Wikidata for example. One way to implement KG is using a concept of triple, which is a statement in "subject/predicate/object" form. A statement linked one entity(subject) to another (object) via a predicate. For example, the milky way has spiral arms. Therefore, the triple is going to be like this :
<br>
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/triple.png)
<br>
In this project, we extract relations from the nlp pipeline and use the example, the milky way has spiral arms, as our demonstration input . If you aren't familiar with this. Maybe the post -[ A brief introduction: semantics & syntax ](https://haoweihohoho.medium.com/brief-introduce-semantics-syntax-9b84174de947)  can provide you a little bit of insight.

<br><br><br><br>

## NLP Pipeline 
In this article, we will use the nlp pipeline to extract relations within an utterance. And we are gonna use spacy as our main tool.
<br>
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/spacyPipline.svg)
NLP Pipeline - Credict by Spacy
<br>
<br>
<br>
Using a text as input and doc as output, we process it into several steps by leveraging different well-trained models. That model is also known as the **NLP processing Pipeline**. A typical NLP pipeline including a segmentation (tokenizer), a Part-of-speech tagging (tager), a parser and any entity recognizer. This process can be easy accessed by calling the Spacy library.
<br>
<br>
```
import spacy
text = "the milky way has spiral arms"
nlp = spacy.load("en_core_web_sm")
displacy.render(nlp(text), jupyter=True, style = 'dep')
 ```

- dependency of the example sentence - *the milky way has spiral arms*
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/DepMilkyWay.png)

To see all of the dependency/ POS tagging relationship of the sentence - *the milky way has spiral arms*, we could have the following code to help us determine which part we would like to extract.
```
                for token in doc:
                    print(token.text, token.pos_, token.dep_)
                   
                 
                # the DET det
                # milky ADJ amod
                # way NOUN nsubj
                # has VERB ROOT
                # spiral ADJ amod
                # arms NOUN dobj
```
Having this information, we could easily extract a triplet. See all the [dependency labels](https://github.com/clir/clearnlp-guidelines/blob/master/md/specifications/dependency_labels.md.)(for English only).

## Information extraction / Entity extraction
To build up a knowledge graph, it's important to extract nodes and the relation between them. There are several **unsupervised manners** to do the information extraction. On syntactic level, we could leverage part-of-Speech (POS) tags to help us extract this information, or, on semantic level, we can use Semantic Role Labeling (SRL) technique to help us extract entities.
<br><br>
In this article, we will focus on syntactic level with POS technique which is one of efficient ways to do it.
<br><br>
However, when an entity could not only just a single word but a chunk - which means multiple words should be put together. In this case, we could leverage a dependency tree to help us to extract chunks as our entities.
<br><br>
Let's see how to extract chunks through a sentence. Noun related tags will be the entities (Subject/ Object) and the dependency between them will be the relation (Predicate).
### Extract Eneities
```
	def get_entities(self, sent):
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
                
                stn_text = "the milky way has spiral arms"
                print(get_entities(stn_text))
                # >> ['milky way', 'spiral arms']
```

### Extract Relations 
```
                import spacy
                from spacy.matcher import Matcher

                def get_relations(sent):
                  res = []
                  matcher = Matcher(nlp.vocab)
                  pattern = [{'DEP':'ROOT'}]
                  
                  matcher.add("Rule_1", None, pattern) 
                  doc = nlp(sent)
                  matches = matcher(doc)
                  for match_id, start, end in matches:
                    string_id = nlp.vocab.strings[match_id]  
                    for idx in range(start, end):
                      res.append(doc[idx].lemma_)
                  
                  return res[0]
                
                stn_text = "the milky way has spiral arms"
                print(extrac_relation(stn_text))
                # >> ['have']
```
So, that's it! We just finished the core part of entity extracion code. Let's put those together.
```
 		stn_text = "the milky way has spiral arms"
                sub, obj = [], []
                chunk_pair = get_entities(stn_text)
                relation = [get_relations(stn_text)]
                if chunk_pair and relation:
                  sub.append(chunk_pair[0].strip())
                  obj.append(chunk_pair[1].strip())

                print("stn:\t{}\nsubject:\t{}\nobject:\t{}\npredicate:\t{}".format(stn_text,sub, obj, relation))
                #stn:    the milky way has spiral arms
                #subject:    ['milky way']
                #object: ['spiral arms']
                #predicate:  ['have']
```
## Knowledge Graph Visualization
- NER visulization
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/NER_example.png)

- KG visulization - song instance (randomly pick 100 songs from wikidata triplets) 
<div align="center">
	<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/songs.png" alt="Editor" width="650">
</div>

- KG visulization (resource: unsupervised information extraction )
<div align="center">
	<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/knownled_graph_information_extraction.png" alt="Editor" width650500">
</div>


## What's New
*  The spacy object has been establish for processing nlp pipline
*  Using BeautifulSoup to craw news from website
*  Finished `gramma matcher`
*  Finished `information extraction` 

## Preparing Dependencies
* [spacy](https://spacy.io/usage)
* [en_core_web_sm](https://spacy.io/usage)

## Install all required dependencies (on terminal)
																* conda env create -f freeze.yml
* python -m spacy download en_core_web_sm											
