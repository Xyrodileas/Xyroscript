from pygraphviz import *

G=AGraph(strict=True, directed=True)
#Ajout des noeuds
G.add_nodes_from([1,2,3,4,5,6,12,15])
#AJout des arcs
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),(1,12),(1,15),(2,6),(2,12),(3,6),(3,15),(5,15),(6,12)])
#Intitulé du graph'
G.graph_attr['label']='m est un diviseur de n'

G.node_attr['shape']='circle'
G.edge_attr['color']='red'

G.layout(prog='dot')
#Nom du fichier de sortie
G.draw('file.png')