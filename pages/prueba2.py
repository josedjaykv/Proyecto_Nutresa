import base64

encoded_string = "Q1RGe0FuYWxpendhcl9sb2dzX3RlX2RhX2luZm9ybWFjaW9ufQ=="
decoded_string = base64.b64decode(encoded_string).decode('utf-8')

print(decoded_string)
