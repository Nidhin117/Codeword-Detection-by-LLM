To use the Hugging Face APIs we need to obtain the API credentials from the Hugging Face website.
For this, first create an account on Hugging Face website and create an SSH key for API using the following link : https://huggingface.co/settings/tokens
Once the key is obtained, paste it inside the file: "HuggingFace_API.txt"

The folder contains 3 files:
1)Test_Bart_Large.py
2)Test_DeBERTa_V3_Base_MNLI.py
3)evaluate_bart_deberta_res.ipynb

1)Test_Bart_Large.py
This file will extract each sentence from the dataset "CombinesDS_2.txt" and invoke the Hugging Face API to test the model facebook/bart-large-mnli.
The results are then output to a file named "bart_test_result1.txt"
The actual file generated during my experiment is present in the folder "Files"

2)Test_DeBERTa_V3_Base_MNLI.py
This file will extract each sentence from the dataset "CombinesDS_2.txt" and invoke the Hugging Face API to test the model MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli.
The results are then output to a file named "deberta_test_result1.txt"
The actual file generated during my experiment is present in the folder "Files"

3)evaluate_bart_deberta_res.ipynb
This notebook will evaluate the results of both the models and create a consolidated file that contains actual values and predicted values from both models.
The actual file generated during my experiments is inside the "Files" folder named "Result_file_bart_deberta1.txt".
For better visualisation, an excel workbook version of same file is also present in same folder "Result_file_bart_deberta1.xlsx"