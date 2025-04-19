from rag.db.neo4j.utils import Node, Graph, Edge

class Converter:
    def __init__(self):
        pass

    def response2graph(self, response: str) -> Graph:
        response = response.split('<|COMPLETE|>')[0]
        name2node = {}
        edges = []

        for line in response.split('\n'):
            line = line.strip()
            if not line:
                continue

            if '"entity"<|>' in line:
                parts = line.strip('()').split('<|>')
                _, node_name, node_type, node_description, _ = parts
                print(node_name)
                name2node[node_name] = Node(
                    node_type.upper(),
                    {"name": node_name, "node_description": node_description}
                    )

            elif '"relationship"<|>' in line:
                parts = line.strip('()').split('<|>')
                _, node_name_1, node_name_2, rel_type, ao = parts
                edges.append(Edge(
                    name2node[node_name_1],
                    name2node[node_name_2],
                    rel_type + "|" + ao
                ))

        return Graph(list(name2node.values()), edges)