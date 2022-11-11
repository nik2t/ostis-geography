from common import ScModule, ScKeynodes, ScPythonEventType
from DistanceAgent import DistanceAgent

from sc import *


class DistanceModule(ScModule):

    def __init__(self):
        ScModule.__init__(
            self,
            ctx=__ctx__,
            cpp_bridge=__cpp_bridge__,
            keynodes=[],
        )
        self.keynodes = ScKeynodes(self.ctx)

    def OnInitialize(self, params):
        print('Initialize Distance module')
        question_initiated = self.keynodes['question_initiated']

        agent = DistanceAgent(self)
        agent.Register(question_initiated, ScPythonEventType.AddOutputEdge)

    def OnShutdown(self):
        print('Shutting down Distance module')


service = DistanceModule()
service.Run()
