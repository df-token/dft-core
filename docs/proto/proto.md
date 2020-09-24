# Protocol Documentation
<a name="top"/>

## Table of Contents

- [dft.proto](#dft.proto)
    - [AddressList](#dft.AddressList)
    - [AddressState](#dft.AddressState)
    - [Block](#dft.Block)
    - [BlockExtended](#dft.BlockExtended)
    - [BlockHeader](#dft.BlockHeader)
    - [BlockHeaderExtended](#dft.BlockHeaderExtended)
    - [BlockMetaData](#dft.BlockMetaData)
    - [BlockMetaDataList](#dft.BlockMetaDataList)
    - [EphemeralMessage](#dft.EphemeralMessage)
    - [GenesisBalance](#dft.GenesisBalance)
    - [GetAddressStateReq](#dft.GetAddressStateReq)
    - [GetAddressStateResp](#dft.GetAddressStateResp)
    - [GetBlockReq](#dft.GetBlockReq)
    - [GetBlockResp](#dft.GetBlockResp)
    - [GetKnownPeersReq](#dft.GetKnownPeersReq)
    - [GetKnownPeersResp](#dft.GetKnownPeersResp)
    - [GetLatestDataReq](#dft.GetLatestDataReq)
    - [GetLatestDataResp](#dft.GetLatestDataResp)
    - [GetLocalAddressesReq](#dft.GetLocalAddressesReq)
    - [GetLocalAddressesResp](#dft.GetLocalAddressesResp)
    - [GetNodeStateReq](#dft.GetNodeStateReq)
    - [GetNodeStateResp](#dft.GetNodeStateResp)
    - [GetObjectReq](#dft.GetObjectReq)
    - [GetObjectResp](#dft.GetObjectResp)
    - [GetStakersReq](#dft.GetStakersReq)
    - [GetStakersResp](#dft.GetStakersResp)
    - [GetStatsReq](#dft.GetStatsReq)
    - [GetStatsResp](#dft.GetStatsResp)
    - [GetWalletReq](#dft.GetWalletReq)
    - [GetWalletResp](#dft.GetWalletResp)
    - [LatticePublicKeyTxnReq](#dft.LatticePublicKeyTxnReq)
    - [MR](#dft.MR)
    - [MsgObject](#dft.MsgObject)
    - [NodeInfo](#dft.NodeInfo)
    - [Peer](#dft.Peer)
    - [PingReq](#dft.PingReq)
    - [PongResp](#dft.PongResp)
    - [PushTransactionReq](#dft.PushTransactionReq)
    - [PushTransactionResp](#dft.PushTransactionResp)
    - [StakeValidator](#dft.StakeValidator)
    - [StakeValidatorsList](#dft.StakeValidatorsList)
    - [StakeValidatorsTracker](#dft.StakeValidatorsTracker)
    - [StakeValidatorsTracker.ExpiryEntry](#dft.StakeValidatorsTracker.ExpiryEntry)
    - [StakeValidatorsTracker.FutureStakeAddressesEntry](#dft.StakeValidatorsTracker.FutureStakeAddressesEntry)
    - [StakeValidatorsTracker.FutureSvDictEntry](#dft.StakeValidatorsTracker.FutureSvDictEntry)
    - [StakeValidatorsTracker.SvDictEntry](#dft.StakeValidatorsTracker.SvDictEntry)
    - [StakerData](#dft.StakerData)
    - [StoredPeers](#dft.StoredPeers)
    - [Timestamp](#dft.Timestamp)
    - [Transaction](#dft.Transaction)
    - [Transaction.CoinBase](#dft.Transaction.CoinBase)
    - [Transaction.Destake](#dft.Transaction.Destake)
    - [Transaction.Duplicate](#dft.Transaction.Duplicate)
    - [Transaction.LatticePublicKey](#dft.Transaction.LatticePublicKey)
    - [Transaction.Stake](#dft.Transaction.Stake)
    - [Transaction.Transfer](#dft.Transaction.Transfer)
    - [Transaction.Vote](#dft.Transaction.Vote)
    - [TransactionCount](#dft.TransactionCount)
    - [TransactionCount.CountEntry](#dft.TransactionCount.CountEntry)
    - [TransactionExtended](#dft.TransactionExtended)
    - [TransferCoinsReq](#dft.TransferCoinsReq)
    - [TransferCoinsResp](#dft.TransferCoinsResp)
    - [Wallet](#dft.Wallet)
    - [WalletStore](#dft.WalletStore)

    - [GetLatestDataReq.Filter](#dft.GetLatestDataReq.Filter)
    - [GetStakersReq.Filter](#dft.GetStakersReq.Filter)
    - [NodeInfo.State](#dft.NodeInfo.State)
    - [Transaction.Type](#dft.Transaction.Type)


    - [AdminAPI](#dft.AdminAPI)
    - [P2PAPI](#dft.P2PAPI)
    - [PublicAPI](#dft.PublicAPI)


- [dftbase.proto](#dftbase.proto)
    - [GetNodeInfoReq](#dft.GetNodeInfoReq)
    - [GetNodeInfoResp](#dft.GetNodeInfoResp)



    - [Base](#dft.Base)


- [dftlegacy.proto](#dftlegacy.proto)
    - [BKData](#dft.BKData)
    - [FBData](#dft.FBData)
    - [LegacyMessage](#dft.LegacyMessage)
    - [MRData](#dft.MRData)
    - [NoData](#dft.NoData)
    - [PBData](#dft.PBData)
    - [PLData](#dft.PLData)
    - [PONGData](#dft.PONGData)
    - [SYNCData](#dft.SYNCData)
    - [VEData](#dft.VEData)

    - [LegacyMessage.FuncName](#dft.LegacyMessage.FuncName)




- [Scalar Value Types](#scalar-value-types)



<a name="dft.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dft.proto



<a name="dft.AddressList"/>

### AddressList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="dft.AddressState"/>

### AddressState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  | FIXME: Discuss. 32 or 64 bits? |
| pubhashes | [bytes](#bytes) | repeated |  |
| transaction_hashes | [bytes](#bytes) | repeated |  |






<a name="dft.Block"/>

### Block



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#dft.BlockHeader) |  |  |
| transactions | [Transaction](#dft.Transaction) | repeated |  |
| dup_transactions | [Transaction](#dft.Transaction) | repeated | TODO: Review this |
| vote | [Transaction](#dft.Transaction) | repeated |  |
| genesis_balance | [GenesisBalance](#dft.GenesisBalance) | repeated | This is only applicable to genesis blocks |






<a name="dft.BlockExtended"/>

### BlockExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block | [Block](#dft.Block) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="dft.BlockHeader"/>

### BlockHeader



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  | Header |
| epoch | [uint64](#uint64) |  |  |
| timestamp | [Timestamp](#dft.Timestamp) |  | FIXME: Temporary |
| hash_header | [bytes](#bytes) |  |  |
| hash_header_prev | [bytes](#bytes) |  |  |
| reward_block | [uint64](#uint64) |  |  |
| reward_fee | [uint64](#uint64) |  |  |
| merkle_root | [bytes](#bytes) |  |  |
| hash_reveal | [bytes](#bytes) |  |  |
| stake_selector | [bytes](#bytes) |  |  |






<a name="dft.BlockHeaderExtended"/>

### BlockHeaderExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#dft.BlockHeader) |  |  |
| transaction_count | [TransactionCount](#dft.TransactionCount) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="dft.BlockMetaData"/>

### BlockMetaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="dft.BlockMetaDataList"/>

### BlockMetaDataList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number_hashes | [BlockMetaData](#dft.BlockMetaData) | repeated |  |






<a name="dft.EphemeralMessage"/>

### EphemeralMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [bytes](#bytes) |  |  |
| ttl | [uint64](#uint64) |  |  |
| data | [bytes](#bytes) |  | Encrypted String containing aes256_symkey, prf512_seed, xmss_address, signature |






<a name="dft.EphemeralMessage.Data"/>

### EphemeralMessage.Data



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| aes256_symkey | [bytes](#bytes) |  |  |
| prf512_seed | [bytes](#bytes) |  |  |
| xmss_address | [bytes](#bytes) |  |  |
| xmss_signature | [bytes](#bytes) |  |  |






<a name="dft.GenesisBalance"/>

### GenesisBalance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | Address is string only here to increase visibility |
| balance | [uint64](#uint64) |  |  |






<a name="dft.GetAddressStateReq"/>

### GetAddressStateReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="dft.GetAddressStateResp"/>

### GetAddressStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [AddressState](#dft.AddressState) |  |  |






<a name="dft.GetBlockReq"/>

### GetBlockReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  | Indicates the index number in mainchain |
| after_hash | [bytes](#bytes) |  | request the node that comes after hash |






<a name="dft.GetBlockResp"/>

### GetBlockResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#dft.NodeInfo) |  |  |
| block | [Block](#dft.Block) |  |  |






<a name="dft.GetKnownPeersReq"/>

### GetKnownPeersReq







<a name="dft.GetKnownPeersResp"/>

### GetKnownPeersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#dft.NodeInfo) |  |  |
| known_peers | [Peer](#dft.Peer) | repeated |  |






<a name="dft.GetLatestDataReq"/>

### GetLatestDataReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetLatestDataReq.Filter](#dft.GetLatestDataReq.Filter) |  |  |
| offset | [uint32](#uint32) |  | Offset in the result list (works backwards in this case) |
| quantity | [uint32](#uint32) |  | Number of items to retrive. Capped at 100 |






<a name="dft.GetLatestDataResp"/>

### GetLatestDataResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| blockheaders | [BlockHeaderExtended](#dft.BlockHeaderExtended) | repeated |  |
| transactions | [TransactionExtended](#dft.TransactionExtended) | repeated |  |
| transactions_unconfirmed | [TransactionExtended](#dft.TransactionExtended) | repeated |  |






<a name="dft.GetLocalAddressesReq"/>

### GetLocalAddressesReq







<a name="dft.GetLocalAddressesResp"/>

### GetLocalAddressesResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="dft.GetNodeStateReq"/>

### GetNodeStateReq







<a name="dft.GetNodeStateResp"/>

### GetNodeStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [NodeInfo](#dft.NodeInfo) |  |  |






<a name="dft.GetObjectReq"/>

### GetObjectReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [bytes](#bytes) |  |  |






<a name="dft.GetObjectResp"/>

### GetObjectResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| found | [bool](#bool) |  |  |
| address_state | [AddressState](#dft.AddressState) |  |  |
| transaction | [TransactionExtended](#dft.TransactionExtended) |  |  |
| block | [Block](#dft.Block) |  |  |






<a name="dft.GetStakersReq"/>

### GetStakersReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetStakersReq.Filter](#dft.GetStakersReq.Filter) |  | Indicates which group of stakers (current / next) |
| offset | [uint32](#uint32) |  | Offset in the staker list |
| quantity | [uint32](#uint32) |  | Number of stakers to retrive. Capped at 100 |






<a name="dft.GetStakersResp"/>

### GetStakersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stakers | [StakerData](#dft.StakerData) | repeated |  |






<a name="dft.GetStatsReq"/>

### GetStatsReq







<a name="dft.GetStatsResp"/>

### GetStatsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#dft.NodeInfo) |  |  |
| epoch | [uint64](#uint64) |  | Current epoch |
| uptime_network | [uint64](#uint64) |  | Indicates uptime in seconds |
| stakers_count | [uint64](#uint64) |  | Number of active stakers |
| block_last_reward | [uint64](#uint64) |  |  |
| block_time_mean | [uint64](#uint64) |  |  |
| block_time_sd | [uint64](#uint64) |  |  |
| coins_total_supply | [uint64](#uint64) |  |  |
| coins_emitted | [uint64](#uint64) |  |  |
| coins_atstake | [uint64](#uint64) |  |  |






<a name="dft.GetWalletReq"/>

### GetWalletReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="dft.GetWalletResp"/>

### GetWalletResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallet | [Wallet](#dft.Wallet) |  | FIXME: Encrypt |






<a name="dft.LatticePublicKeyTxnReq"/>

### LatticePublicKeyTxnReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  |  |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |
| xmss_pk | [bytes](#bytes) |  |  |
| xmss_ots_index | [uint64](#uint64) |  |  |






<a name="dft.MR"/>

### MR
FIXME: This is legacy. Plan removal


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [string](#string) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="dft.MsgObject"/>

### MsgObject



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ephemeral | [EphemeralMessage](#dft.EphemeralMessage) |  | Overlapping - objects used for 2-way exchanges P2PRequest request = 1; P2PResponse response = 2; |






<a name="dft.NodeInfo"/>

### NodeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| state | [NodeInfo.State](#dft.NodeInfo.State) |  |  |
| num_connections | [uint32](#uint32) |  |  |
| num_known_peers | [uint32](#uint32) |  |  |
| uptime | [uint64](#uint64) |  | Uptime in seconds |
| block_height | [uint64](#uint64) |  |  |
| block_last_hash | [bytes](#bytes) |  |  |
| stake_enabled | [bool](#bool) |  |  |
| network_id | [string](#string) |  |  |






<a name="dft.Peer"/>

### Peer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ip | [string](#string) |  |  |






<a name="dft.PingReq"/>

### PingReq







<a name="dft.PongResp"/>

### PongResp







<a name="dft.PushTransactionReq"/>

### PushTransactionReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_signed | [Transaction](#dft.Transaction) |  |  |






<a name="dft.PushTransactionResp"/>

### PushTransactionResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| some_response | [string](#string) |  |  |






<a name="dft.StakeValidator"/>

### StakeValidator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| slave_public_key | [bytes](#bytes) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| activation_blocknumber | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  |  |
| is_banned | [bool](#bool) |  |  |
| is_active | [bool](#bool) |  |  |






<a name="dft.StakeValidatorsList"/>

### StakeValidatorsList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stake_validators | [StakeValidator](#dft.StakeValidator) | repeated |  |






<a name="dft.StakeValidatorsTracker"/>

### StakeValidatorsTracker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sv_dict | [StakeValidatorsTracker.SvDictEntry](#dft.StakeValidatorsTracker.SvDictEntry) | repeated |  |
| future_stake_addresses | [StakeValidatorsTracker.FutureStakeAddressesEntry](#dft.StakeValidatorsTracker.FutureStakeAddressesEntry) | repeated |  |
| expiry | [StakeValidatorsTracker.ExpiryEntry](#dft.StakeValidatorsTracker.ExpiryEntry) | repeated |  |
| future_sv_dict | [StakeValidatorsTracker.FutureSvDictEntry](#dft.StakeValidatorsTracker.FutureSvDictEntry) | repeated |  |
| total_stake_amount | [uint64](#uint64) |  |  |






<a name="dft.StakeValidatorsTracker.ExpiryEntry"/>

### StakeValidatorsTracker.ExpiryEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [AddressList](#dft.AddressList) |  |  |






<a name="dft.StakeValidatorsTracker.FutureStakeAddressesEntry"/>

### StakeValidatorsTracker.FutureStakeAddressesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#dft.StakeValidator) |  |  |






<a name="dft.StakeValidatorsTracker.FutureSvDictEntry"/>

### StakeValidatorsTracker.FutureSvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [StakeValidatorsList](#dft.StakeValidatorsList) |  |  |






<a name="dft.StakeValidatorsTracker.SvDictEntry"/>

### StakeValidatorsTracker.SvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#dft.StakeValidator) |  |  |






<a name="dft.StakerData"/>

### StakerData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_state | [AddressState](#dft.AddressState) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |






<a name="dft.StoredPeers"/>

### StoredPeers



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peers | [Peer](#dft.Peer) | repeated |  |






<a name="dft.Timestamp"/>

### Timestamp
TODO: Avoid using timestamp until the github issue is fixed
import &#34;google/protobuf/timestamp.proto&#34;;


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seconds | [int64](#int64) |  |  |
| nanos | [int32](#int32) |  |  |






<a name="dft.Transaction"/>

### Transaction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Transaction.Type](#dft.Transaction.Type) |  |  |
| nonce | [uint64](#uint64) |  |  |
| addr_from | [bytes](#bytes) |  |  |
| public_key | [bytes](#bytes) |  |  |
| transaction_hash | [bytes](#bytes) |  |  |
| ots_key | [uint32](#uint32) |  |  |
| signature | [bytes](#bytes) |  |  |
| transfer | [Transaction.Transfer](#dft.Transaction.Transfer) |  |  |
| stake | [Transaction.Stake](#dft.Transaction.Stake) |  |  |
| coinbase | [Transaction.CoinBase](#dft.Transaction.CoinBase) |  |  |
| latticePK | [Transaction.LatticePublicKey](#dft.Transaction.LatticePublicKey) |  |  |
| duplicate | [Transaction.Duplicate](#dft.Transaction.Duplicate) |  |  |
| vote | [Transaction.Vote](#dft.Transaction.Vote) |  |  |






<a name="dft.Transaction.CoinBase"/>

### Transaction.CoinBase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |






<a name="dft.Transaction.Destake"/>

### Transaction.Destake







<a name="dft.Transaction.Duplicate"/>

### Transaction.Duplicate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| prev_header_hash | [uint64](#uint64) |  |  |
| coinbase1_hhash | [bytes](#bytes) |  |  |
| coinbase2_hhash | [bytes](#bytes) |  |  |
| coinbase1 | [Transaction](#dft.Transaction) |  |  |
| coinbase2 | [Transaction](#dft.Transaction) |  |  |






<a name="dft.Transaction.LatticePublicKey"/>

### Transaction.LatticePublicKey



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |






<a name="dft.Transaction.Stake"/>

### Transaction.Stake



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activation_blocknumber | [uint64](#uint64) |  |  |
| slavePK | [bytes](#bytes) |  |  |
| hash | [bytes](#bytes) |  |  |






<a name="dft.Transaction.Transfer"/>

### Transaction.Transfer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |
| fee | [uint64](#uint64) |  |  |






<a name="dft.Transaction.Vote"/>

### Transaction.Vote



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="dft.TransactionCount"/>

### TransactionCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [TransactionCount.CountEntry](#dft.TransactionCount.CountEntry) | repeated |  |






<a name="dft.TransactionCount.CountEntry"/>

### TransactionCount.CountEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="dft.TransactionExtended"/>

### TransactionExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#dft.BlockHeader) |  |  |
| tx | [Transaction](#dft.Transaction) |  |  |






<a name="dft.TransferCoinsReq"/>

### TransferCoinsReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  | Transaction source address |
| address_to | [bytes](#bytes) |  | Transaction destination address |
| amount | [uint64](#uint64) |  | Amount. It should be expressed in Shor |
| fee | [uint64](#uint64) |  | Fee. It should be expressed in Shor |
| xmss_pk | [bytes](#bytes) |  | XMSS Public key |
| xmss_ots_index | [uint64](#uint64) |  | XMSS One time signature index |






<a name="dft.TransferCoinsResp"/>

### TransferCoinsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_unsigned | [Transaction](#dft.Transaction) |  |  |






<a name="dft.Wallet"/>

### Wallet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | FIXME move to bytes |
| mnemonic | [string](#string) |  |  |
| xmss_index | [int32](#int32) |  |  |






<a name="dft.WalletStore"/>

### WalletStore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallets | [Wallet](#dft.Wallet) | repeated |  |








<a name="dft.GetLatestDataReq.Filter"/>

### GetLatestDataReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALL | 0 |  |
| BLOCKHEADERS | 1 |  |
| TRANSACTIONS | 2 |  |
| TRANSACTIONS_UNCONFIRMED | 3 |  |



<a name="dft.GetStakersReq.Filter"/>

### GetStakersReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| CURRENT | 0 |  |
| NEXT | 1 |  |



<a name="dft.NodeInfo.State"/>

### NodeInfo.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| UNSYNCED | 1 |  |
| SYNCING | 2 |  |
| SYNCED | 3 |  |
| FORKED | 4 |  |



<a name="dft.Transaction.Type"/>

### Transaction.Type


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| TRANSFER | 1 |  |
| STAKE | 2 |  |
| DESTAKE | 3 |  |
| COINBASE | 4 |  |
| LATTICE | 5 |  |
| DUPLICATE | 6 |  |
| VOTE | 7 |  |







<a name="dft.AdminAPI"/>

### AdminAPI
This is a place holder for testing/instrumentation APIs

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLocalAddresses | [GetLocalAddressesReq](#dft.GetLocalAddressesReq) | [GetLocalAddressesResp](#dft.GetLocalAddressesReq) | FIXME: Use TLS and some signature scheme to validate the cli? At the moment, it will run locally |


<a name="dft.P2PAPI"/>

### P2PAPI
This service describes the P2P API

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#dft.GetNodeStateReq) | [GetNodeStateResp](#dft.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#dft.GetKnownPeersReq) | [GetKnownPeersResp](#dft.GetKnownPeersReq) |  |
| GetBlock | [GetBlockReq](#dft.GetBlockReq) | [GetBlockResp](#dft.GetBlockReq) | rpc PublishBlock(PublishBlockReq) returns (PublishBlockResp); |
| ObjectExchange | [MsgObject](#dft.MsgObject) | [MsgObject](#dft.MsgObject) | A bidirectional streaming channel is used to avoid any firewalling/NAT issues. |


<a name="dft.PublicAPI"/>

### PublicAPI
This service describes the Public API used by clients (wallet/cli/etc)

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#dft.GetNodeStateReq) | [GetNodeStateResp](#dft.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#dft.GetKnownPeersReq) | [GetKnownPeersResp](#dft.GetKnownPeersReq) |  |
| GetStats | [GetStatsReq](#dft.GetStatsReq) | [GetStatsResp](#dft.GetStatsReq) |  |
| GetAddressState | [GetAddressStateReq](#dft.GetAddressStateReq) | [GetAddressStateResp](#dft.GetAddressStateReq) |  |
| GetObject | [GetObjectReq](#dft.GetObjectReq) | [GetObjectResp](#dft.GetObjectReq) |  |
| GetLatestData | [GetLatestDataReq](#dft.GetLatestDataReq) | [GetLatestDataResp](#dft.GetLatestDataReq) |  |
| GetStakers | [GetStakersReq](#dft.GetStakersReq) | [GetStakersResp](#dft.GetStakersReq) |  |
| TransferCoins | [TransferCoinsReq](#dft.TransferCoinsReq) | [TransferCoinsResp](#dft.TransferCoinsReq) |  |
| PushTransaction | [PushTransactionReq](#dft.PushTransactionReq) | [PushTransactionResp](#dft.PushTransactionReq) |  |
| GetLatticePublicKeyTxn | [LatticePublicKeyTxnReq](#dft.LatticePublicKeyTxnReq) | [TransferCoinsResp](#dft.LatticePublicKeyTxnReq) |  |





<a name="dftbase.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dftbase.proto



<a name="dft.GetNodeInfoReq"/>

### GetNodeInfoReq







<a name="dft.GetNodeInfoResp"/>

### GetNodeInfoResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| grpcProto | [string](#string) |  |  |












<a name="dft.Base"/>

### Base


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeInfo | [GetNodeInfoReq](#dft.GetNodeInfoReq) | [GetNodeInfoResp](#dft.GetNodeInfoReq) |  |





<a name="dftlegacy.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dftlegacy.proto



<a name="dft.BKData"/>

### BKData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mrData | [MRData](#dft.MRData) |  |  |
| block | [Block](#dft.Block) |  |  |






<a name="dft.FBData"/>

### FBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |






<a name="dft.LegacyMessage"/>

### LegacyMessage
Adding old code to refactor while keeping things working


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| func_name | [LegacyMessage.FuncName](#dft.LegacyMessage.FuncName) |  |  |
| noData | [NoData](#dft.NoData) |  |  |
| veData | [VEData](#dft.VEData) |  |  |
| pongData | [PONGData](#dft.PONGData) |  |  |
| mrData | [MRData](#dft.MRData) |  |  |
| sfmData | [MRData](#dft.MRData) |  |  |
| bkData | [BKData](#dft.BKData) |  |  |
| fbData | [FBData](#dft.FBData) |  |  |
| pbData | [PBData](#dft.PBData) |  |  |
| pbbData | [PBData](#dft.PBData) |  |  |
| syncData | [SYNCData](#dft.SYNCData) |  |  |






<a name="dft.MRData"/>

### MRData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [LegacyMessage.FuncName](#dft.LegacyMessage.FuncName) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="dft.NoData"/>

### NoData







<a name="dft.PBData"/>

### PBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |
| block | [Block](#dft.Block) |  |  |






<a name="dft.PLData"/>

### PLData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peer_ips | [string](#string) | repeated |  |






<a name="dft.PONGData"/>

### PONGData







<a name="dft.SYNCData"/>

### SYNCData







<a name="dft.VEData"/>

### VEData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| genesis_prev_hash | [bytes](#bytes) |  |  |








<a name="dft.LegacyMessage.FuncName"/>

### LegacyMessage.FuncName


| Name | Number | Description |
| ---- | ------ | ----------- |
| VE | 0 | Version |
| PL | 1 | Peers List |
| PONG | 2 | Pong |
| MR | 3 | Message received |
| SFM | 4 | Send Full Message |
| BK | 5 | Block |
| FB | 6 | Fetch request for block |
| PB | 7 | Push Block |
| PBB | 8 | Push Block Buffer |
| ST | 9 | Stake Transaction |
| DST | 10 | Destake Transaction |
| DT | 11 | Duplicate Transaction |
| TX | 12 | Transfer Transaction |
| VT | 13 | Vote |
| SYNC | 14 | Add into synced list, if the node replies |










## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double" /> double |  | double | double | float |
| <a name="float" /> float |  | float | float | float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool" /> bool |  | bool | boolean | boolean |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |

