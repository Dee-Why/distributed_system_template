# learning grpc
make a demo
* server: get_suggestion(id) return a tuple (id, number);
* server: update_observation()  maintain a list in the server.
---
## first - create protobuf
define the data structure that will be delivered between client and server
1. init a new package and write a proper `.proto` file
2. use the following command in that package folder
```shell script
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. <xxx.proto>
```
where <xxx.proto> should be replaced by your `.proto` file name created in step1.

## second - creat my_server.py and my_client.py
the name of these two files are arbitrary, you can change the name;
we are going to use one of them as 'server' while the other as 'client'