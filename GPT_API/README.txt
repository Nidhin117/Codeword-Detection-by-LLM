To run experiments with GPT we need the need to retrieve API key from the Open AI website.
For this, first create an account on Open AI website and create an API link using the following link : https://platform.openai.com/account/api-keys
Copy the API key and paste it in the file API_Key.txt.

This folder consists of two files:
1) Test_GPT3.py : 
This file reads each line from test dataset and makes an API call to GPT-3.
The results are then output to a file.
The actual outputs generated during my experiments are present in the file name "gpt_test_result2.txt" inside the folder "Files".

2) evaluate_gpt_results.ipynb:
This file is used to evaluate the GPT results.
It produces 2 output files, one file "Result_file2.txt" contains combined results of actual value and predicted values.
For better visualization, another version of this file exists as an excel workbook named "Result_file2.xlsx" inside the folder "Files".
The notebook also produces another file "gpt_CW_stat1.csv" which contain the statistics of the code words identified by GPT-3.

Note: "Files" folder contains actual output files generated during experiments.

