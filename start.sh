#/bin/bash

# 스크립트 설명: 서비스를 시작
# 재시작시 백앤드에서 코드를 수정하면 반영이 되지만 프론트 앤드는 반영이 안되어서 build.sh부터 실행시켜줘야함


input=$1
if [ "$input" = "--build" ]; then
    # 프론트 빌드 폴더 구성
    mkdir -p ./omilzomil/frontend/dist/css
    mkdir -p ./omilzomil/frontend/dist/img
    mkdir -p ./omilzomil/frontend/dist/js
    mkdir -p ./webrtc/frontend/dist/css
    mkdir -p ./webrtc/frontend/dist/img
    mkdir -p ./webrtc/frontend/dist/js
    # 프론트 빌드
    echo [+] frontend build
    sudo docker-compose --env-file .env.lock build web_vue camera_vue  
    sudo docker-compose --env-file .env.lock up web_vue
    sudo docker-compose --env-file .env.lock up camera_vue

    echo [+] frontend build 대기

    while sudo docker-compose --env-file .env.lock ps --services --filter status=running | grep -q 'vue'; do
        echo `sudo docker-compose --env-file .env.lock ps --services --filter status=running`
        wait_time=`date +%T`
        echo frontend $wait_time
        sleep 1;
    done;


    echo [+] Checking build files...
    while [ ! -f ./omilzomil/frontend/dist/index.html ] ; do
        wait_time=`date +%T`
        echo [!] omilzomil 프론트 빌드 실패 - $wait_time
        sleep 1;
    done
    while [ ! -f ./webrtc/frontend/dist/index.html ] ; do
        wait_time=`date +%T`
        echo [!] webrtc 프론트 빌드 실패 - $wait_time
        sleep 1;
    done
fi

echo [+] Checking build files...
if [ ! -f ./omilzomil/frontend/dist/index.html ] ; then
    echo "[!] Please run 'build.sh' first! - omilzomil front NONE"
    exit
fi
if [ ! -f ./webrtc/frontend/dist/index.html ] ; then
    echo "[!] Please run 'build.sh' first! - webrtc front NONE"
    exit
fi


echo [+] run web camera
sudo docker-compose --env-file .env.lock up web camera