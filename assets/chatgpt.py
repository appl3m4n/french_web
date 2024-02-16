import webbrowser
import time
import openai

str1 = 'sk-DUcs51jM5Pz0NeyLnWyY'
str2 = 'T3BlbkFJkkvbdmHt'
str3 = 'MslyktK7xLis'


openai.api_key = str1 + str2 + str3

x = "Give me 7 ideas for a date in Paris"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": x}])
y = [completion.choices[0].message.content]
#chatgpt = "xxx"

html_content = f"<html> <head> </head> {y} <body> </body> </html>"

with open("index_gpt.html", "w") as html_file:
    html_file.write(html_content)
    print("Html file created successfully !!")

time.sleep (2)
webbrowser.open_new_tab("index_gpt.html")