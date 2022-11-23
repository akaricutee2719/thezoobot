import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "739371bde39f6ceb4007eadd6ff13f89"
    
    }

conn.request("GET", "/fixtures/events?fixture=215662", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))