bytes_obj = "Hello Python".encode('utf-8')
print("Bytes object:", bytes_obj)

str_obj = bytes_obj.decode('utf-8')
print("Bytes to String:", str_obj)

hex_str = bytes_obj.hex()
print("Bytes to hex: ", hex_str)

bytes_from_hex = bytes.fromhex(hex_str)
print("Hex to bytes: ", bytes_from_hex)

byte_array = bytearray("Hello Python", 'utf-8')
print("New bytearray: ", byte_array)

ba_from_bytes = bytearray(bytes_obj)
print("Bytes to bytearray: ", ba_from_bytes)

sliced_bytes = bytes_obj[6:]
print("Sliced bytes: ", sliced_bytes)

byte_array_modified = bytearray(bytes_obj)
byte_array_modified[0] = ord('h')
decoded_modified = byte_array_modified.decode('utf-8')
print("Modified Message: ", decoded_modified)



