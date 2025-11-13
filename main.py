import marshal, zlib, base64

kgs_access_key = b"khansir6342"

def xor_dec(data: bytes, kgs_access_key: bytes) -> bytes:
    return bytes([data[i] ^ kgs_access_key[i % len(kgs_access_key)] for i in range(len(data))])

with open("kgs_access.bin", "rb") as f:
    encrypted = base64.b64decode(f.read())

decompressed = xor_dec(encrypted, kgs_access_key)
bytecode = zlib.decompress(decompressed)
code = marshal.loads(bytecode)
exec(code)