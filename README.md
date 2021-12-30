# 虚拟主播

- 1、带人脸的静态图输出虚拟主播

技术实现原理如下：
首先，把图像放入FOM进行面部表情迁移，让虚拟主播的表情更加逼近真人，既然定位是一个主播，那表情都参考当然是要用“国家级标准”的，所以BoBo参考的对象是梓萌老师~
同时，通过PaddleSpeech的TTS模块，将输入的文字转换成音频输出。
得到面部表情迁移的视频和音频之后，通过Wav2Lip模块，将音频和视频合并，并根据音频内容调整唇形，使得虚拟人更加接近真人效果。

## 安装依赖
```
pip3 install -r requirements.txt
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt -i https://pypi.python.org/simple/
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

```
Centos 7提示ImportError: /usr/lib64/libstdc++.so.6: version `CXXABI_1.3.8' not found错误的解决办法

1.通过下面的命令查看/usr/lib64/下的动态库版本
strings /usr/lib64/libstdc++.so.6 | grep 'CXXABI'

查询结果动态库的版本就到1.3.7。

2.从网上下载所需要的libstdc++.so.6.0.22版本，为了方便可以从本站直接下载：libstdc++.so.6.0

3.将下载好的libstdc++.so.6.0.22解压缩后上传到Centos 7系统的/usr/lib64目录下。

4.切换到/usr/lib64目录。
cd /usr/lib64

5.删除原来的libstdc++.so.6软连接。
rm -rf libstdc++.so.6

6.新建软连接。
ln -s libstdc++.so.6.0.22 libstdc++.so.6


wget https://ftp.gnu.org/gnu/glibc/glibc-2.18.tar.gz --no-check-certificate

tar -xvf glibc-2.18.tar.gz

我这里需要修改 /etc/profile 中的这行字 不然会报错 

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
export LD_LIBRARY_PATH

成这样

LD_LIBRARY_PATH=/usr/local/lib
export LD_LIBRARY_PATH

编译安装
cd glibc-2.18

mkdir build

cd build

../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin

make && make install
```