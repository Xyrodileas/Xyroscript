from pygraphviz import *

G=AGraph(strict=True, directed=True)
#Ajout des noeuds
nodes = [1,2,3,4,5,6,12,15]
G.add_nodes_from(nodes)
#AJout des arcs
edges = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,12),(1,15),(2,6),(2,12),(3,6),(3,15),(5,15),(6,12)]
G.add_edges_from(edges)
#Intitulé du graph'
G.graph_attr['label']='m est un diviseur de n'

G.node_attr['shape']='circle'
G.edge_attr['color']='red'

G.layout(prog='dot')
#Nom du fichier de sortie
fich = sys.argv[1]+".png"
G.draw(fich)