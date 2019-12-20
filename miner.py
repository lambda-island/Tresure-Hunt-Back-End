import hashlib
import requests
import random
import time
import os
import sys


def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    - Find a number proof such that hash(proof') contains 6 leading
    zeroes, where proof is the previous proof '
    - proof is the previous proof, and proof' is the new proof
    """

    print("Searching for next proof")
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1

    print("Proof found: " + str(proof))
    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain n
    leading zeroes?
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = int(sys.argv[1])
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"

    coins_mined = 0

    try:
        with open('my_id.txt') as f:
            id = f.readlines()[0]
            f.close()
    except:
        f = open('my_id.txt', 'w')
        f.write(str(uuid4()).replace('-', ''))
        id = f.readlines()[0]
        f.close()

    print(id)

    url = f"{node}/last_proof/"

    print(url)

    headers = {
        "Authorization": f"Token {id}"
    }

    while True:

        # Get the last proof from the server
        r = requests.get(url=url, headers=headers)
        data = r.json()
        print(data.get('proof'))
        new_proof = proof_of_work(data.get('proof'))

        post_data = {
            "proof": new_proof
        }

        time.sleep(2)

        r = requests.post(url=node + "/mine/", headers=headers, json=post_data)

        data = r.json()
        print(data)

        time.sleep(30)
        
