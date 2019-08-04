import requests
from Request import Request
from Parse import Parse
from Sha1 import Sha1
from Decode import Decode

def main():
    Request.get()
    Decode.saveDecode()
    Sha1.resume()
    Request.post()

if __name__ == '__main__':
    main()