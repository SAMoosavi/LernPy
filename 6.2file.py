import datetime
import json

now = datetime.datetime.now

a = open('6.2file.txt', 'w')
a.write(f"now {str(now())}\n")
a.close()

a = open('6.2file.txt', 'r')
print(a.read())
a.close()

with open('6.2file.txt', 'a') as f:
    for i in range(15):
        f.write(f"{i}: {str(now())}\n")

with open('6.2file.txt', 'r') as f:
    for i in f:
        print(i, end='')
        if i[0] == '9':
            break
    print(f.readline(), end='')

a = {'year': now().year, 'month': now().month, 'day': now().day}
f = open('6.2file.json', 'w')
f.write(json.dumps(a))
f.close()

with open('6.2file.json', 'r') as f:
    print(json.loads(f.read()))
