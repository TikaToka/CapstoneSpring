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
      count += 1
  if count != 0:
    weight = sum/count
  return weight

def add_weights(g):
  edges = g.edges()
  for edge in edges:
    node1 = g.nodes[edge[0]]
    node2 = g.nodes[edge[1]]  
    
def add_edges(g, query_ids, data):  
  for q_item in data:
    docs = q_item['docs_id']
    for x in docs:
      edges = [(x,y) for y in docs[:docs.index(x)]+docs[docs.index(x)+1:]]
      #print(edges)
      g.add_edges_from(edges)

def export_to_pickle(g):
  path = 'graph_v2.pkl'
  protocol = pickle.HIGHEST_PROTOCOL

  pickle.dump(g, open(path, 'wb'), protocol)

# Generate Graph
file_path = ''

# get data from input file
# to do: implement for several files
if len(sys.argv) != 1:
  file_path = sys.argv[0]
else:
  file_path = './prepro.train.pkl'
  
data = open_file(file_path)

graph = nx.Graph()
graph.nodes(data = True)
queries = add_nodes(graph, data)
add_edges(graph, queries, data)
#add_weights(graph)
export_to_pickle(graph)