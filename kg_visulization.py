import pandas as pd
df = pd.read_csv("query.csv")
df['source'] = df["item"].apply(lambda _: "song" )
df['relation'] = df["item"].apply(lambda _: "instance_of" )
kg_df = pd.DataFrame({'source':df['source'] , 'target':df['itemLabel'], 'edge':df['relation']})

#create directed graph from df
def KG_visual(df):
	import networkx as nx
	G = nx.from_pandas_edgelist(df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

	import matplotlib.pyplot as plt
	plt.figure(figsize=(12,12))
	pos = nx.spring_layout(G)
	nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
	plt.show()

KG_visual(kg_df)
KG_visual(kg_df[kg_df['edge']=="instance_of")
