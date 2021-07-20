# Knowledge-Graph


A knowledge graph is a structured graph from multiple sources standardized to acquire and integrate human knowledge. Knowledge graphs are often used to store interlinked descriptions of entities – objects, events, situations or abstract concepts – with free-form semantics(from wiki). Here we demo a basic implementation of a knowledge graph using triples. (There are many various ways to implement KG, and this project demonstrates the automatic way based on the result of information extraction).


## Background Knowledge
In this project, we extract relations  from nlp pipeline. If you don't familiar with this. Maybe [my blog](https://haoweihohoho.medium.com/brief-introduce-semantics-syntax-9b84174de947) can provide you a little bit insight.

## NLP Pipeline 
- NER visulization
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/NER_example.png)

- Dependency visulization
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/Dependency_example.png)

- KG visulization - song instance (randomly pick 100 songs from wikidata triplets) 
<div align="center">
	<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/songs.png" alt="Editor" width="650">
</div>

- KG visulization (resource: unsupervised information extraction )
<div align="center">
	<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/knownled_graph_information_extraction.png" alt="Editor" width650500">
</div>

- KG visulization - "appear" instance - pairs whose relation are "appear" (Using unsupervised information extraction tech)
<div align="center">
	<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/withappearEdge.png" alt="Editor" width="650">
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
