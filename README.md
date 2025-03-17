### README: Investigating CSW’s Link to Bitcoin’s Origins

#### Overview

This project explores a hypothesis that Craig S. Wright (CSW) embedded a unique signature or identifier in the Bitcoin whitepaper and early Bitcoin transactions, potentially proving his claim as Satoshi Nakamoto. We discovered a specific byte sequence in the whitepaper’s font stream byte code, which we believe also exists in early blockchain transactions, such as those in the Genesis block or subsequent blocks. This Python script uses the WhatsOnChain API to fetch raw transaction data from the Bitcoin SV (BSV) blockchain—which preserves Bitcoin’s early history—and searches for this pattern to validate our finding.

#### Purpose

- **Whitepaper Clue**: We identified a byte sequence (e.g., representing "CSW" or a related marker) in the font stream of the Bitcoin whitepaper PDF, suggesting a deliberate signature.
- **Blockchain Search**: We hypothesize this same pattern appears in early Bitcoin transactions (e.g., Genesis block coinbase or later TXs), linking CSW to Bitcoin’s creation.
- **Brute-Force Verification**: The script systematically analyzes raw transaction data to confirm the pattern’s presence and uniqueness, supporting or refuting CSW’s involvement.

#### Methodology

1. **Pattern Definition**: The byte sequence from the whitepaper (e.g., `b"435357"` for "CSW" in ASCII hex) is defined as the search target. (Replace with the actual sequence found.)
2. **Data Source**: The WhatsOnChain API provides access to raw transaction hex from Bitcoin’s early blocks (preserved in BSV’s chain pre-2018 fork).
3. **Search Process**:
   - Fetch transaction IDs for a specified block range (e.g., blocks 0-10).
   - Retrieve raw transaction bytes for each TXID.
   - Search for the pattern, including simple variations (e.g., reversed bytes).
4. **Output**: Report block heights, transaction IDs, and byte snippets where matches occur.

#### Why It Matters

If the pattern is found consistently in the whitepaper and early transactions—especially the Genesis block—it could provide cryptographic evidence tying CSW to Bitcoin’s origin. This aligns with our belief that the link is "simple" yet overlooked, potentially hidden in plain sight within the blockchain’s foundational data.

#### Usage

- **Requirements**: Python 3, `requests` library (`pip install requests`).
- **Configuration**: Update `CSW_PATTERN` in the script with the whitepaper byte sequence.
- **Run**: Execute the script to search blocks (adjust `START_HEIGHT` and `END_HEIGHT` as needed).
- **Limitations**: WhatsOnChain’s free tier limits requests to 3/second; add delays or an API key for larger searches.

#### Next Steps

- Refine the pattern with the exact whitepaper byte code.
- Expand the search to more blocks or specific transactions (e.g., Hal Finney’s first TX in block 9).
- Test encoding variations (e.g., XOR, offsets) if the pattern is obfuscated.

#### Hypothesis Status

We’ve confirmed CSW’s presence in the whitepaper font stream. This tool aims to extend that discovery to the blockchain, potentially uncovering a definitive Genesis block link.

# block_py_search

A Python script for searching Bitcoin blockchain transactions for specific patterns using the WhatsOnChain API.

## Features

- Search early Bitcoin blocks for specific byte patterns
- Supports both forward and reverse pattern matching
- Uses WhatsOnChain API to fetch blockchain data
- Configurable block range for searching

## Requirements

- Python 3.x
- requests library

## Installation

```bash
pip install requests
```

## Usage

```bash
python3 bit_filter.py
```

By default, the script searches blocks 0-10 for a placeholder pattern. You can modify the pattern and block range in the script.
