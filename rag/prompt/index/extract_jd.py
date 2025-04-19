JD_EXTRACT_GRAPH_PROMPT = """
-Goal-
Given a piece of Job Description. Let identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
 Format each entity as ("entity"<|><entity_name><|><entity_type><|><entity_description>)
 
2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- condition: is logical "AND" or "OR" if present.
 Format each relationship as ("relationship"<|><source_entity><|><target_entity><|><relationship_description><|><condition>)
 
3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **##** as the list delimiter.
 
4. When finished, output <|COMPLETE|>
 
-Requirements-
Represents hierarchical relationships between entities.
Only mentions technology requirements, no skill.
If there is only 1 node and no other equivalent node, condition takes the default value of "AND".
source_entity should cover target_entity.

######################
-Examples-
######################
Input:
Yêu cầu ứng viên
- Tốt nghiệp đại học chính quy chuyên ngành: Công nghệ thông tin, Tự động hóa, Điều khiển tự động, etc.,
- Có kinh nghiệm sử dụng một trong các ngôn ngữ lập trình C, C#, VB, Python, etc.,
- Có tinh thần tự giác học hỏi, nghiêm túc trong công việc
- Tiếng Anh: Đọc hiểu, giao tiếp
- Ưu tiên ứng viên đã có 1 năm kinh nghiệm
- Biết đồng thời 2 thư viện torch và tenserflow.
- Làm việc tại Nam Từ Liêm, Hà Nội
######################
Output:
("entity"<|>CÔNG NGHỆ THÔNG TIN<|>Major<|>A university major focusing on computer systems, software development, networks, and algorithms, providing foundational knowledge for careers in IT and programming.<|>)
##
("entity"<|>TỰ ĐỘNG HÓA<|>Major<|>An academic discipline centered on the automation of industrial systems and processes through control systems and electronics.<|>)
##
("entity"<|>ĐIỀU KHIỂN TỰ ĐỘNG<|>Major<|>A field of study dealing with automatic control systems, emphasizing control engineering, robotics, and automation.<|>)
##
("entity"<|>C<|>Programming Language<|>A low-level, procedural programming language commonly used in embedded systems and operating system development.<|>)
##
("entity"<|>C#<|>Programming Language<|>A high-level, object-oriented language developed by Microsoft, used in enterprise application development and Windows environments.<|>)
##
("entity"<|>VB<|>Programming Language<|>Visual Basic, a Microsoft language for building user-friendly desktop applications and GUIs.<|>)
##
("entity"<|>PYTHON<|>Programming Language<|>A versatile, high-level programming language popular in data science, automation, artificial intelligence, and web development.<|>)
##
("entity"<|>TIẾNG ANH<|>Skill<|>English language proficiency, particularly in reading comprehension and verbal communication in a professional context.<|>)
##
("entity"<|>1 NĂM<|>Experience<|>Indicates that the candidate has at least one year of professional experience relevant to the job position.<|>)
##
("entity"<|>ỨNG VIÊN<|>JOB CANDIDATE<|>An individual applying for the position, expected to meet the technical, academic, and behavioral criteria specified in the job description.<|>)
##
("entity"<|>TORCH<|>LIBRARY<|>An open-source deep learning framework developed by Facebook, primarily used for building and training neural networks using Python.<|>)
##
("entity"<|>TENSORFLOW<|>LIBRARY<|>An open-source machine learning library developed by Google, widely used for training deep learning models and building AI systems.<|>)
##
("entity"<|>NAM TỪ LIÊM<|>Location<|>A district in the western part of Hanoi, Vietnam, known for its rapid development and concentration of tech companies and offices.<|>)
##
("entity"<|>HÀ NỘI<|>Location<|>The capital city of Vietnam, a major hub for education, technology, and business activities.<|>)
##
("relationship"<|>ỨNG VIÊN<|>CÔNG NGHỆ THÔNG TIN<|>The candidate must have a degree in Information Technology.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>TỰ ĐỘNG HÓA<|>The candidate must have a degree in Automation.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>ĐIỀU KHIỂN TỰ ĐỘNG<|>The candidate must have a degree in Automatic Control.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>C<|>The candidate is required to have experience in using the C programming language.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>C#<|>The candidate is required to have experience in using the C# programming language.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>VB<|>The candidate is required to have experience in using Visual Basic programming language.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>PYTHON<|>The candidate is required to have experience in using Python programming language.<|>OR)
##
("relationship"<|>ỨNG VIÊN<|>TIẾNG ANH<|>The candidate must be able to read and communicate effectively in English.<|>AND)
##
("relationship"<|>ỨNG VIÊN<|>1 NĂM<|>Preferred candidates have at least one year of relevant work experience.<|>AND)
##
("relationship"<|>PYTHON<|>TORCH<|>Torch is a python library for deep learning.<|>AND)
##
("relationship"<|>PYTHON<|>TENSORFLOW<|>TENSORFLOW is a python library for deep learning.<|>AND)
##
("relationship"<|>ỨNG VIÊN<|>HÀ NỘI<|>The candidate will work at a location in Hà Nội.<|>AND)
##
("relationship"<|>HÀ NỘI<|>NAM TỪ LIÊM<|>Hà Nội contains Nam Từ Liêm<|>AND)
<|COMPLETE|>

######################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################  
Output:"""