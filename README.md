# Knowledge-Graph
## Features
* Information Extraction
* Entity-Chunk Extraction
* Predicate Extraion
* Dependency Tree
* Knowledge Graph Visualization

## What's New
*  Finish `show` to get result of visualization
*  Finish `get_entity` to get chunk information
*  Finish `get_relation` to get relation between entities
*  Sorted up Knowledge graph module
*  Finished `gramma matcher`
*  Finished `information extraction` 

## Preparing Dependencies
* conda env create -f freeze.yml
* python -m spacy download en_core_web_sm													

## Usage
Get the Entity Chunk. Sample code: 
```
from knowledgeGraph import get_entity		
text = "the milky way has spiral arms" 
output = get_entity(text)
print(output)
 ```
output :  ('milky way', 'spiral arms')

<br><br>
Get Relation. Sample code:
```
from knowledgeGraph import get_relation		
text = "the milky way has spiral arms" 
output = get_relation(text)
print(output)
 ```
output :   'have'

<br><br>
Visualization. Sample code
```
from knowledgeGraph import show		
text = "the milky way has spiral arms" 
show("the milky way has spiral arms")
 ```
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/triple_gen.png)
<br><br>

## Online Demo 
[http://www.haoweihohoho.com/KGDemo](http://www.haoweihohoho.com/KGDemo) - For the triplet extraction

## Intorduction
A knowledge graph is a structured graph from multiple sources standardized to acquire and integrate human knowledge. Knowledge graphs are often used to store interlinked descriptions of entities – objects, events, situations or abstract concepts – with free-form semantics(from wiki). Here we demo one way of implementation using triples as our data format. (There are many various ways to implement KG, and this project demonstrates the automatic way based on the result of information extraction).


## Background Knowledge
Let's took the most common knowledge graph - Wikidata for example. One way to implement KG is using a concept of triple, which is a statement in "subject/predicate/object" form. A statement linked one entity(subject) to another (object) via a predicate. For example, *the milky way has spiral arms*. The triple is going to be like this :
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
However, when an entity could not only just a single word but a chunk - which means multiple words should be put together. In this case, we could leverage a dependency tree and gramma rules to help us to extract chunks as our entities.

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


