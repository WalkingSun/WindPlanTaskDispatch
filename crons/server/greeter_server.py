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
"""The Python implementation of the GRPC helloworld.Greeter server."""

import logging
import time
from concurrent import futures

import grpc
from planServer import planServer

from crons.server import planserver_pb2_grpc, planserver_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '127.0.0.1'
_PORT = '8888'

class Greeter(planserver_pb2_grpc.PlanServicer):

    def set(self, request, context):
        cronsId = request.cronsId
        times = request.times
        command = request.command
        plansever = planServer()
        plansever.setCrons(cronsId, times, command)
        return planserver_pb2.PlanReply(code="200", message='计划任务设置成功')
    def update(self, request, context):
        cronsId = request.cronsId
        times = request.times
        command = request.command
        plansever = planServer()
        plansever.updateCrons(cronsId, times, command)
        return planserver_pb2.PlanReply(code="200", message='计划任务设置成功')

    def delete(self, request, context):
        cronsId = request.cronsId
        plansever = planServer()
        plansever. delCrons(cronsId)
        return planserver_pb2.PlanReply(code="200", message='计划任务删除成功')

    def read(self, request, context):
        planserver = planServer()
        msg = planserver.readCrons()
        return planserver_pb2.PlanReply(code="200", message=msg)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    planserver_pb2_grpc.add_PlanServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:'+_PORT)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
