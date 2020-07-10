#-*-coding:utf-8-*-
from application import utils

def request_handler(new_client_socket, ip_port):
    #接收客户端请求报文
    request_recv_data = new_client_socket.recv(1024)
    #判断请求报文是否为空
    if not request_recv_data:
        print(f'客户端{ip_port}已下线')
        new_client_socket.close()
        return
    #转换二进制请求报文为字符串
    request_recv_text = request_recv_data.decode()
    #找到请求行的位置
    loc = request_recv_text.find('\r\n')
    #分解出请求行
    recv_text = request_recv_text[:loc]
    #找到请求路径
    request_line_list = recv_text.split(' ')
    file_path = request_line_list[1]
    return file_path

def response_handler(file_path, current_dir):
    #判断请求路径
    if file_path == '/' :
        file_path = '/index.html'
    # else:
    #     file_path = current_dir
    try:
        with open(current_dir + file_path,'rb') as f:
            response_body = f.read()
            #print(current_dir+file_path)
    except Exception as e:
        response_body = f'Eorror！{e}'
        response_body = response_body.encode()
        response_data = utils.create_http_response('404 Not Found',response_body)

    response_data = utils.create_http_response('200 OK',response_body)
    return response_data
        
    


