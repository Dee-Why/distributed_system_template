# coding:utf-8
import time
import grpc

import my_rpc.DemoAdvisor_pb2 as pb2
import my_rpc.DemoAdvisor_pb2_grpc as pb2_grpc
from concurrent import futures  # 这个库就是用来给grpc_server起线程用的


history_list = []


class DemoAdvisor(pb2_grpc.DemoAdvisorServicer):
    def update_observation(self, request, context):
        new_id = request.new_id  # follow the definition of update_observation_param
        new_name = request.new_name  # follow the definition of update_observation_param
        history_list.append((new_id, new_name))

        log_info = 'history_list = ['
        for item in history_list:
            log_info += '(' + str(item[0]) + ',' + str(item[1]) + '),'
        log_info += ']'

        return pb2.update_observation_reply(log_info=log_info)

    def get_suggestion(self, request, context):
        question_id = int(request.question_id)
        for item in history_list:
            if int(item[0]) == int(question_id):
                result = f'the suggestion for question:{question_id} is ' + str(item[1])
                return pb2.get_suggestion_reply(result=result)
        return pb2.get_suggestion_reply(result='not recorded in history')


def run():
    # 起一个server
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    # 在server上注册提供grpc服务的类
    pb2_grpc.add_DemoAdvisorServicer_to_server(DemoAdvisor(), grpc_server)
    # server打开一个服务端口，并运行
    grpc_server.add_insecure_port('127.0.0.1:8888')  # 使用5000端口
    print('server will start at 127.0.0.1:8888')
    grpc_server.start()
    print('usage 1:')
    print('python my_client.py update_observation <new_id:int> <new_name:str>  # update the observation history')
    print('usage 2:')
    print('python my_client.py get_suggestion <question_id:int>  # ask advice for question identified with question_id')
    try:  # python使用grpc需要用这个技巧防止服务闪退
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)  # 安全退出


if __name__ == '__main__':
    run()
