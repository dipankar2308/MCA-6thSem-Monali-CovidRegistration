import base64

def decodeString(inputString):
    base64_bytes = inputString.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

# base64_message = 'UHl0aG9uIGlzIGZ1bg=='
# print(decodeString(base64_message))