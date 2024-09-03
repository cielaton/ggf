import requests


def viewForm(url):
    try:
        requests.get(url)
        print("Submitted successfully!")
    except requests.HTTPError:
        print("Unsuccessful!")
    except requests.Timeout:
        print("Timeout!")

    return url


answerValues = {"279816145": "Có", "255472575": "Nam"}
requestParameters = ""
for key, value in answerValues.items():
    requestParameters += "&entry.{key}={value}".format(key=key, value=value)

print(
    viewForm(
        "https://docs.google.com/forms/d/e/1FAIpQLSdH8XBrgstc5rG5OeB4ogOb7b8jxoOtK3woRzhYZhytu_sUDQ/viewform?usp=sf_link"
        + requestParameters
    )
)
