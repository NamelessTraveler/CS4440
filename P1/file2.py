#!/usr/bin/env python3
# coding: iso-8859-1
   
MSG = bytes(r"""                                                             - �\���@~�&��P3��!��Tj�~��*�U��n��f|	��8��-�N����ځ�#���7a��IYȻi������t׫[O�%A�|�m��W����R�F�dAu�ρ�4�Izl��
""", "iso-8859-1")
from hashlib import sha256
print(sha256(MSG).hexdigest())