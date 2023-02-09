from pymd5 import md5, padding
m = "&user=admin&command1=ListFiles&command2=NoOp&command3=UnlockAllSafes"
h = md5()
h.update(m)
print(h.hexdigest())
