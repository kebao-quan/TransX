from translate_func import deepl_translate as translate_API

text = "Hello World!"
target = "ZH"

trans_text = translate_API(target,text)

print(f"input: {text}\noutput: {trans_text}")