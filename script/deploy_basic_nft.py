from src import basic_nft

PUG_URI = "QmanoFs6a4GHRtTW32w1fFJSv61TFT8Vk9qKqFF1mcdjMK"


def deploy_basic_nft():
    contract = basic_nft.deploy()
    contract.mint(PUG_URI)
    token_uri = contract.tokenURI(0)
    print(token_uri)


def moccasin_main():
    deploy_basic_nft()