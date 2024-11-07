import hashlib

def calculate_sha256_checksum(file_path):
  sha256_hash = hashlib.sha256()
  with open(file_path, 'rb') as f:
    for byte_block in iter(lambda: f.read(4096), b""):
      sha256_hash.update(byte_block)
  return sha256_hash.hexdigit()

original_file = ''
original_hashsum = calculate_sha256_checksum(original_file)

encrypt_file = ''
encrypt_hashsum = calculate_sha256_checksum(encrypt_file)

if original_file == encrypt_file:
  print("das ist good")
else:
  print("not good")
