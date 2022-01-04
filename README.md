# 虚拟主播

- 1、带人脸的静态图输出虚拟主播

## 安装依赖
```
pip3 install -r requirements.txt
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt -i https://pypi.python.org/simple/
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 资源消耗

- CPU: 56%
- 内存: 2%(0.4 GB/16.0 GB)
- 硬盘: 0%(0.0 GB/100.0 GB) 
- GPU: 0% 
- 显存: 0%(0.0 GB/16.0 GB)

## 安装问题
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