import os
import sys
import hashlib

def sha256(s):
    h=hashlib.sha256()
    h.update(s.encode("utf-8"))
    return h.hexdigest()
    #return (h.digest().encode('hex'))
    #should call binascii.hexlify(h.digest()) and import binascii

MAX=20000
nonceHex=hex(0)
filename=sys.argv[1] #'0.txt'
f=open(filename,'r')
data=f.read()
f.close()
target=sha256(data)
#proof of work is going to add 1 to nonce and see if we can get a value less than the target
print('target')
targetList=list(target)
targetList[0]='0'
targetList[1]='0'
#targetList[2]='0'
#targetList[3]='0'
target="".join(targetList)
print(target)
i=1
h1=sha256(data+nonceHex)
while (i<MAX) and (h1>target):
    nonceHex=hex(i)
    h1=sha256(data+nonceHex)
#    print 'hash:',h1
#    print 'data:',data+nonceHex
    i+=1

print( 'result')
print( i-1)
print( nonceHex)
print( h1)
f=open('dataNonce.txt','w')
f.write(data+nonceHex)
f.close()



