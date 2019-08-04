import json
import string
import os
from Parse import Parse

class Decode:
    def decoding():
        code = Parse.code().lower()
        number = Parse.number()
        result = ''
        letters = string.ascii_lowercase

        for letter in code:
            if letter.isalpha():
                position = letters.find(letter)
                if position > number:
                    position = position - number
                    result = result + letters[position]
                if position <= number:
                    position = position - 27
                    result = result + letters[position]
            
            if not letter.isalpha():
                result += letter
        
        return result
    
    def saveDecode():
        decode = Decode.decoding()
        with open('answer.json', 'r') as f:
            data = json.load(f)
            data['decifrado'] = decode
        
        os.remove('answer.json')

        with open('answer.json', 'w') as f:
            json.dump(data, f)
        
        f.close()   