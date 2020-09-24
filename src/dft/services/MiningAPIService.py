# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from grpc import StatusCode

from pydftlib.pydftlib import bin2hstr

from dft.core import config
from dft.core.dftnode import dftNode
from dft.crypto.Qryptonight import Qryptonight
from dft.generated import dftmining_pb2
from dft.generated.dftmining_pb2_grpc import MiningAPIServicer
from dft.services.grpcHelper import GrpcExceptionWrapper


class MiningAPIService(MiningAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, dftnode: dftNode):
        self.dftnode = dftnode
        self._qn = Qryptonight()

    @GrpcExceptionWrapper(dftmining_pb2.GetBlockMiningCompatibleResp, StatusCode.UNKNOWN)
    def GetBlockMiningCompatible(self,
                                 request: dftmining_pb2.GetBlockMiningCompatibleReq,
                                 context) -> dftmining_pb2.GetBlockMiningCompatibleResp:

        blockheader, block_metadata = self.dftnode.get_blockheader_and_metadata(request.height)

        response = dftmining_pb2.GetBlockMiningCompatibleResp()
        if blockheader is not None and block_metadata is not None:
            response = dftmining_pb2.GetBlockMiningCompatibleResp(
                blockheader=blockheader.pbdata,
                blockmetadata=block_metadata.pbdata)

        return response

    @GrpcExceptionWrapper(dftmining_pb2.GetLastBlockHeaderResp, StatusCode.UNKNOWN)
    def GetLastBlockHeader(self,
                           request: dftmining_pb2.GetLastBlockHeaderReq,
                           context) -> dftmining_pb2.GetLastBlockHeaderResp:
        response = dftmining_pb2.GetLastBlockHeaderResp()

        blockheader, block_metadata = self.dftnode.get_blockheader_and_metadata(request.height)

        response.difficulty = int(bin2hstr(block_metadata.block_difficulty), 16)
        response.height = blockheader.block_number
        response.timestamp = blockheader.timestamp
        response.reward = blockheader.block_reward + blockheader.fee_reward
        response.hash = bin2hstr(blockheader.headerhash)
        response.depth = self.dftnode.block_height - blockheader.block_number

        return response

    @GrpcExceptionWrapper(dftmining_pb2.GetBlockToMineResp, StatusCode.UNKNOWN)
    def GetBlockToMine(self,
                       request: dftmining_pb2.GetBlockToMineReq,
                       context) -> dftmining_pb2.GetBlockToMineResp:

        response = dftmining_pb2.GetBlockToMineResp()

        blocktemplate_blob_and_difficulty = self.dftnode.get_block_to_mine(request.wallet_address)

        if blocktemplate_blob_and_difficulty:
            response.blocktemplate_blob = blocktemplate_blob_and_difficulty[0]
            response.difficulty = blocktemplate_blob_and_difficulty[1]
            response.height = self.dftnode.block_height + 1
            response.reserved_offset = config.dev.extra_nonce_offset
            seed_block_number = self._qn.get_seed_height(response.height)
            response.seed_hash = bin2hstr(self.dftnode.get_block_header_hash_by_number(seed_block_number))

        return response

    @GrpcExceptionWrapper(dftmining_pb2.GetBlockToMineResp, StatusCode.UNKNOWN)
    def SubmitMinedBlock(self,
                         request: dftmining_pb2.SubmitMinedBlockReq,
                         context) -> dftmining_pb2.SubmitMinedBlockResp:
        response = dftmining_pb2.SubmitMinedBlockResp()

        response.error = not self.dftnode.submit_mined_block(request.blob)

        return response
