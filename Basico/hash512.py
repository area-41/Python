import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
print(m.hexdigest())
m.update(b" the spammish repetition")
print(m.hexdigest())

print(f"Hash da Frase:\n{hashlib.sha256(b'Frase que eu quero calcular o Hash!').hexdigest()}")

text = hashlib.sha3_512(b"Nobody inspects", usedforsecurity=True)
print(text)
print(text.hexdigest())

def hash(n):
  return ((0x0000FFFF & n)<<16) + ((0xFFFF0000 & n)>>16)

print(hash(35545))