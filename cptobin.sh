if [[ $(id -u) -ne 0 ]] ; then 
	echo "Please run as root" 
	exit 1 
 fi
cp selectSS.py  /bin/ss