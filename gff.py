import requests


viewURL = "https://docs.google.com/forms/d/e/1FAIpQLSdH8XBrgstc5rG5OeB4ogOb7b8jxoOtK3woRzhYZhytu_sUDQ/viewform?usp=sf_link"
submitFormURL = "https://docs.google.com/forms/d/e/1FAIpQLSdH8XBrgstc5rG5OeB4ogOb7b8jxoOtK3woRzhYZhytu_sUDQ/formResponse?&pageHistory=0,1,2,3,4"


def send_request_to_form(url, value):
    try:
        requests.post(url, value)
        print("Submitted successfully!")
    except requests.HTTPError:
        print("Unsuccessful!")
    except requests.Timeout:
        print("Timeout!")

    return url


answerValues = {
    # "entry.279816145": "Có",
    # "entry.255472575": "Nữ",
    # "entry.1025981134": "Trên 45",
    # "entry.64279046": "Quảng Nam",
    # "entry.1787404521": "1",
    # "entry.116574743": "Không",
    # "entry.1965288185": "Chưa",
    # "entry.1992272144": "Quan tâm",
    # "entry.990394175": "Chưa",
    # "entry.1316612624": "Thiet bi cam tay",
    # "entry.1968651515": "Chi phí quá cao",
    "entry.276741477": [
        "Gửi thông báo đến điện thoại phụ huynh",
        "Cảnh báo trẻ em khi ra khỏi khu vực an toàn",
    ],
    # "entry.577361753": "Dưới 500.000 VNĐ",
    # "entry.476453814": "a",
}

requestParameters = ""

# For request URL

# def add_to_request_param(key, value):
#     global requestParameters
#     value = value.replace(" ", "%20")
#     requestParameters += "&entry.{key}={value}".format(key=key, value=value)
#
#
# for key, value in answerValues.items():
#
#     if isinstance(value, list):
#         for listValue in value:
#             add_to_request_param(key, value)
#         continue
#
#     add_to_request_param(key, value)

for i in range(1):
    send_request_to_form(submitFormURL, answerValues)
# print(send_request_to_form(viewURL + requestParameters))
