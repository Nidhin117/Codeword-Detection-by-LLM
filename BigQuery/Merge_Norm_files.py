import os
from pathlib import Path

path = Path ('C:\everythingelse\Strath\958\Code\BigQuery\Files')


cword_fname = "NormWord_DS.txt"
log_fname = "NW1.txt"

def logger(fname,msg):
    file= open(fname,'a',encoding='utf-8')
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

target = open (path / 'Normal_Word_file.txt','r')
cw = open (path / cword_fname,'a' )

for l in target:
    sentences = l.split(',')
    log(f"here for Target word {sentences}")
    normal_words = [x.strip().lower() for x in sentences]
    log(normal_words)
    for word in normal_words:
        cw.write(f"-------- {word}------- \n")
        for filename in os.listdir(path / 'Normal_OP'):
            log(f"Here for file name {filename}")

            file = open (path / f'Normal_OP\{filename}','r')
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