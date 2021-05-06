import base64

def encodeString(inputString):
    message_bytes = inputString.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

# message = "dipankar"
# print(encodeString(message))