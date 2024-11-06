import hashlib

init_data = input()
encrypt_data = input()

if hashlib.sha256(init_data) == hashlib.sha256(encrypt_data):
  print("yes")
