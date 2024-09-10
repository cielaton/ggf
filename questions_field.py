import requests
from ast import literal_eval
import re

URL = "https://docs.google.com/forms/d/e/1FAIpQLSdH8XBrgstc5rG5OeB4ogOb7b8jxoOtK3woRzhYZhytu_sUDQ/viewform?usp=sf_link"
response_HTML = requests.get(URL).text

# print(response_HTML)

formContent = re.findall("FB_PUBLIC_LOAD_DATA.*$", response_HTML)[0]
splittedField = formContent.split("]],[")

questions = []

# Obtain the questions
for value in splittedField:
    if value is not None:

        # find anything that inside a double
        toBeAdded = re.findall('"(.*?)"', value)
        if len(toBeAdded) != 0:

            # The first element will be the question, append it to the list
            # Check for the raw string \n
            if "\\n" in toBeAdded[0]:
                questions.append(toBeAdded[0].replace("\\n", "\n"))
                continue

            questions.append(toBeAdded[0])
    # print(value)
    # print("\n")

for value in questions:
    print(value)
    print("\n")
