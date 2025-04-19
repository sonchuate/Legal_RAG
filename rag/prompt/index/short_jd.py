SHORT_JD_PROMPT = """
-Goal-
Given a piece of recruitment related material, it could be a job description or a resume. Let’s rewrite this document to make it shorter and remove unnecessary information, keeping only the job requirements, workplace (district and city only), and salary.
-Require-
Only return output, no chat-chit.
######################
-Examples-
######################
-Input data-
```
Tên công việc: Kỹ Sư Trí Tuệ Nhân Tạo (NLP)

Mô tả công việc
Phát triển các thư viện cho Xử lý ngôn ngữ tự nhiên, cụ thể bao gồm: Named Entity Recognition, Syntactic Parsing, Coreference Resolution, Topic Modeling, Semantic Role Labeling...
Phát triển các hệ thống tìm kiếm thông tin (Information Retrieval)
Hỗ trợ nghiên cứu, cài đặt các mô hình SOTA của NLP
Yêu cầu ứng viên
Tốt nghiệp Đại học Chính quy loại Khá trở lên chuyên ngànhC NTT, Khoa học máy tính, Trí tuệ nhân tạo, ... hoặc các chuyên ngành liên quan
Có từ 02 năm kinh nghiệm
Tiếng Anh tương đương từ 550 TOEIC (Chưa yêu cầu chứng chỉ khi tuyển dụng)
Có kinh nghiệm nghiên cứu và phát triển trong lĩnh vực Xử lý ngôn ngữ tự nhiên, Trí tuệ nhân tạo, Khai phá dữ liệu, Học máy
Có kinh nghiệm thực hiện các bài toán về NLP: Text classification, Sentiment Analysis, Sequence labeling...
Quyền lợi
Đãi ngộ đáng mơ ước với thu nhập cạnh tranh.
Các khoản phúc lợi bằng tiền mặt: Khoảng hơn 2000$/năm.
Là đồng nghiệp của đội ngũ chuyên gia công nghệ hàng đầu về các lĩnh vực như: DPI (Deep Packet Inspection), BigData, Machine Learning, AI (Artificial Intelligence), Data Mining, Speech Recognition, Virtual Assistant, NLP (Natural Language Processing),....
Xem xét nâng lương hàng năm (tối thiểu 1 năm 1 lần).
Chế độ 12 ngày nghỉ lễ, 12 ngày nghỉ phép và 3 ngày nghỉ dưỡng (trợ cấp 400 USD) hàng năm.
Luôn được hưởng đầy đủ các chế độ BHXH, BHYT, BHTN và nghỉ phép, nghỉ ốm theo luật định sau khi ký Hợp đồng lao động.
Tiếp cận với những cơ hội thăng tiến hấp dẫn.
Khai phá tiềm năng với các khoa đào tạo chuyên sâu về chuyên môn, hội thảo, khoá học theo nguyện vọng cá nhân.
Làm việc trong các dự án trọng điểm của Tập đoàn với quy mô hệ thống lớn.
Trải nghiệm sự đa văn hóa khi làm việc với nhân sự của Viettel tại hơn 10 quốc gia trên thế giới.
Địa điểm làm việc
- Hà Nội
- Hà Nội: Tòa nhà Keangnam - Landmark 72, Nam Từ Liêm, Hà Nội
Thời gian làm việc
Thứ 2 - Thứ 6 (từ 08:30 đến 18:00)
```
-Output data-
```
- Yêu cầu ứng viên: 
Tốt nghiệp Đại học Chính quy loại Khá trở lên chuyên ngànhC NTT, Khoa học máy tính, Trí tuệ nhân tạo, ... hoặc các chuyên ngành liên quan
Có từ 02 năm kinh nghiệm
Tiếng Anh tương đương từ 550 TOEIC (Chưa yêu cầu chứng chỉ khi tuyển dụng)
Có kinh nghiệm nghiên cứu và phát triển trong lĩnh vực Xử lý ngôn ngữ tự nhiên, Trí tuệ nhân tạo, Khai phá dữ liệu, Học máy
Có kinh nghiệm thực hiện các bài toán về NLP: Text classification, Sentiment Analysis, Sequence labeling...
Địa điểm làm việc: Nam Từ Liêm, Hà Nội
```
######################
-Real Data-
######################
-Input data-
{input_text}
Output:
"""