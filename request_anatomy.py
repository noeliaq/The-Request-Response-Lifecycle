import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def request_anatomy(response):

    #Inspect what We sent (The request)
    print (f"\n{'=' *20} {response.request.method} REQUEST {'=' *20}")
    print (f"Method: {response.request.method}")
    print (f"URL: {response.request.url}")

    print (f"\n{'*' *10} Request Headers {'*' *10}")
    for key, value in response.request.headers.items():
        print (f" {key} , {value}")

    print (f"\n{'*' *10} Request Body {'*' *10}")
    if response.request.body:
        print (f"{response.request.body}")
    else:
        print (f"{response.request.body} (GET requests do not include a body)")


    #Inspect what SERVER sent back (the response)
    print (f"\n{'*' *10} Status Code and Reason {'*' *10}")
    print (f"Status: {response.status_code}: {response.reason}")
    print (f"\n{'*' *10} Response Headers {'*' *10}")
    
    for key, value in response.headers.items():
        print (f" {key} {value}")
    content_length = response.headers.get("Content-Length", len(response.content))
    print (f" Content-Length: {content_length}")
      
    print (f"\n{'*' *10} Response Body {'*' *10}")
    print(json.dumps(response.json(), indent = 2))

    print (f"\n{'*' *10} Elapsed Time in milliseconds {'*' *10}")
    print (f"Total Time: {response.elapsed.total_seconds():.3f} seconds") 
    print (f"That's {response.elapsed.total_seconds() * 1000:.0f} milliseconds")

result_get = requests.get(f"{BASE_URL}/users/1")
request_anatomy(result_get)

result_post = requests.post(f"{BASE_URL}/posts",
        json={"title": "Lifecycle Demo", "body": "Testing the full cycle", "userId": 1}, #content type -sends a python dictionary as Json #
            headers= {"X-Customer-Header": "learning-apis"})
request_anatomy(result_post)

result_patch = requests.patch(f"{BASE_URL}/posts/1",
        json= {"title": "API's fundamentals"})
request_anatomy(result_patch)


