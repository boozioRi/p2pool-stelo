import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '7ab3c4d2'.decode('hex')
P2P_PORT = 12477
ADDRESS_VERSION = 63
SCRIPT_ADDRESS_VERSION = 20
RPC_PORT = 12478
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'steloaddress' in (yield dashd.rpc_help()) and
            not (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 120 # s
SYMBOL = 'STL'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'stelocore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/stelocore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.stelocore'), 'stelo.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://206.189.100.68:3001/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://206.189.100.68:3001/address/'
TX_EXPLORER_URL_PREFIX = 'http://206.189.100.68:3001/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
