function  for_in_file(){
path_key=''
space='  '
for i in  `cat /home/arvin/PycharmProjects/go/.environmental`
do
    path_key=${path_key}${space}${i%=*}
done
echo $path_key
}

for_in_file
