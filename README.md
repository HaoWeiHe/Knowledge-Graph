# Knowledge-Graph


A knowledge graph is a knowledge base that uses a graph-structured data model or topology to integrate data. Knowledge graphs are often used to store interlinked descriptions of entities – objects, events, situations or abstract concepts – with free-form semantics(from wiki). 
Here we demo a basic implementation of a knowledge graph using triples. (There are many various ways to implement KG, and this project demo the basic way which based on syntactic information). 

## Background Knowledge
In this project, we extract relations  from nlp pipeline. If you don't familiar with this. Maybe [my blog](https://haoweihohoho.medium.com/brief-introduce-semantics-syntax-9b84174de947) can provide you a little bit insight.

## NLP Pipeline 
- NER visulization
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/NER_example.png)

- Dependency visulization
![img](https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/Dependency_example.png)

- KG visulization - song instance (randomly pick 100 songs from wikidata) 
<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/songs.png" width="650" height="650">
resource: wikidata triplet

- KG visulization (resource: unsupervised information extraction )
<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/knownled_graph_information_extraction.png" width="650" height="650">

- KG visulization - "appear" instance - pairs whose relation are "appear" (Using unsupervised information extraction tech)
<img src="https://github.com/HaoWeiHe/Knowledge-Graph/blob/main/Img/withappearEdge.png" width="650" height="650">

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
