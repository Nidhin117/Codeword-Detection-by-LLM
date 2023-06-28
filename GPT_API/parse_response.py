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
   

print(list_stmts[1])