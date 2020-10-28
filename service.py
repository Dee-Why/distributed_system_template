# coding:utf-8
import time
import grpc

import g_rpc.demo_pb2 as pb2
import g_rpc.demo_pb2_grpc as pb2_grpc
from concurrent import futures  # 这个库就是用来给grpc_server起线程用的


history_list = []


class bo_advisor(pb2_grpc.bo_advisorServicer):
    def get_suggestion(self, request, context):
        id = request.id
        name = request.name
        history_list.append((id, name))

        result = 'history_list = ['
        for item in history_list:
            result += '(' + str(item[0]) + ',' + str(item[1]) + '),'
        result += ']'
        return pb2.get_suggestion_reply(result=result)


def run():
    # 起一个server
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    # 在server上注册grpc服务
    pb2_grpc.add_bo_advisorServicer_to_server(bo_advisor(), grpc_server)
    # server打开一个服务端口，并运行
    grpc_server.add_insecure_port('127.0.0.1:5000')  # 使用5000端口
    print('server will start at 127.0.0.1:5000')
    grpc_server.start()

    try:  # python使用grpc需要用这个技巧防止服务闪退
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)  # 安全退出


if __name__ == '__main__':
    run()
