import base64

base64_message = "b'MDZFbzhPVTNldTY='"
decrypt = base64_message[2:18]
base64_bytes = decrypt.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')


print(len(message))