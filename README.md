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


## Information extraction / Entity extraction
To build up a knowledge graph, it's important to extract nodes and the relation between them. There are several **unsupervised manners** to do the information extraction. On syntactic level, we could leverage part-of-Speech (POS) tags to help us extract this information, or, on semantic level, we can use Semantic Role Labeling (SRL) technique to help us extract entities.
<br><br>
In this article, we will focus on syntactic level with POS technique which is one of efficient ways to do it.
<br><br>
However, when an entity could not only just a single word but a chunk - which means multiple words should be put together. In this case, we could leverage a dependency tree to help us to extract chunks as our entities.
<br><br>
Let's see how to extract chunks through a sentence. Noun related tags will be the entities (Subject/ Object) and the dependency between them will be the relation (Predicate).

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

## Install all required dependencies
```conda env create -f freeze.yml```
