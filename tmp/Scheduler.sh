tiMe=$(echo $1|cut -d " " -f1)
name=$2
tiMe=`expr $tiMe \* 60`
sleep $tiMe
echo $name
