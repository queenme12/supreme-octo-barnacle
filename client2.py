#clinet.py
import socket
import threading

# 定义接收消息的函数，参数是socket对象和服务器地址
def recv(sock, addr):
    '''
    一个UDP连接在接收消息前必须要让系统知道所占端口
    也就是需要send一次，否则win下会报错
    '''
    sock.sendto(name.encode('utf-8'), addr)  # 发送客户端名称到服务器，以便服务器知道客户端身份
    while True:
        data = sock.recv(1024)  # 接收来自服务器的消息
        print(data.decode('utf-8'))  # 打印接收到的消息

# 定义发送消息的函数，参数是socket对象和服务器地址
def send(sock, addr):
    '''
    发送数据的方法
    参数：
        sock：定义一个实例化socket对象
        server：传递的服务器IP和端口
    '''
    while True:
        string = input('')  # 接收用户输入的消息
        message = name + ' : ' + string  # 构造消息格式，包括客户端名称和消息内容
        data = message.encode('utf-8')  # 将消息转换为字节串
        sock.sendto(data, addr)  # 发送消息到服务器
        if string.lower() == 'EXIT'.lower():  # 如果用户输入'EXIT'（不区分大小写），退出循环
            break

# 主函数，设置socket，创建接收和发送的线程
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建UDP socket对象
    server = ('127.0.0.1', 9999)  # 服务器的IP地址和端口
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)  # 创建接收消息的线程，设置为守护线程
    ts = threading.Thread(target=send, args=(s, server))  # 创建发送消息的线程
    tr.start()  # 启动接收消息的线程
    ts.start()  # 启动发送消息的线程
    ts.join()  # 等待发送线程结束，这里可能存在逻辑问题，因为ts.join()应该在tr.join()之后
    s.close()  # 关闭socket

if __name__ == '__main__':
    print("-----,退出请输入'EXIT(不分大小写)'-----")  # 打印欢迎信息
    name = input('请输入你的名称:')  # 获取用户名称
    print('-----------------%s------------------' % name)  # 打印用户名称
    main()  # 执行主函数
 
