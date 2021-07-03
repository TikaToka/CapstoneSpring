# CapstoneSpring
## Project Name: "Effective Ways to Select Dataset from Large Corpus"

### Arrangement in Progress!!


### Model

#### Robusk Ranker
##### https://drive.google.com/file/d/1Z3xbRuVaiAOb5ymUh8eanDxoG1FCrMao/view?usp=sharing

#### TIM_PLUS
##### https://drive.google.com/file/d/1uZPgHeL5Ao1HKL4J0j144oWimizhIPW9/view?usp=sharing


### Dataset

#### Robust04
##### https://drive.google.com/file/d/1YxqwHkHQvNWJOoNCva8j_kHFpKxrZXri/view?usp=sharing


### How to Run?

1. Download Models and Dataset and unzip
2. run graph/graph-generator.py to make graph asd (Change data location at line 105 to '/filename.pkl'. Check Readme.docx) 
3. run TIM_PLUS using step 2's result (check README.txt)
4. Use step 3's result to make seed.txt (Just copy the result and write into it)
5. run /graph/create-set.py (data, pkl and seed.txt needed)
6. run /Robust-Ranker-Master/main.py (Check README.md if you need)
7. Compare MAP! ^-^
