# Socket-Like-Requests
Send Requests With Socket Like The Default Requests Module in Python

# Download
```pip install socket_like_requests```


  ```python
  # this is how to import it
from socket_like_requests import REQ

```

# POST Method With

 Requests Module :


  ```python
r = requests.post('example.com')

```


My Module :


  ```python
r = REQ().post('example.com')

```
</p>
</details>


# Headers

Requests Module


  ```python
  
  
  hed = {}
  hed["header"] = "value"
  hed["header"] = "value"
  hed["header"] = "value"
    
  data = {}
  data["Key1"] = "Value1"
  data["Key2"] = "Value2"
  data["Key3"] = "Value3"
  
r = requests.post('example.com', headers = hed, data = data)

```
</p>
</details>

My Module


  ```python
  hed = {}
  hed["header"] = "value"
  hed["header"] = "value"
  hed["header"] = "value"
    
  data = {}
  data["Key1"] = "Value1"
  data["Key2"] = "Value2"
  data["Key3"] = "Value3"
  
r = REQ().post('example.com', headers = hed, data = data)

```
</p>
</details>



# **Add Proxy**


  Add Proxy ```ip:port``` Format
  
  Example :
  
  ```python
  r = REQ().post('example.com', proxy = 'ip:port', proxy_type = 'socks4')

```
  and the proxy type : ```http, socks4, socks5```
  
</p>
</details>

# Add ssl


  
  ```python
r = REQ().post('example.com', verify = True)

```
  
  if you don't want to use ssl replace it with ```False```
  
</p>
</details>

# Add Timeout


  Default Timeout is 5 , but you can change it like this :
  
  ```python
r = REQ().post('example.com', timeout = 5)

```
 
  
</p>
</details>

# Print Response


  To Print Response :
  
  ```python
r = REQ().post('example.com')
  print(r.text)

```
  
 
  
</p>
</details>

# Print Status Code


  To Print Status Code :
  
  ```python
r = REQ().post('example.com')
  print(r.sc)

```

  
</p>
</details>

# Full Usage


  
  ```python
  hed = {}
  hed["header"] = "value"
  hed["header"] = "value"
  hed["header"] = "value"
    
  data = {}
  data["Key1"] = "Value1"
  data["Key2"] = "Value2"
  data["Key3"] = "Value3"
  
r = REQ().post('example.com', headers = hed, data = data, proxy = 'ip:port', proxy_type = 'socks4', verify = True, timeout = 5)
  print(r.text, r.sc)

```

  
</p>
</details>
