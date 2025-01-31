# Mood NFT
An ERC721-compliant dynamic NFT that changes based on the owner's mood, built using Vyper. Each NFT can switch between "Happy" and "Sad" states, with all artwork and metadata stored completely on-chain.

Key Features

- Dynamic State Changes: NFTs can toggle between Happy and Sad moods
- 100% On-Chain Storage: All artwork (SVG) and metadata stored on-chain
- Base64 Encoding: Efficient encoding for SVG and JSON metadata
- Owner Controls: Only token owners can modify their NFT's mood
- Gas Optimized: Uses immutable variables and efficient encoding

# Getting Started

## Prerequisites
- git
  
You'll know you've done it right if you can run git --version and see a version number.
- anvil
  
You'll know you've done it right if you can run anvil --version and see an output like anvil 0.2.0 (fdd321b 2024-10-15T00:21:13.119600000Z)
- moccasin
  
You'll know you've done it right if you can run mox --version and get an output like: Moccasin CLI v0.3.0


# Setup & Installation

- Clone the repository
   
`git clone https://github.com/yourusername/mood-nft.git`

`cd mood-nft`

# Quickstart

```
# Deploy and mint the basic NFT
mox run deploy_basic_nft

# Deploy and mint the Mood NFT
mox run deploy_mood_nft

# Flip the mood of the deployed Mood NFT
mox run flip_mood
```
