# coding:utf-8
import sys, getopt
import grpc
import my_rpc.DemoAdvisor_pb2 as pb2
import my_rpc.DemoAdvisor_pb2_grpc as pb2_grpc


def run_update_observation(argv):
    # 选择端口，接入
    conn = grpc.insecure_channel('127.0.0.1:8888')  # the same port typed in my_service.py
    client = pb2_grpc.DemoAdvisorStub(channel=conn)
    # 执行远程过程调用， 其中参数要使用pb2.get_suggestion_param(id = xxx, name='xxx')的形式给
    response = client.update_observation(
        pb2.update_observation_param(
            new_id=int(argv[0]),
            new_name=str(argv[1])
        )
    )
    # 展示结果
    print(response.log_info)


def run_get_suggestion(argv):
    conn = grpc.insecure_channel('127.0.0.1:8888')  # the same port typed in my_service.py
    client = pb2_grpc.DemoAdvisorStub(channel=conn)
    # 执行远程过程调用， 其中参数要使用pb2.get_suggestion_param(id = xxx, name='xxx')的形式给
    response = client.get_suggestion(
        pb2.get_suggestion_param(
            question_id=int(argv[0])
        )
    )
    print(response.result)


if __name__ == '__main__':
    if sys.argv[1] == 'update_observation' or sys.argv[1] == 'u':
        run_update_observation(sys.argv[2:])
    elif sys.argv[1] == 'get_suggestion' or sys.argv[1] == 'g':
        run_get_suggestion(sys.argv[2:])


