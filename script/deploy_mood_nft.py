import base64

from src import mood_nft


def deploy_mood_nft():
    happy_svg_uri = ""
    sad_svg_uri = ""
    with open("./images/happy.svg", "r") as f:
        happy_svg = f.read()
        happy_svg_uri = svg_to_base64_uri(happy_svg)
    with open("./images/sad.svg", "r") as f:
        sad_svg = f.read()
        sad_svg_uri = svg_to_base64_uri(sad_svg)

    mood_nft_contract = mood_nft.deploy(happy_svg_uri, sad_svg_uri)
    print(f"Deployed mood NFT to {mood_nft_contract.address}")
    mood_nft_contract.mint_nft()
    print(mood_nft_contract.tokenURI(0))
    return mood_nft_contract


def moccasin_main():
    return deploy_mood_nft()


def svg_to_base64_uri(svg_content: str) -> str:
    """
    Convert SVG content to a base64-encoded data URI.

    Args:
        svg_content (str): The SVG content as a string

    Returns:
        str: Base64-encoded data URI for the SVG
    """
    svg_bytes = svg_content.encode("utf-8")
    base64_svg = base64.b64encode(svg_bytes).decode("utf-8")
    return f"data:image/svg+xml;base64,{base64_svg}"