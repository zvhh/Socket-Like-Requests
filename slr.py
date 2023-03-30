import socket, ssl, base64, struct


# For Any Help Contact Me :
# instagram : zvhk
# email : sami2700@outlook.com
# discord : zvhk#0007

class REQ:
    
    def __init__(self):
        #print('test')
        pass
    
    
    def data(self, data=None):
        
        if not len(data) < 1:
        
            ls = []

            for m, n in data.items():
                ls.append(f'{m}={n}')
                
            zx = '&'.join(ls)
            
            zx = f'Content-Length: {len(zx)}\r\n\r\n{zx}'
            
            return zx
        
    def hed(self, hed=None):
        
        a = []
        
        for k, v in hed.items():
            if 'Content-Length' in k or 'Host' in k:
                pass
            
            else:
                a.append(f'{k}: {v}\r\n')

        qz = ''.join(a) 
        
        return qz
    
    def proxy(self, s, type, auth=None):



        if type == None:
            
            return s

        if 'https' in type:
            
            return self.https(s, auth)
            
                    
        elif 'http' in type:
            
            return s
            
        elif 'socks4' in type:
            
            return self.socks4(s)
                
                
        elif 'socks5' in type:
            
            return self.socks5(s)
        
        
            
            
    # def http_auth(self, s, auth):
        
        
    #     hed = f'CONNECT www.{self.path}:{self.port} HTTP/1.1\r\nHost: www.{self.path}\r\nProxy-Authorization: Basic {auth_a}\r\n\r\n'.encode()
    #     s.sendall(hed)
        
    #     response = s.recv(20)
    #     if not response.__contains__(b'200 OK'): # Need Test Again
    #         raise Exception('Proxy Failed')
            
    #     return s
    
    # def https(self, s, auth):
        
    #     s.sendall(f'CONNECT {self.path}:{self.port} HTTP/1.1\r\nHost: {self.path}{auth}\r\n\r\n'.encode())
    #     response = s.recv(70)
        
    #     if not response.__contains__(b'200'): # Need Test Again
    #         raise Exception('Proxy Failed')
        
    #     return s
    def https(self, s, auth):
        
        s.sendall(f'CONNECT {self.path}:{self.port} HTTP/1.1\r\n\r\n{auth}'.encode())
        response = s.recv(70)
        
        return s
        
    def socks4(self, s):
        
        s.sendall(b'\x04\x01' + struct.pack('>H', self.port) + socket.inet_aton(socket.gethostbyname(f'{self.path}')) + b'\x00')
        response = s.recv(12)
       
        if not response:
            raise Exception('Null')
        
        if response[0] != 0x00:
            raise Exception('Wrong Socks Version')
    
        if response[0:1] != b'\x00':
            raise Exception('Bad Data')
        
        resp = ord(response[1:2])
        
        if resp != 0x5A:
            #print(resp)
            raise Exception('socks4 Error')
        
        
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
        
        ho, xz = path.split('://')
        
        if ho.__contains__('https'):
            po = 443
            
            
        elif ho.__contains__('http'):
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
    
        
    def connect(self, s, proxy):
        
        if proxy == None:
            ip = self.path
            port = self.port
            
        else:
            
            ip, port = proxy.split(':')
            
        s.connect((f'{ip}', int(port)))
        
        return s
        
    def auths(self, auth):
        
        user,pa = auth.split(':')
        auth_a = base64.b64encode(f'{user}:{pa}'.encode()).decode()
        auth = f'\r\nProxy-Authorization: Basic {auth_a}'
        
        return auth
        
    def conf(self, s, path, proxy, proxy_type, auth, verify, hh):
        
        try:
        
            s = self.connect(s, proxy)
            
            if not auth == None:
                
                auth = self.auths(auth)
                
                
            s = self.proxy(s, proxy_type, auth)
            
            if verify == None or verify == True:
                s = self.verify(s)

            if proxy_type == None:
                pass
            
            elif proxy_type.__contains__('http'):
                hh = path
                
        except:
            pass


        return s, hh
        
        
    def send(self, path, method=None, hed=None, data=None, proxy=None, verify=None, proxy_type=None, auth=None, timeout=5):
        
        self.path, hh, self.port = self.path_de(path)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

        socket.setdefaulttimeout(timeout)
        
        s, hh = self.conf(s, path, proxy, proxy_type, auth, verify, hh)
        
        hed = f'{method} {hh} HTTP/1.1\r\nHost: {self.path}\r\n{self.hed(hed)}{self.data(data)}'.encode()
        
        #print(hed, '\n\n')

        s.sendall(hed)
        
        lst = []
        
        while True:
            data = s.recv(1024)
            if (len(data) < 1):
                break
            lst.append(data.decode())
            
    
        qz = ' '.join(lst)
        
        s.close()

        return Response(qz)
        
    
    
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
    
    @property
    def headers(self):
        
        cont = self.qz.split('\r\n\r\n')[0]
        
        return cont
    

req = REQ()
    
    
    
    
