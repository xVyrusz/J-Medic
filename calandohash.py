import bcrypt
import os

password = "jalo"

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(10))

print(hashed)
print(len(hashed))
if bcrypt.checkpw(password.encode(), hashed):
    print("si jala")
else:
    print("pendejo")

os.system("pause")
