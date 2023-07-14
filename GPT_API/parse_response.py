import re

response = '''1) Present: Yes, Code word: pot, Code word meaning: Marijuana
2) Present: Yes, Code word: coke, Code word meaning: Cocaine
3) Present: No
4) Present: Yes, Code word: grass, Code word meaning: Marijuana
5) Present: Yes, Code word: peruvian, Code word meaning: Cocaine'''

#print (response)
res = response.split('\n')
dict={}
#print(res)
list_stmts=[]
for stmt in res:
    stmt_split = stmt.split(",")
    list_stmts.append(stmt_split)
    # for rec in stmt_split:
    #     key, value = rec.split(":")
    #     dict[key]=value
    #     print(key)
   

#print(list_stmts[1])

#response2 = "Present: Yes, Code word: coke, Code word meaning: Cocaine"
#response2 =  "Present: No"
#response2 = "Present: Yes, Code word: crystal, Code word meaning: Crystal methamphetamine "
response2 = "Present: Yes, Code word: fish scale, Code word meaning: Cocaine"
val = response2.split(",")
present = val[0].split(":")[1]
print(present)
if present.lower().strip() == "yes":
    code_word = val[1].split(":")[1]
    cw_meaning = val[2].split(":")[1]
    pattern = r'Present\s*:\s*yes*\s*\,\s*Code word\s*:\s*\w*\s*\w*\s*\,\s*Code word meaning\s*:\s*\w*\s*\w*\s*'
    match = re.fullmatch(pattern,response2,re.IGNORECASE)
    if match:
        print("Pattern matches")
        print (f"Present {present} , code word is {code_word}, cw meaning is {cw_meaning}")
    else:
        print("Pattern does not match")
        
else:
    pattern = r'Present\s*:\s*no\s*'
    match = re.fullmatch(pattern,response2,re.IGNORECASE)
    if match:
        print("Pattern matches No")
    else:
        print("Pattern does not match no")
        



