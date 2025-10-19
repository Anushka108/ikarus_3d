import requests, time
base='http://127.0.0.1:8000'
print('Polling root...')
for i in range(10):
    try:
        r=requests.get(base+'/',timeout=5)
        print('Root status',r.status_code,r.text)
        break
    except Exception as e:
        print('Root not ready, retry',i,e)
        time.sleep(1)

print('Calling /recommend (this may take long for first load)...')
try:
    r=requests.get(base+'/recommend', params={'query':'modern wooden chair'}, timeout=300)
    print('Recommend status', r.status_code)
    try:
        print(r.json())
    except Exception as e:
        print('Failed to parse JSON:', e, '\nRaw text:', r.text[:1000])
except Exception as e:
    print('Request failed:', e)
