#-*-coding:utf-8-*-

def create_http_response(status,response_body):
    response_line = f'HTTP/1.0 {status}\r\n'
    response_header = 'Server:Python_web_server/1.0\r\n'
    response_header += 'Content-Type: text/html\r\n'
    response_blank = '\r\n'
    response_data = (response_line + response_header +response_blank).encode() + response_body
    return response_data
