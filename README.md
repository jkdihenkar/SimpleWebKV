# SimpleWebKV

A simple web KV Store in Flask with GET SET and WATCH

# Running the Project

**PRE-REQS**: Have docker installed on the system setup and working fine.


```bash
git clone https://github.com/jkdihenkar/SimpleWebKV.git
cd SimpleWebKV
docker build -t simplekv .
docker run -d -p 127.0.0.1:5000:5000 simplekv
docker logs -f <container-id>
```

From another terminal - test the project is running fine.

```
$ curl -d '{"arg1":"val1"}' -XPUT http://localhost:5000/put/hello 
{"result":"success"}
```
