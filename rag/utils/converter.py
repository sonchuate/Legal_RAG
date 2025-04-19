from rag.db.neo4j.utils import Node, Graph, Edge

class Converter:
    def __init__(self):
        pass

    def response2graph(self, response:str) -> Graph:
        response = response.split('<|COMPLETE|>')[0]
        name2node = {}
        edges = []

        for line in response.split('##'):
            if line.startswith('("entity"'):
                _, node_name, node_type, node_description, _ = line.split('<|>')
                node = Node(node_type.upper(), {"name": node_name, "node_description": node_description})
                name2node[node_name] = node
        
            if line.startswith('("relationship'):
                _, node_name_1, node_name_2, rel_type, ao = line[1:-1]
                edges.append(Edge(name2node[node_name_1], name2node[node_name_2], rel_type + "|" + ao))

        return Graph(name2node.values(), edges)
