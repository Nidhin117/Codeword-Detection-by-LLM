import requests
import numpy as np
import pandas as pd
import time

file = open("./HuggingFace/HuggingFace_API.txt","r")
API_TOKEN= file.read()
file.close()
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
#headers = {"Authorization": "Bearer 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"}
log_fname = "bart_test_log1.txt"
result_file = "bart_test_result1.txt"

df =  pd.read_csv('./BigQuery/Files/CombinesDS_2.txt', delimiter='|')
dataset_size = 0.5

def format_msg(msg):
    msg = msg.rstrip().replace("'","")
    if msg[-1] != ".":
        msg += "."
    return msg

def logger(fname,msg):
    file= open(fname,'a',encoding='utf-8')
    file.write(f'{msg} \n')
    file.close()

def init_write(fname, text):
    file= open(fname,'w',encoding='utf-8')
    file.write(text + '\n')
    file.close()

def log(msg):
    global log_fname
    logger(log_fname, msg)

def call_bart(payload):
    err_flag = False
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json(),err_flag
    except Exception as e:
        err_flag=True
        err_msg = f"Exception raised {e}"
        return err_msg,err_flag

    

init_write(log_fname,"Logging starts")
init_write(result_file," ")

# output = query({
#     "inputs": "Lol, that shit is probably so stepped on you can't even call it coke anymore.",
#     "parameters": {"candidate_labels": ["code word for drug", "food", "faq","drink","verb"]}
# })

counter = 0 
prompt_msg = ""
exception_counter = 0 
parameters = {"candidate_labels": ["sentence with code word for drugs", "normal sentence"]}

for index,row in df.iterrows():
    if index == (int(len(df)*dataset_size)): # stop at 50% of dataset 
    #if index == 5: # stop at 50% of dataset 
        break
    log (f" Sentence: {row['Sentences']}")
    counter += 1
    prompt_msg =  f"{ format_msg(row['Sentences'])}" 
    task_prompt = {"inputs": prompt_msg, "parameters":parameters }
    #log(task_prompt)
    output,err_flg = call_bart(task_prompt)
    log (f"{output['labels']}, {np.argmax(output['scores'] )}" )
    if not err_flg:
        try:
            idx = np.argmax(output['scores'])
            op_label = output['labels'][idx]
            if op_label == "sentence with code word for drugs":
                present = "yes"
            else:
                present = "no"
            logger(result_file,f"{row['Sentences']} | {present} | NA | NA")  
        except Exception as e:
            log(f"In exception due to {e}")
            exception_counter += 1
            logger(result_file,f"{row['Sentences']} | In exception {e} | NA | NA")
    else:
        exception_counter += 1
        log(f"In API exception{output}")
        logger(result_file,f"{row['Sentences']} | In API exception {output} | NA | NA")
    if exception_counter == 10:
        log("Encountered too many exceptions, going to exit")
        break
    time.sleep(0.1)

print("Done with execution")