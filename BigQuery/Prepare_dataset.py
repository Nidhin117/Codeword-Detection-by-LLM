import os
from google.cloud import bigquery
from google.api_core.exceptions import BadRequest

log_fname = "Log_MainDNM2.txt"
cword_fname = "CodeWord_SentencesDNM2.txt"

def logger(fname,msg):
    file= open(fname,'a')
    file.write(f'{msg} \n')
    file.close()

def init_write(fname, text):
    file= open(fname,'w')
    file.write(text + '\n')
    file.close()

def log(msg):
    global log_fname
    logger(log_fname, msg)


init_write(log_fname,"Logging starts")
init_write(cword_fname," ")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\everythingelse\\Strath\\958\\Code\\BigQuery\\researchproposal.json'
client = bigquery.Client()

file = open ("Code_word_file.txt",'r')
words_found =[]
words_notfound = []

for l in file:
    
    sentences = l.split(':')
    log(f"here for Target word {sentences[0]}")
    code_words = sentences[1].split(',')
    code_words = [x.strip().lower() for x in code_words]
    log(code_words)
    for word in code_words:
        log(f"Here for code word -> {word}")
        sql_query = f'''
        SELECT body FROM `fh-bigquery.reddit_comments.2016_08` where subreddit=\'DarkNetMarkets\' and lower(body) like \'%{word}%\'
        and length(body) < 250
        LIMIT 5
        '''
        try:
            query_job = client.query(sql_query)
        except BadRequest as e:
            print(f"Encountered a bad request error:\n{e}")

        except Exception as e:
            print(f"Encountered an error:\n{e}")
        log(f"Exception is {query_job.exception()}")
        log(f"Number of rows {query_job.result().total_rows}")
        if query_job.result().total_rows == 0 :
            words_notfound.append(word)
        elif query_job.result().total_rows > 0 :
            words_found.append(word)
            logger(cword_fname,f"---------{word}------------")
            for row in  query_job.result():
                s = row.body
                logger(cword_fname, s.strip())

log(f"Words found {words_found}")
log(f"Words not found{words_notfound}")
print("Finished Execution")
    