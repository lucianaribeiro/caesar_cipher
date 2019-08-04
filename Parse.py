import json

class Parse:
    def code():
        with open('answer.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        resp = json.loads(json_str)
        cifrado = resp['cifrado']
        f.close()
        return cifrado
    
    def number():
        with open('answer.json', 'r') as f:
            data = json.load(f)
        
        json_str = json.dumps(data)
        resp = json.loads(json_str)
        number = resp['numero_casas']
        f.close()
        return number