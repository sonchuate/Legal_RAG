from rag.prompt.index.extract_graph import GRAPH_EXTRACTION_PROMPT
from rag.llm.llm_gemini import GeminiLLM
from rag.db.neo4j.utils import Node, Edge, Graph, GraphManager
from rag.utils.converter import Converter

class GraphExtractor:
    def __init__(self, config, llm_type:int=0):
        self.llm_type = llm_type
        if llm_type == 0:
            self.llm  = GeminiLLM(config)
        else:
            raise Exception('Unsupport llm_type', llm_type)

        self.converter = Converter()

    def get_graph(self, input_text:str, entity_types:str, return_ans:bool=False) -> Graph:
        ans = self.llm.chat([
            {'role':'user','content':GRAPH_EXTRACTION_PROMPT.format(entity_types = entity_types, input_text = input_text)}
            
        ])
        if return_ans:
            graph = None
            try: 
                graph = self.converter.response2graph(ans)
            except:
                print('err')
            return graph, ans
        return self.converter.response2graph(ans)
    



if __name__ == "__main__":
    import time
    for i in range(1, 35):
        with open(f'E:/data/jd/{i}.txt', 'r', encoding='utf-8') as f:
            input_text = f.read()

        config = {'gemini_key':'AIzaSyCMChcFML_dA97fNRD0i-gm2xXBA3PVz0Q'}
        st = time.time()
        entity_types = 'JOB NAME, COUNTRY NAME, CITY NAME, DISTRICT NAME, LANGUAGE, PROGRAMMING LANGUAGE, SOFTWARE, SALARY, EXPERIENCE, EDUCATION LEVEL, MAJOR, TECHNOLOGY STACK, SKILL, CERTIFICATE, SCORE, CATEGORY, LIBRARY, JOB CANDIDATE'

        ge = GraphExtractor(config)



        graph, ans = ge.get_graph(input_text, entity_types, return_ans=True)
        with open(f'E:/data/jd/{i}_.txt', 'w', encoding='utf-8') as f:
            f.write(ans)
        print('/> exec time:', time.time() - st)
    # print('converter')
    # for node in graph.list_nodes:
    #     print(f"{node.label} - {node.properties}")

    # for edge in graph.list_edges:
    #     node1 = edge.src_node
    #     node2 = edge.trg_node
    #     rel_type = edge.rel_type
    #     print(f"{node1.label} - {node1.properties}")
    #     print(f"{node2.label} - {node2.properties}")
    #     print(rel_type)
    # print('/> exec time:', time.time() - st)