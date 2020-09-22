from sys import argv 

print("ideomatic python with 'with' statement:")
with open(argv[2], 'w+') as f:
	f.write(argv[1])
with open(argv[2],'r') as f:
	print(f.read())

print("non-ideomatic and not recommended python:")
f = open(argv[2], 'w+')
f.write(argv[1])
f.close()
f = open(argv[2], 'r')
print(f.read())
