import bcrypt
import os

password = "contraseña"

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(10))
hashed = "$2b$10$DRvCS7TJNoy6NIDd3F4yd.zZuts4/NLnX1/lb5Qb5aXYs8TDn9jom"

print(hashed)
print(len(hashed))
if bcrypt.checkpw(password.encode(), hashed.encode()):
    print("si jala")
else:
    print("pendejo")

os.system("pause")
