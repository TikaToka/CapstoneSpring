# Influence Maximization problem

### networkx vs other packages
#### https://www.timlrx.com/2019/05/05/benchmark-of-popular-graph-network-packages/

### installing networkx
<pre>
<code>
pip install networkx
pip install pytest
</code>
</pre>

* Graph realization
    + Node: doc_id
        * attributes: {query_id: rel_1d}
    + Edge: relation between nodes
        * Q(q) - all queries that node1 and node2 participate
        * weight:  ∑(q)/n 

*	Implementation:
    + version 1: 
        - step 1: create nodes
        - step 2: between every two nodes calculate weight
        - step 3: connect those nodes 
        - Conclusion: takes several hours to be done (around 7 hours)
    + version 2:
        - step 1: create nodes
        - step 2: make list of all edges (in networkx edges can be assigned as list of tuples [(node1, node2)]
        - step 3: connect them at once
        - Conclusion: Failed in allocating memory for that many edges
* How to run
    + for creating a graph: 
        <pre>
        <code>
        python generate_graph.py
        </code>
        </pre>
    + for loading a graph:
        <pre>
        <code>
        python generate_graph.py load
        </code>
        </pre>
