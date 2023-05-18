import base64

with open('anon.session', 'rb') as f:
    data = f.read()
    encoded_data = base64.b64encode(data)
    print(encoded_data)
