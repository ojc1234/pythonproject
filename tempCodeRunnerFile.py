newlike = collation.find()
for i in newlike:
    t = t +  int(i.get("like"))
print(t)