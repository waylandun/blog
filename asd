export MY_CONTAINER="pytorch_py3_ubuntu2204"
num=`docker ps -a|grep "$MY_CONTAINER" | wc -l`
echo $num
echo $MY_CONTAINER
if [ 0 -eq $num ];then
docker run -it \
--privileged \
--pid=host \
--net=host \
--device /dev/cambricon_dev0 \
--device /dev/cambricon_ctl \
--device /dev/cambricon_ipcm0 \
--name $MY_CONTAINER \
-v /ai:/ai \
-v /public_hanwj:/public_hanwj \
-v /usr/bin/cnmon:/usr/bin/cnmon \
yellow.hub.cambricon.com/pytorch/pytorch:v1.17.0-torch1.13.1-ubuntu20.04-py310 \
/bin/bash
else
docker start $MY_CONTAINER
docker exec -ti $MY_CONTAINER /bin/bash
fi