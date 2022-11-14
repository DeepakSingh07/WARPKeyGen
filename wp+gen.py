import random
import grequests
import time
import requests as rrr
ppkeys = rrr.get('https://keyses-for-generator.serdarad.repl.co/')
pkeys = ppkeys.content.decode('UTF8')
keys = pkeys.split(',')


a = 0
# Самый обычный цикл while
while True:
        a += 1
        try:
            # Header with variables
            headers = {
                "CF-Client-Version": "a-6.11-2223",
                "Host": "api.cloudflareclient.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1",
            }

            base = ["https://api.cloudflareclient.com/v0a2223"]
            requests = (grequests.post(f"{u}/reg",headers=headers) for u in base)
            responses = grequests.map(requests)
            id = [response.json() for response in responses][0]["id"]
            license = [response.json() for response in responses][0]["account"]["license"]
            token = [response.json() for response in responses][0]["token"]

            requests = (grequests.post(f"{u}/reg",headers=headers) for u in base)
            responses = grequests.map(requests)
            id2 = [response.json() for response in responses][0]["id"]
            token2 = [response.json() for response in responses][0]["token"]

            headers_get = {"Authorization": f"Bearer {token}"}
            headers_get2 = {"Authorization": f"Bearer {token2}"}
            headers_post = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token}",
            }

            json = {"referrer": f"{id2}"}
            (grequests.put(f"{u}/reg/{id}", headers=headers_post, json=json)  for u in base)
            (grequests.delete(f"{u}/reg/{id2}", headers=headers_get2) for u in base)
            
            key = random.choice(keys)

            json = {"license": f"{key}"}
            (grequests.put(f"{u}/reg/{id}/account", headers=headers_post, json=json) for u in base)
            json = {"license": f"{license}"}
            (grequests.put(f"/reg/{id}/account", headers=headers_post, json=json) for u in base)

            #r = client.get(f"/reg/{id}/account", headers=headers_get)
            requests = (grequests.get(f"{u}/reg/{id}/account", headers=headers_get) for u in base)
            responses = grequests.map(requests)
            account_type = [response.json() for response in responses][0]["account_type"]
            referral_count = [response.json() for response in responses][0]["referral_count"]
            license = [response.json() for response in responses][0]["license"]

            grequests.map([grequests.delete(f"{u}/reg/{id}", headers=headers_get) for u in base])
            if referral_count == 1:
                with open('gened1GB.txt','a') as f:
                    f.write(license + '\n')
            else:
                with open('gened12PB.txt','a') as f:
                    f.write(license + '\n')
            if a % 2 == 0:
                time.sleep(60)
        except:
            print('Er')
        if a % 2 == 0:
            time.sleep(60)