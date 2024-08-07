import pickle
import os
filename = "Userstore"
userdict = {}
if os.path.isfile(filename):
    userdict = pickle.load(open(filename, "rb"))
username = input("введите имя пользователя?")
password = input("введите пароль?")
userdict[username] = password
print(userdict)
pickle.dump(userdict, open("Userstore", "wb"))