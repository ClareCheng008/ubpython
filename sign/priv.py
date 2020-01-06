#!/usr/bin/env python3
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


if __name__ == '__main__':
    sha256 = SHA256.new()
    sha256.update(b"asus project sign test.")
    print(sha256.hexdigest())
    
    private_key = False
    with open("rsa_private_key.pem", "r") as f:
        private_key = RSA.importKey(f.read())
    public_key = False
    with open("rsa_public_key.pem", "r") as f:
        public_key = RSA.importKey(f.read())
    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(sha256)
    print(signature)
#    sign_content = b64encode(signature)

    verifier = PKCS1_v1_5.new(public_key)
    if(verifier.verify(sha256, signature)):
        print("This signture is true.")
    else:
        print("This signture is false.")



