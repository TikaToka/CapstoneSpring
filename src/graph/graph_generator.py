import sys
import pickle
import networkx as nx

def open_file(file_path):
  #open dataset pickle file
  with open(file_path, 'rb') as f:
    data = pickle.load(f)

  return data

def add_nodes(g, data):
  query = {}
  query_ids = []
  for element in data:
    query_id = element['query_id']
    if query_id not in query_ids:
      query_ids.append(query_id)
    
    g.add_nodes_from(element['docs_id'])
    for doc in element['docs_id'] :
      g.nodes[doc][query_id] = element['rel_1d'][element['docs_id'].index(doc)].item()
  return query_ids

def calculate_edge_weight(node1, node2, g):
  queries = g.nodes[node1].keys()
  count = 0
  sum = 0
  weight = 0.0
  for q in queries:
    if(q in g.nodes[node2].keys()):
      sum += g.nodes[node1][q]+ g.nodes[node2][q]
      count += 2
  if count != 0:
    weight = sum/count  
  return weight

def add_edges(g, query_ids):
  nodes = g.nodes()
  for node1 in g.nodes():
    for node2 in g.nodes():
      if(node1 != node2):
        w = calculate_edge_weight(node1, node2, g)
        if w != 0:
          #print(w)
          g.add_edge(node1, node2, weight = w)  

def export_to_pickle(g):
  path = 'graph_digraph.pkl'
  protocol = pickle.HIGHEST_PROTOCOL
  
  pickle.dump(g, open(path, 'wb'), protocol)

def read_from_pickle():
  path = 'graph_digraph.pkl'
  return nx.read_gpickle(path)
 
##############################################
#make a txt files consists of                #
#       graph_lt.txt        #                #
#---------------------------#                #
#Line1   node1 node2 weight #                #
#Line2          //          #                #
#---------------------------#                #
#       attribute.txt       #                #
#---------------------------#                #
#Line1   n=#_of_nodes       #                #
#Line2   m=#_of_nodes       #                #
####################start#####################
def to_imp_input(g):
    f1 = open("attribute.txt", 'w')
    f1.write("n=" + str(g.number_of_nodes()) + "\n") #write attribute
    f1.write("m=" + str(g.number_of_edges()) + "\n")

    
    mapping = {}  # indexing and save id:index dictionary into pickle file, will use https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary when restore
    i = 0;
    for node in list(g.nodes):
        mapping[node] = i
        i += 1
    with open('mapping.pickle', 'wb') as handle:
        pickle.dump(mapping, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    h = nx.relabel_nodes(g, mapping) # relabel graph with mapping
    
    f2 = open("graph_lt.inf", 'w') #make inputfile
    for line in nx.generate_edgelist(h, data=['weight']):
        f2.write(line+'\n')
    
    f3 = open("graph_ic.inf", 'w')
    for line in nx.generate_edgelist(h, data=['weight']):
        f3.write(line+'\n')
    f1.close()
    f2.close()
    f3.close()
#####################end#####################

# Generate Graph
file_path = ''

# get data from input file
# to do: implement for several files
if len(sys.argv) == 1:
 
  file_path = 'Robust-Ranker-master/data/robust04/split_1/prepro.train.pkl'
    
  data = open_file(file_path)

  graph = nx.DiGraph()
  graph.nodes(data = True)
  queries = add_nodes(graph, data)
  add_edges(graph, queries)
  export_to_pickle(graph)
  to_imp_input(graph)
elif sys.argv[1] == 'load':
  graph = read_from_pickle()