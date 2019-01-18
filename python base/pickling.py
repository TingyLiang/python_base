import pickle

d = dict(name="abc", age=20)

f = open("pickling_dumps.txt", "wb")
print(pickle.dumps(d))

pickle.dump(d, f)
f.close()

f = open("pickling_dumps.txt", "rb")
print(pickle.load(f))
f.close()
