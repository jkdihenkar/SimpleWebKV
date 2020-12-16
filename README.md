# SimpleWebKV

A simple web KV Store in Flask with GET SET and WATCH

# Running the Project

**PRE-REQS**: Have docker installed on the system setup and working fine. This project uses makefile so ensure that make utils are installed. 

Also ensure that you have kustomize, skaffold and minikube installed locally.


```bash
git clone https://github.com/jkdihenkar/SimpleWebKV.git
cd SimpleWebKV
make kube_deploy
```

Check the deployment:

```

```

From another terminal - test the project is running fine.

```
$ curl -d '{"arg1":"val1"}' -XPUT http://localhost:5000/put/hello 
{"result":"success"}
```

### Testing the Watch Feature

Once the app is running - Open a new terminal and run - 
```
curl -N http://localhost:5000/watch
```

Now do some operations from another terminal window - 

```
curl -d '{"arg1":"val1"}' -XPUT http://localhost:5000/put/hello 
```

You will start seeing events of the "curl -N watch" terminal.

### Description of the Contents of the Code files

* `simplekv.py` : core KV store functionalities
* `simplekv_server.py` : flask kvstore service
* `simplekv_cli_client.py` : CLI that interacts with the flask store service
* `test_simplekv_server.py` : Tests for kvstore web service
* `test_simplekv.py` : Test for core kv store utils

## Simple CLI Client Usgaes

Connect to the running container with - 

```
docker exec -it f59dc4e /bin/bash
```

And test out the CLI - 

```

# PUT
$ python simplekv_cli_client.py put  hello 456
success

# GET
$ python simplekv_cli_client.py get hello
456

# WATCH
$ python simplekv_cli_client.py watch
PUT :: INIT STORE cli_store
PUT :: Set hello = 456 in cli_store
...
...

# Unsupported command
$ python simplekv_cli_client.py set hello 456
ERROR: Cannot find key: set
Usage: simplekv_cli_client.py <command>
  available commands:    get | put | watch

For detailed information on this command, run:
  simplekv_cli_client.py --help

```