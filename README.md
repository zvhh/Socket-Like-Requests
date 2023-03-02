# Socket-Like-Requests
Send Requests With Socket Like The Basic Requests Module


# POST Method With :

<details><summary>Requests Module</summary>
<p>

  ```python
r = requests.post('example.com')

```
</p>
</details>

<details><summary>My Module</summary>
<p>

  ```python
r = REQ().post('example.com')

```
</p>
</details>


# Headers :

<details><summary>Requests Module</summary>
<p>

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

<details><summary>My Module</summary>
<p>

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

# My Module Usage :

<details><summary>Add Proxy</summary>
<p>

  Add Proxy ```ip:port``` Format
  
  Example :
  
  ```python
  r = REQ().post('example.com', proxy = 'ip:port', proxy_type = 'socks4')

```
  and the proxy type : http, socks4, socks5
  
</p>
</details>

<details><summary>Add ssl</summary>
<p>

  
  ```python
r = REQ().post('example.com', verify = True)

```
  
  if you don't want to use ssl replace it with False
  
</p>
</details>

<details><summary>Add Timeout</summary>
<p>

  Default Timeout is 5 , but you can change it like this :
  
  ```python
r = REQ().post('example.com', timeout = 5)

```
 
  
</p>
</details>

<details><summary>Print Response</summary>
<p>

  To Print Response :
  
  ```python
r = REQ().post('example.com')
  print(r.text)

```
  
 
  
</p>
</details>

<details><summary>Print Status Code</summary>
<p>

  To Print Status Code :
  
  ```python
r = REQ().post('example.com')
  print(r.sc)

```

  
</p>
</details>

<details><summary>Full Usage</summary>
<p>

  
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
  print(r.sc)

```

  
</p>
</details>
