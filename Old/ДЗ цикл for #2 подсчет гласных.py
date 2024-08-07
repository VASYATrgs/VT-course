name = input("введите предложение")
books = 'IOEAUioeauАЕИЫУОЕЭЮЯЙауыеэоиюяй'
s = 0
for i in name:
    if i in books:
        s = s + 1

print(s)