import socket, ssl, base64, struct

class REQ:
    
    def __init__(self):
        #print('test')
        pass
    
    
    def data(self, data=None):
        
        ls = []

        for m, n in data.items():
            ls.append(f'{m}={n}')
            
        zx = '&'.join(ls)
        
        return zx
        
    def hed(self, hed=None):
        
        a = []
        
        for k, v in hed.items():
            if k.__contains__('Content-Length') or k.__contains__('Host'):
                pass
            
            else:
                a.append(f'{k}: {v}\r\n')

        qz = ''.join(a) 
        
        return qz
    
    def proxy(self, s, type, auth=None):


        if type.__contains__('https'):
            
            return self.https(s)
            
                    
        elif type.__contains__('http'): # need test
            
            return s
            
            
        elif type.__contains__('socks4'):
            
            return self.socks4(s)
                
                
        elif type.__contains__('socks5'):
            
            return self.socks5(s)
            
            
        elif type.__contains__('http giga'):
            
            return self.http_auth(s, auth)
            
            
    def http_auth(self, s, auth):
        
        user,pa = auth.split(':')
        auth_a = base64.b64encode(f'{user}:{pa}'.encode()).decode()
        hed = f'CONNECT www.{self.path}:{self.port} HTTP/1.1\r\nHost: www.{self.path}\r\nProxy-Authorization: Basic {auth_a}\r\n\r\n'.encode()
        s.sendall(hed)
        
        response = s.recv(20)
        if not response.__contains__(b'200 OK'): # Need Test Again
            raise Exception('Proxy Failed')
            
        return s
    
    def https(self, s):
        
        s.sendall(f'CONNECT www.{self.path}:{self.port} HTTP/1.0\r\n\r\n'.encode())
        response = s.recv(20)
        #print(response)
        
        return s
        
    def socks4(self, s):
        
        s.sendall(b'\x04\x01' + struct.pack('>H', self.port) + socket.inet_aton(socket.gethostbyname(f'{self.path}')) + b'\x00')
        response = s.recv(8)
        if response[0] != 0x00:
            raise Exception('Bad Proxy')
        
        
        return s
        
        
    def socks5(self, s):
        
        s.sendall(b'\x05\x01\x00')
        response = s.recv(2)
        
        if response[0] != 0x05 or response[1] != 0x00:
            raise Exception('Bad Proxy')
        
        ipz = socket.gethostbyname(f'www.{self.path}')
        
        s.sendall(b'\x05\x01\x00\x03' + chr(len(ipz)).encode() + ipz.encode() + struct.pack('>H', self.port))
        
        response = s.recv(10)
        
        
        if response[0] != 0x05 or response[1] != 0x00:
            raise Exception('Bad Proxy')
        
        return s
    
    
    def verify(self, s):
        
        if self.port == 443:
        
            s = ssl.create_default_context().wrap_socket(s, server_hostname=f'{self.path}')
    
        return s

    def path_de(self, path, hh=None, po=None):
        
        #print(path)
        
        ho, xz = path.split('://')
       # print(ho)
        
        if ho.__contains__('https'):
            po = 443
            #print('port = 443')
            
        elif ho.__contains__('http'):
            #print('port = 80')
            po = 80
        
        z = xz.split('/')
        host = z[0]
        
        z.remove(z[0])
        hh = '/'.join(z)
        
        
        
        hh = '/' + hh
        
        return host, hh, po
    
    
    def get(self, path, **kwargs):
        
        r''''''
        
        return self.send(path, 'GET', **kwargs)
    
    
    def post(self, path, **kwargs):
        
        r''''''
        
        return self.send(path, 'POST', **kwargs)
    
        
    def send(self, path ,method=None, hed=None, data=None, proxy=None, verify=None, proxy_type=None, auth=None, timeout=5):
        
        self.path, hh, self.port = self.path_de(path)
        
        #print(self.port)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

        socket.setdefaulttimeout(timeout)
        ip, port = proxy.split(':')
        s.connect((f'{ip}', int(port)))
        
        s = self.proxy(s, proxy_type, auth)
        
        if verify == None or verify == True:
            s = self.verify(s)

        if proxy_type.__contains__('http'):
            hh = path


        hed = f'{method} {hh} HTTP/1.1\r\nHost: {self.path}\r\nContent-Length: {len(self.data(data))}\r\n{self.hed(hed)}\r\n{self.data(data)}'.encode()
        #print(hed)
        s.sendall(hed)
        
        
        lst = []
        
        while True:
            data = s.recv(1024)
            if (len(data) < 1):
                break
            rr = data.decode()
            lst.append(rr)
        
        qz = ' '.join(lst)
        
        #
        
        s.close()
        
        #ga = (f'{sc}\n\n{qq}')
        
        
        return Response(qz)
        
    
    
class met:
    
    pass
    
    
class Response:
    
    def __init__(self, qz):
        self.qz = qz
    
    @property
    def text(self):
        
        q = self.qz.split('\r\n\r\n')[1]

        return q
    
    
    @property
    def sc(self):
        
        status_code = int(self.qz.splitlines()[0].split(' ')[1])

        return status_code
    

req = REQ()
    
    
    
    
