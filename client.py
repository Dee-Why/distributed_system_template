# coding:utf-8
import sys, getopt
import grpc
import g_rpc.demo_pb2 as pb2
import g_rpc.demo_pb2_grpc as pb2_grpc


def run(argv):
    # 选择端口，接入
    conn = grpc.insecure_channel('127.0.0.1:5000')  # the same port typed in service.py
    client = pb2_grpc.bo_advisorStub(channel=conn)
    # 执行远程过程调用， 其中参数要使用pb2.get_suggestion_param(id = xxx, name='xxx')的形式给
    response = client.get_suggestion(
        pb2.get_suggestion_param(
            id=int(argv[0]),
            name=str(argv[1])
        )
    )
    # 展示结果
    print(response.result)


if __name__ == '__main__':
    run(sys.argv[1:])
