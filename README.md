chmode +x generateFiles.sh
./generateFiles.sh

cat ?.txt
#get the nonce
#get consensus
python3 nonce.py 0.txt
#create the chain in the next block, using 1.txt
echo -n $(shasum -a 256 dataNonce.txt | awk {'print $1'}) >> 1.txt
#find the nonce and repeat 7-8 for 2. and 3.txt

