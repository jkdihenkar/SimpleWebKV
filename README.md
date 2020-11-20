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

Description of the Contents of the Code files:

* `simplekv.py` : core KV store functionalities
* `simplekv_server.py` : flask kvstore service
* `simplekv_cli_client.py` : CLI that interacts with the flask store service
* `test_simplekv_server.py` : Tests for kvstore web service
* `test_simplekv.py` : Test for core kv store utils
