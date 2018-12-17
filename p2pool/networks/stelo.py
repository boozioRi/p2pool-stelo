from p2pool.dash import networks

PARENT = networks.nets['stelo']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '1B018E126E58B46D'.decode('hex')
PREFIX = '1B018E101A4CD06E'.decode('hex')
COINBASEEXT = '2f7032706f6f6c2d7374656c6f2f'.decode('hex')
P2P_PORT = 2981
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 2982
BOOTSTRAP_ADDRS = '91.226.82.94 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-stl'
VERSION_CHECK = lambda v: v >= 120204
