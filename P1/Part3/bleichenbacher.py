from roots import *
import hashlib
import sys

message = sys.argv[1]
# Your code to forge a signature goes here!

prefix = '0001FF003021300906052B0E03021A05000414'
arbitrary_bytes = '00' * 217

md5 = hashlib.sha1()
md5.update(message.encode())
md5_hash = md5.hexdigest()

prefix_hash = prefix + md5_hash
forged_signaure = prefix_hash + arbitrary_bytes

int_result, bool_result = integer_nthroot(int(forged_signaure, 16), 3)

if bool_result == False:
    int_result += 1


print(integer_to_base64(int_result))