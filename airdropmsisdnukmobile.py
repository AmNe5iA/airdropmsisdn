import hashlib

targetstart = input('Enter the target hash start fragment: ')
targetend = input('Enter the target hash end fragment: ')
print('Checking all UK mobile numbers.  Results will report on completion.')
phonematch = []

line = 0
while line < 1000000000:
    targetphone = '447' + str(line).zfill(9)
    if (line % 1000000 == 0):
        print( 'Checking numbers from ' + str(targetphone) + ' and on...')
    targettest = hashlib.sha256(targetphone.encode())
    starthashcheck = targettest.hexdigest() [0:5]
    endhashcheck = targettest.hexdigest() [-5:]
    if starthashcheck == targetstart.lower() and endhashcheck == targetend.lower():
        phonematch.append(targetphone)
        print(targetphone + ' matches hash fragments.  Still checking...')
    line = line + 1
            
if phonematch:
    print('Your target\'s phone number may be:')
    for match in phonematch:
        print(match)
else:
    print('Target phone number not found.')
