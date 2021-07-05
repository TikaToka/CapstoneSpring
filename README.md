# CapstoneSpring
## Project Name: "Effective Ways to Select Dataset from Large Corpus"
#### [Video](https://drive.google.com/file/d/1izaw2MqWYFViPmLNyYPHrrCP-gJq0IKt/view?usp=sharing) [PPT](https://github.com/TikaToka/CapstoneSpring/blob/main/presentation/Effective%20Ways%20to%20Select%20Dataset%20from%20Large%20Corpus.pptx)

### Arrangement in Progress!!

#### This project is organized for 'CSI4101: Capstone Design(1)' class. 
#### Idea originated from Prof. Jinyeong Yeo @ Convei lab in Yonsei Univ.
#### Assist was given by Gayeon Lee @ Convei Lab in Yonsei Univ.

#### Most of the NLP datasets are so big that lead developers to spend a lot of time and costs to train model. To reduce this burden, We propose a new approach that reduces size of data and improves performances.

### Model

#### - Robusk Ranker (https://arxiv.org/abs/1904.07094)
##### https://drive.google.com/file/d/1Z3xbRuVaiAOb5ymUh8eanDxoG1FCrMao/view?usp=sharing

#### - TIM_PLUS (https://arxiv.org/abs/1404.0900)
##### https://drive.google.com/file/d/1uZPgHeL5Ao1HKL4J0j144oWimizhIPW9/view?usp=sharing


### Dataset

#### - Robust04 (https://trec.nist.gov/data/robust/04.guidelines.html)
##### https://drive.google.com/file/d/1YxqwHkHQvNWJOoNCva8j_kHFpKxrZXri/view?usp=sharing


### How to Run?

1. Download Models and Dataset and unzip
2. run graph/graph-generator.py to make graph asd (Change data location at line 105 to '/filename.pkl'. Check Readme.docx) 
3. run TIM_PLUS using step 2's result (check README.txt)
4. Use step 3's result to make seed.txt (Just copy the result and write into it)
5. run /graph/create-set.py (data, pkl and seed.txt needed)
6. run /Robust-Ranker-Master/main.py (Check README.md if you need)
7. Compare MAP! ^-^
