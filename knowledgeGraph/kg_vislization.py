import knowledgeGraph
import pandas as pd

class Visualize():

	def get_df(self):
		
		sub, obj = [], []
		chunk_pair = knowledgeGraph.get_entity(self.stn)
		relation = [knowledgeGraph.get_relation(self.stn)]
		if chunk_pair and relation:
		  sub.append(chunk_pair[0].strip())
		  obj.append(chunk_pair[1].strip())

		return pd.DataFrame({'subj':sub , "obj":obj, "rel": relation})

	#create directed graph from df
	def show(self,stn = None):
		self.stn = stn
		df = self.get_df()
		if stn == None:
			return None
		
		import networkx as nx
		g = nx.from_pandas_edgelist(df,
		                            'subj',
		                            'obj',
		                             edge_attr='rel',
		                             create_using=nx.DiGraph(),) 

		import matplotlib.pyplot as plt
		pos = nx.random_layout(g)
		nx.draw_networkx_edge_labels(g, pos)
		edge_labels = nx.get_edge_attributes(g, "rel")
		nx.draw(g, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos, node_size=1800,width=2)
		plt.axis('off')
		axis = plt.gca()
		plt.tight_layout()
		plt.show()




