import os
from pathlib import Path

path = Path ('C:\everythingelse\Strath\958\Code\BigQuery\Files')


cword_fname = "CodeWord_DS.txt"
log_fname = "CW1.txt"

def logger(fname,msg):
    file= open(fname,'a')
    file.write(f'{msg} \n')
    file.close()

def log(msg):
    global log_fname
    logger(path / log_fname, msg)

def init_write(fname):
    file= open(fname,'w')
    file.close()

init_write(path / cword_fname)
init_write(path / log_fname)

target = open (path / 'Code_word_file.txt','r')
cw = open (path / cword_fname,'a' )

for l in target:
    sentences = l.split(':')
    log(f"here for Target word {sentences[0]}")
    code_words = sentences[1].split(',')
    code_words = [x.strip().lower() for x in code_words]
    log(code_words)
    for word in code_words:
        cw.write(f"-------- {word}------- \n")
        for filename in os.listdir(path / 'Output'):
            log(f"Here for file name {filename}")

            file = open (path / f'Output\{filename}','r')
            counter = 0
            for line in file:
                #print(line)
                if "---" in line:
                    continue
                elif word in line:
                    cw.write(f'{line.strip()} \n')
                
            file.close()

print("Done")
target.close()
cw.close()