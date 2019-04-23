# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc

from crons.server import planserver_pb2_grpc, planserver_pb2


class greeter_client:
    __port = '8888'
    __grpcStub = None    # 存根
    def __init__(self,host,port=None):
        if(port):
            self.__port = port
        channel = grpc.insecure_channel(host+':'+self.__port)   #建立连接通道
        self.__grpcStub = planserver_pb2_grpc.PlanStub(channel)
        pass
    def setPlan(self,cronsId,times,command):
        response = self.__grpcStub.set(planserver_pb2.PlanRequest(cronsId=cronsId, times=times, command=command))
        print("Greeter client received:"+response.message)
        return response

    def updatePlan(self, cronsId, times, command):
        response = self.__grpcStub.update(planserver_pb2.PlanRequest(cronsId=cronsId, times=times, command=command))
        print("Greeter client received:" + response.message)
        return response

    def deletePlan(self, cronsId):
        response = self.__grpcStub.delete(planserver_pb2.PlanRequest(cronsId=cronsId))
        print("Greeter client received:" + response.message)
        return response

    def readPlan(self):
        response = self.__grpcStub.read(planserver_pb2.PlanRequest(cronsId='-1'))
        print("Greeter client received:" + response.message)
        # result = {"code": response.code, "msg": response.message}
        return response

# if __name__ == '__main__':
#     logging.basicConfig()
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # with grpc.insecure_channel('localhost:8888') as channel:
    #     stub = planserver_pb2_grpc.PlanStub(channel)
        # planrequest = planserver_pb2.PlanRequest(cronsId='walkingsun', times="2 * * * *", command="ls")
        # planrequest = planserver_pb2.PlanRequest(cronsId='walkingsun')
        # response = stub.set(planrequest)
        # response = stub.update(planrequest)
        # response = stub.delete(planrequest)
        # response = stub.read(planrequest)
        # print("Greeter client received: " + response.code + response.message)
