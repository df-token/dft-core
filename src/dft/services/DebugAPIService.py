# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from dft.core import config
from dft.core.dftnode import dftNode
from dft.generated import dftdebug_pb2
from dft.generated.dftdebug_pb2_grpc import DebugAPIServicer
from dft.services.grpcHelper import GrpcExceptionWrapper


class DebugAPIService(DebugAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, dftnode: dftNode):
        self.dftnode = dftnode

    @GrpcExceptionWrapper(dftdebug_pb2.GetFullStateResp)
    def GetFullState(self, request: dftdebug_pb2.GetFullStateReq, context) -> dftdebug_pb2.GetFullStateResp:
        return dftdebug_pb2.GetFullStateResp(
            coinbase_state=self.dftnode.get_address_state(config.dev.coinbase_address).pbdata,
            addresses_state=self.dftnode.get_all_address_state()
        )
