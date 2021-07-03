import networkx as nx
import pickle
import json
import torch 
import numpy as np

def open_pkl_file(file_path):
  print('Opening pickle file')
  return nx.read_gpickle(file_path)

def load_seed_set(file_path):
  print('Opening seed file')
  data = ''
  with open(file_path) as f:
    data = f.read()
  
  return data.split(' ')

def create_data(graph, seed, data):
  print('Creating data')
  obj = {}
  pick_data = []
  nodes_lst = list(graph.nodes())
  for q in data:
    docs_id = []
    query_new = []
    query_len_new = []
    docs_new = []
    docs_len_new = []
    rel_1d_new = []

    query_id = q['query_id']
    query = q['query'].numpy()
    query_len = q['query_len'].numpy()
    docs = q['docs'].numpy()
    docs_len = q['docs_len'].numpy()
    rel_1d = q['rel_1d'].numpy()
    for node_idx in seed:
        node_id = nodes_lst[int(node_idx)]
        if node_id in q['docs_id']:
            docs_id.append(node_id)
            idx = q['docs_id'].index(node_id)
            docs_len_new.append(docs_len[idx])
            query_new.append(query[idx])
            query_len_new.append(query_len[idx])
            docs_new.append(docs[idx])
            rel_1d_new.append(rel_1d[idx])
    doc_size = len(docs_id)
    obj = {'dsize': doc_size,
    'query_id': query_id,
    'query': torch.tensor(query_new),
    'query_len': torch.tensor(query_len_new),
    'docs_id': docs_id,
    'docs': torch.tensor(docs_new),
    'docs_len': torch.tensor(docs_len_new),
    'rel_1d': torch.tensor(rel_1d_new)}
    pick_data.append(obj)

  return pick_data

def write_data(data):
  print('Writing to json')
  with open('data_set.json', 'w') as f:
    json.dump(data, f)

def write_to_pickle(data):
  with open('/content/drive/My Drive/graph/data_set.pickle', 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

########### MAIN ###############
graph_path = "/content/drive/My Drive/graph/graph_digraph.pkl"
data_path = "/content/drive/My Drive/graph/prepro.train.pkl"
seed_set_path = "/content/drive/My Drive/graph/seed.txt"

data = {'id'}
#load files
graph = open_pkl_file(graph_path) 
data_set = open_pkl_file(data_path)
seed = load_seed_set(seed_set_path)
data = create_data(graph, seed, data_set)
write_to_pickle(data)
#write_data(data)
print('All done!')