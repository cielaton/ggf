import requests
import re

URL = "https://docs.google.com/forms/d/e/1FAIpQLSdH8XBrgstc5rG5OeB4ogOb7b8jxoOtK3woRzhYZhytu_sUDQ/viewform?usp=sf_link"
response_HTML = requests.get(URL).text

# print(response_HTML)

formContent = re.findall("FB_PUBLIC_LOAD_DATA.*$", response_HTML)[0]
splittedField = formContent.split(",")
splittedQuestions = []


for value in splittedField:
    toBeAdded = re.findall('^".*"', value)
    if not 
    splittedQuestions.append()

for value in splittedQuestions:
    print(value)
    print("\n")

print(formContent)
