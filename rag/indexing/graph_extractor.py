from rag.prompt.index.extract_graph import GRAPH_EXTRACTION_PROMPT
from rag.llm.llm_vllm import vLLM_LLM

if __name__ == "__main__":
    import time
    input_text = \
"""Mức phạt lỗi không đội mũ bảo hiểm năm 2025 là bao nhiêu? 
(1) Mức phạt lỗi không đội mũ bảo hiểm năm 2025 đối với xe đạp, xe đạp máy
Theo quy định tại khoản 4 Điều 9 Nghị định 168/2024/NĐ-CP thì phạt tiền từ 400.000 đồng đến 600.000 đồng đối với người điều khiển xe thực hiện một trong các hành vi vi phạm sau:

- Gây tai nạn giao thông không dừng ngay phương tiện, không giữ nguyên hiện trường, không trợ giúp người bị nạn, không ở lại hiện trường hoặc không đến trình báo ngay với cơ quan công an, Ủy ban nhân dân nơi gần nhất;

- Điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở;

- Không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ;

- Người điều khiển xe đạp máy không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách khi tham gia giao thông trên đường bộ;

- Chở người ngồi trên xe đạp máy không đội “mũ bảo hiểm cho người đi mô tô, xe máy” hoặc đội “mũ bảo hiểm cho người đi mô tô, xe máy” không cài quai đúng quy cách, trừ trường hợp chở người bệnh đi cấp cứu, trẻ em dưới 06 tuổi, áp giải người có hành vi vi phạm pháp luật.

Như vậy, mức phạt lỗi không đội mũ bảo hiểm năm 2025 đối với người điều khiển xe đạp, xe đạp máy sẽ bị phạt tiền từ 400.000 đồng đến 600.000 đồng. 
"""
    llm  = vLLM_LLM({'url':'https://7d2c-34-71-230-150.ngrok-free.app'})
    st = time.time()
    print(llm.chat([
        {'role':'system','content':'You are a traffic assistant'},
        {'role':'user','content':GRAPH_EXTRACTION_PROMPT.format(entity_types ="person, law name, traffic violation, fine, object, traffic regulation, age", input_text = input_text)}
        
    ]))
    print('/> exec time:', time.time() - st)