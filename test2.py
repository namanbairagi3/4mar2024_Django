import base64

# Example base64 encoded string
encoded_string = "SGVsbG8gV29ybGQh"

# Decode the base64 string
decoded_string = base64.b64decode(encoded_string).decode('utf-8')

# Print the decoded string
print(decoded_string)
    



