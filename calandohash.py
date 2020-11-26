import bcrypt
import os

password = "contraseña"

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(10))
hashed = b'$2b$10$p6f6qaN3GTNUCYR0TTtJdeb8pcLcQ4cRo/rxFRNd44y67qvGDcqje'
print(hashed)
print(hashed.decode())
if bcrypt.checkpw(password.encode(), hashed):
    print("si jala")
else:
    print("pendejo")

os.system("pause")
