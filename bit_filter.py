import requests
import binascii

# WhatsOnChain API base URL (mainnet, covering BTC history up to BSV fork)
BASE_URL = "https://api.whatsonchain.com/v1/bsv/main"

# Placeholder pattern from whitepaper font stream (replace with your actual finding)
CSW_PATTERN = b"435357"  # Hex for "CSW" in ASCII; update this!

def get_block_txs(block_height):
    """Fetch all transaction IDs for a given block height."""
    url = f"{BASE_URL}/block/height/{block_height}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch block {block_height}: {response.status_code}")
        return []
    block_data = response.json()
    return block_data["tx"]

def get_raw_tx(txid):
    """Fetch raw transaction hex and convert to bytes."""
    url = f"{BASE_URL}/tx/{txid}/hex"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch TX {txid}: {response.status_code}")
        return None
    try:
        # The API returns raw hex string directly, not JSON
        raw_hex = response.text.strip()
        return binascii.unhexlify(raw_hex)
    except Exception as e:
        print(f"Error processing TX {txid}: {e}")
        return None

def search_pattern_in_tx(tx_bytes, pattern):
    """Search for the CSW pattern in transaction bytes."""
    if pattern in tx_bytes:
        return True
    # Check reversed pattern (simple steganography variation)
    if pattern[::-1] in tx_bytes:
        return True
    return False

def analyze_early_blocks(start_height, end_height):
    """Search early blocks for the CSW pattern."""
    print(f"Searching blocks {start_height} to {end_height} for pattern {CSW_PATTERN.hex()}...")
    matches = []

    for height in range(start_height, end_height + 1):
        txids = get_block_txs(height)
        print(f"Block {height}: {len(txids)} transactions")
        
        for txid in txids:
            tx_bytes = get_raw_tx(txid)
            if tx_bytes and search_pattern_in_tx(tx_bytes, CSW_PATTERN):
                matches.append({
                    "block_height": height,
                    "txid": txid,
                    "raw_bytes_snippet": tx_bytes[:50].hex() + "..."
                })
    
    return matches

def main():
    # Analyze Genesis block and first few blocks
    START_HEIGHT = 0  # Genesis block
    END_HEIGHT = 10   # Adjust as needed
    
    matches = analyze_early_blocks(START_HEIGHT, END_HEIGHT)
    
    if matches:
        print("\nFound matches for CSW pattern:")
        for match in matches:
            print(f"Block {match['block_height']}, TXID: {match['txid']}, Bytes: {match['raw_bytes_snippet']}")
    else:
        print("\nNo matches found in specified blocks.")

if __name__ == "__main__":
    main()