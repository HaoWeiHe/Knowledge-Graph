import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
doc = nlp('The US economy lost 140,000 jobs in December.')
for e in doc:
	print("{}\t{}\t{})".format(e, e.ent_iob_,e.ent_type_ ))

from bs4 import BeautifulSoup
import requests
import re
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


news_text = url_to_string('https://www.nytimes.com/2021/01/09/us/politics/capitol-riot-charges.html?action=click&module=Spotlight&pgtype=Homepage')
article = nlp(news_text)
stns = [ x for x in article.sents]

RANDOM_NUM = random.randint(0,len(stns))
from spacy import displacy
displacy.render(nlp(str(stns[RANDOM_NUM])), jupyter=True, style='ent')

