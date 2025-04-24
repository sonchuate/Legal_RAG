from rag.db.neo4j.utils import Node, Graph, Edge
import re

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
                node_name = self.process_string(node_name)
                node_type = self.process_string(node_type)
                node_description = self.process_string(node_description)

                name2node[node_name] = Node(
                        node_type,
                        {"name": node_name, "node_description": node_description}
                    )

            elif '"relationship"<|>' in line:
                parts = line.strip('()').split('<|>')

                _, node_name_1, node_name_2, rel_type, ao = parts
                node_name_1 = self.process_string(node_name_1)
                node_name_2 = self.process_string(node_name_2)
                rel_type = self.process_string(rel_type)
                ao = self.process_string(ao)

                edges.append(
                    Edge(
                        name2node[node_name_1],
                        name2node[node_name_2],
                        rel_type + "__" + ao
                    )
                )

        return Graph(list(name2node.values()), edges)
    
    def process_string(self, s):
        s = re.sub(r'\s+', ' ', s).strip()
        for c in """%#@!^&*:,/.-+'()\"""":
            s = s.replace(c, '')
        return s.lower().replace(' ', '_')