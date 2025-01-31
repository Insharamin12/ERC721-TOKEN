# pragma version 0.4.0

"""
@license MIT
@title Puppy NFT
"""

from snekmate.tokens import erc721
from snekmate.auth import ownable as ow

initializes: ow
initializes: erc721[ownable := ow]

exports: erc721.__interface__

# ------------------------------------------------------------------
#                         STATE VERIABLES
# ------------------------------------------------------------------
NAME: constant(String[25]) = "Puppy NFT"
SYMBOL: constant(String[5]) = "PNFT"
BASE_URI: public(constant(String[35])) = " https://gateway.pinata.cloud/ipfs/"
EIP_712_VERSION: constant(String[1]) = "1"

# ------------------------------------------------------------------
#                            FUNCTIONS
# ------------------------------------------------------------------

@deploy
def __init__():
    ow.__init__()
    erc721.__init__(NAME, SYMBOL, BASE_URI, NAME, EIP_712_VERSION)

@external
def mint(uri: String[432]):
    token_id: uint256 = erc721._counter
    erc721._counter = token_id + 1
    erc721._safe_mint(msg.sender, token_id, b"")
    erc721._set_token_uri(token_id, uri)