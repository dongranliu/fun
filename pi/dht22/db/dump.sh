t=`date +%Y%m%d%H%M`
/usr/bin/mysqldump -uuser -ppassword -hdbhost te >/home/pi/db/te-$t.sql
if [ $? -eq 0 ];then
	/home/pi/db/osdb
else
	echo "fail"
fi
