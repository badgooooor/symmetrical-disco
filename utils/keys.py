from hashlib import blake2b

# This should be in environment variable.
SECRET_KEY = b'zkzkzkzkzkzkzk'

def get_hashed_token(token):
  h = blake2b(digest_size=16, key=SECRET_KEY)
  h.update(token.encode('utf-8'))

  hashed = h.hexdigest().encode('utf-8')
  return hashed