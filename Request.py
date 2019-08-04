import requests
import json

class Request:
    
    def get():
        r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b023a1db4aa90bb8ce037431636ce1fee82075c2')

        data = r.json()

        with open('answer.json', 'w') as f:  
            json.dump(data, f)
    
    def post():
        url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=b023a1db4aa90bb8ce037431636ce1fee82075c2'
        answer = {'answer':  open('answer.json', 'rb')}
        response = requests.post(url, files=answer)
        print(response.status_code)
        print(response.json())


