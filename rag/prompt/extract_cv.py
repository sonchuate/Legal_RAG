CV_EXTRACT_GRAPH_PROMPT = """
-Goal-
Given a piece of Curriculum Vitae. Let identify all entities of those types from the text and all relationships among the identified entities.

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
```
Kiến thức
Ngôn ngữ lập trình: Python, C/C++, Java.
Kinh nghiệm sử dụng các thư viện Tensorflow, Pytorch, Paddlepaddle.
```
######################
Output:
```
("entity"<|>Ngôn ngữ lập trình<|>CATEGORY<|>A category encompassing all programming languages known or used by the individual, representing foundational technical skills>)
##
("entity"<|>Python<|>Programming Language<|>A versatile, high-level programming language widely used in data science, web development, scripting, and AI applications>)
##
("entity"<|>C/C++<|>Programming Language<|>Low-level, high-performance languages used extensively in systems programming, embedded systems, and performance-critical software>)
##
("entity"<|>Java<|>Programming Language<|>A platform-independent, object-oriented programming language commonly used for enterprise software and Android application development>)
##
("entity"<|>Tensorflow<|>LIBRARY<|>An open-source deep learning framework developed by Google, supporting large-scale machine learning and neural network training>)
##
("entity"<|>Pytorch<|>LIBRARY<|>A flexible, Python-based deep learning framework developed by Meta, commonly used in academic and research settings for AI and neural networks>)
##
("entity"<|>Paddlepaddle<|>LIBRARY<|>An industrial-grade deep learning platform developed by Baidu, optimized for training and deploying AI models in production>)
##
("entity"<|>ỨNG VIÊN<|>JOB CANDIDATE<|>Candidate apply for jobs, providing skills and experience.<|>)
##
("relationship"<|>ỨNG VIÊN<|>NGÔN NGỮ LẬP TRÌNH<|>Candidate should be able to use NGÔN NGỮ LẬP TRÌNH<|>AND>)
##
("relationship"<|>NGÔN NGỮ LẬP TRÌNH<|>Python<|>Python is part of the set of programming languages known by the individual<|>AND>)
##
("relationship"<|>NGÔN NGỮ LẬP TRÌNH<|>C/C++<|>C/C++ is part of the set of programming languages known by the individual<|>AND>)
##
("relationship"<|>NGÔN NGỮ LẬP TRÌNH<|>Java<|>Java is part of the set of programming languages known by the individual<|>AND>)
##
("relationship"<|>Python<|>Tensorflow<|>Tensorflow is one of the machine learning libraries of Python<|>AND>)
##
("relationship"<|>Python<|>Pytorch<|>Pytorch is one of the machine learning libraries of Python<|>AND>)
##
("relationship"<|>Python<|>Paddlepaddle<|>Paddlepaddle is one of the machine learning libraries of Python<|>AND>)
<|COMPLETE|>
```

######################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################  
Output:"""