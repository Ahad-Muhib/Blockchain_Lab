import sys
sys.path.append("/Users/Lab4/Desktop/blockchain implementation")  #path dewa lagbe ekhane folder er

from Blockchain.Backend.Core.blockchain import Blockchain

if __name__ == "__main__":
    print("Initializing Blockchain...")
    blockchain = Blockchain()

    blockchain.add_next_block()
    blockchain.add_next_block()

    blockchain.print()