"""Results

(venv) noeliaquiroga@Mac inspect_lifecycle.py % python3 request_anatomy.py

==================== GET REQUEST ====================
Method: GET
URL: https://jsonplaceholder.typicode.com/users/1

********** Request Headers **********
 User-Agent , python-requests/2.34.2
 Accept-Encoding , gzip, deflate, zstd
 Accept , */*
 Connection , keep-alive

********** Request Body **********
None (GET requests do not include a body)

********** Status Code and Reason **********
Status: 200: OK

********** Response Headers **********
 Date Mon, 19 Oct 2026 04:22:15 GMT
 Content-Type application/json; charset=utf-8
 Transfer-Encoding chunked
 Connection keep-alive
 access-control-allow-credentials true
 Cache-Control max-age=43200
 etag W/"1fd-+2Y3G3w049iSZtw5t1mzSnunngE"
 expires -1
 pragma no-cache
 vary Origin, Accept-Encoding
 x-content-type-options nosniff
 x-powered-by Express
 x-ratelimit-limit 3600000
 x-ratelimit-remaining 3599998
 x-ratelimit-reset 1790812826
 Age 18315
 Report-To {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=owBI5IbFh6NbI%2Frz4AqsO0Ni7PH6QcKPIDwuJpRpZpkzjl%2BSOIXF4vq3eAS7GrMu5M2rj6XThWdBPV%2B18piyTRS5GkKkIPjM1oUdLRQMLdwQI6cJx39fr0VS3U2le3oNOxPZT56DpnEZwTlXag2V"}]}
 cf-cache-status HIT
 Nel {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
 Content-Encoding zstd
 Server cloudflare
 CF-RAY a4cd002a184f4e45-BOS
 alt-svc h3=":443"; ma=86400
 Content-Length: 509

********** Response Body **********
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}

********** Elapsed Time in milliseconds **********
Total Time: 0.259 seconds
That's 259 milliseconds

==================== POST REQUEST ====================
Method: POST
URL: https://jsonplaceholder.typicode.com/posts

********** Request Headers **********
 User-Agent , python-requests/2.34.2
 Accept-Encoding , gzip, deflate, zstd
 Accept , */*
 Connection , keep-alive
 X-Customer-Header , learning-apis
 Content-Length , 74
 Content-Type , application/json

********** Request Body **********
b'{"title": "Lifecycle Demo", "body": "Testing the full cycle", "userId": 1}'

********** Status Code and Reason **********
Status: 201: Created

********** Response Headers **********
 Date Mon, 19 Oct 2026 04:22:15 GMT
 Content-Type application/json; charset=utf-8
 Content-Length 95
 Connection keep-alive
 access-control-allow-credentials true
 access-control-expose-headers Location
 Cache-Control no-cache
 etag W/"5f-Id4DQwpAUUeLzFKClkGBt/yJKl4"
 expires -1
 location https://jsonplaceholder.typicode.com/posts/101
 pragma no-cache
 vary Origin, X-HTTP-Method-Override, Accept-Encoding
 x-content-type-options nosniff
 x-powered-by Express
 x-ratelimit-limit 3600000
 x-ratelimit-remaining 3599985
 x-ratelimit-reset 1792386024
 cf-cache-status DYNAMIC
 Nel {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
 Report-To {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=gKLuzwvCCJS3B8Aro0o%2FaxRy6eyPaOauOHjdX4JntPhTqTIy3oWG5e5OxTmSDZFInT3saC8uGK4nV2Mx9B68v9gaVyl884GxNlDfs9A87l8ZvSfB20SJiBqc3dZoIkLH53fu1sJntaKe6swQKqeq"}]}
 Server cloudflare
 CF-RAY a4cd002a6b20a2cd-BOS
 alt-svc h3=":443"; ma=86400
 Content-Length: 95

********** Response Body **********
{
  "title": "Lifecycle Demo",
  "body": "Testing the full cycle",
  "userId": 1,
  "id": 101
}

********** Elapsed Time in milliseconds **********
Total Time: 0.073 seconds
That's 73 milliseconds

==================== PATCH REQUEST ====================
Method: PATCH
URL: https://jsonplaceholder.typicode.com/posts/1

********** Request Headers **********
 User-Agent , python-requests/2.34.2
 Accept-Encoding , gzip, deflate, zstd
 Accept , */*
 Connection , keep-alive
 Content-Length , 31
 Content-Type , application/json

********** Request Body **********
b'{"title": "API\'s fundamentals"}'

********** Status Code and Reason **********
Status: 200: OK

********** Response Headers **********
 Date Mon, 19 Oct 2026 04:22:15 GMT
 Content-Type application/json; charset=utf-8
 Transfer-Encoding chunked
 Connection keep-alive
 access-control-allow-credentials true
 Cache-Control no-cache
 etag W/"ec-yqDXP7jEV5fUQbMVQM9/QDL4RRA"
 expires -1
 pragma no-cache
 vary Origin, Accept-Encoding
 x-content-type-options nosniff
 x-powered-by Express
 x-ratelimit-limit 3600000
 x-ratelimit-remaining 3599984
 x-ratelimit-reset 1792386024
 cf-cache-status DYNAMIC
 Nel {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
 Report-To {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=lKKo%2Bl5fD%2FizdvZF6aoavz5zFCB9Z%2FEumaWS0%2BwenDpYZEAZD%2B2OLktLmz2rbhkbaMV6ufOkcPc5rsEisbZUaw9tuUv8hxrn2z1NkMj8uQiN%2FNPCxOaf0z9cmDEfdzDpsAfLoE8pIJdX54Ul1NJj"}]}
 Content-Encoding zstd
 Server cloudflare
 CF-RAY a4cd002ae89cae27-BOS
 alt-svc h3=":443"; ma=86400
 Content-Length: 236

********** Response Body **********
{
  "userId": 1,
  "id": 1,
  "title": "API's fundamentals",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

********** Elapsed Time in milliseconds **********
Total Time: 0.101 seconds
That's 101 milliseconds
(venv) noeliaquiroga@Mac inspect_lifecycle.py % 


"""