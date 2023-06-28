import openai

API_KEY='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'
openai.api_key = API_KEY
model_name = "gpt-3.5-turbo"
# list models
#models = openai.Model.list()
#print(models)
response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are an investigator looking for code word for drugs hidden in sentences. Learn from the given examples and fill in the answer by replacing question marks in each of the numbered sentences"},
        {"role": "user", "content": "Lol, that shit is probably so stepped on you can't even call it coke anymore."},
        {"role": "assistant", "content": "Present: Yes, Code word : coke, Code word meaning : Cocaine"},
        {"role": "user", "content": "No one would resist a pot of soup"},
        {"role": "assistant", "content": "Present:No"},
        {"role": "user", "content": "1)My cousin did the same and when the legalized pot in dc they really started cracking down in virginia and maryland. Present: ? \\n 2)for all vendors of coke it seems pretty obvious that it is not as pure as they market it. Present: ?\\n 3)i understand this is to get more customers but imo its bullshit. Present: ?\\n 4)is there any tests that show the real purity of the grass vendors sell. Present: ?\\n 5) i know whit doc got caught with 50 peruvian,but is there tests of other vendors product. Present: ?\\n"}
    ],
    temperature=0,
)

print(response)
print(response["choices"][0]["message"]["content"])