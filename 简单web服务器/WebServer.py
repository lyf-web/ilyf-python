#-*-coding:utf-8-*-

import socket
from application import app
import sys
import multiprocessing

class WebServer(object):
    def __init__(self, port):
        super().__init__()
        #创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        #设置端口绑定
        tcp_server_socket.bind(('',port))
        #设置被动模式
        tcp_server_socket.listen(128)
        self.projects_dict = dict()
        self.projects_dict['俄罗斯方块'] = 'elsfk'
        self.projects_dict['飞机大战'] = 'fjdz'
        self.projects_dict['坦克大战'] = 'tkdz'
        self.projects_dict['植物大战僵尸'] = 'zwdzjs'
        self.current_dir = ''
        self.tcp_server_socket = tcp_server_socket
        self.init_projects()

    def init_projects(self):
        #显示菜单
        game_list = list(self.projects_dict.keys())
        for game_num, game_name in enumerate(game_list):
            print(f'{game_num}:{game_name}')
        #接收用户选择
        sel_num = int(input('请选择喜欢玩的游戏：'))
        key = game_list[sel_num]
        print(f'您选择的游戏是：{key}')
        self.current_dir = self.projects_dict[key]


    def start(self):
        print('Web服务器启动成功,等待客户端连接.')
        n = 1
        while True:
            #接收连接并创建新套接字
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print(f'新客户端{ip_port}已上线')
            print(n)
            n += 1
            # t = threading.Thread(target = self.all_func, args = (new_client_socket,ip_port,self.current_dir))
            # t.setDaemon(True)
            # t.start()
            process = multiprocessing.Process(target = self.all_func, args = (new_client_socket, ip_port, self.current_dir))
            process.start()
            new_client_socket.close()
            
    def all_func(self,new_client_socket,ip_port,current_dir):
        file_path = app.request_handler(new_client_socket, ip_port)
        response_data = app.response_handler(file_path, self.current_dir)
        new_client_socket.send(response_data)
        

#主程序入口
def main():
    
    #判断参数个数
    if len(sys.argv) != 2:
        print(sys.argv)
        print('参数个数错误，输入格式为：python 文件名 端口号')
        return
    #判断第二个参数是否为纯数字
    if not sys.argv[1].isdigit():
        print('端口号必须为纯数字')
    port = int(sys.argv[1])

    ws = WebServer(port)
    ws.start()

if __name__ == "__main__":
    main()
