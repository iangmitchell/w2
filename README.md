chmode +x generateFiles.sh
./generateFiles.sh
cat ?.txt

Information that is fed into Pow algorithm
File structure: 
amount receiver nonce
space is separator
For example
100 1 0xf1, would be 100 coins sent to user 1, and nonce value 0xf1.

Block structure
with exception of block 0, see above
amount receiver nonce previousHash
space separator
For example
200 2 0x219  00783789046f0679a243eec821522a4175dd0b24c6462a8cd5adbff888acc058
200 coins sent to user 2, with nonce value 0x219 and previous hash of block

For block 0;
get the nonce
python3 nonce.py 0.txt
get consensus
create the chain in the next block, using 1.txt
cat dataNonce.txt >> 0.blk


For block 1 onwards:
Repeat
get the nonce
python nonce.py *i*.txt
get consensus
create the block
cat dataNonce.txt >> *i*.blk
add the previous hash
echo -n ' ' $(shasum -a 256 *i-1*.txt | awk {'print $1'}) >> *i*.blk
until (i==n)
where *i* is the block number
