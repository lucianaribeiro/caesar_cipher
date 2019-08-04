import hashlib
import json
import os
from Parse import Parse
from Decode import Decode

class Sha1:
    def resume():
        decoded = Decode.decoding()
        resumo = hashlib.sha1(decoded.encode('utf-8')).hexdigest()
        print(resumo)

        with open('answer.json', 'r') as f:
            data = json.load(f)
            data['resumo_criptografico'] = resumo
        
        os.remove('answer.json')

        with open('answer.json', 'w') as f:
            json.dump(data, f)
        
        f.close()
        