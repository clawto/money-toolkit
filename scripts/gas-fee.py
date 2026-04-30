#!/usr/bin/env python3
"""Gas费比价 & 省钱策略"""
import json
import sys
import urllib.request

def fetch_eth_gas():
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return json.loads(r.read()).get('result', {})
    except:
        return {}

def main():
    print("⛽ Gas费实时监控\n")
    
    gas = fetch_eth_gas()
    if gas:
        safe = gas.get('SafeGasPrice', 'N/A')
        propose = gas.get('ProposeGasPrice', 'N/A')
        fast = gas.get('FastGasPrice', 'N/A')
        base = gas.get('suggestBaseFee', 'N/A')
        
        print("🔷 Ethereum Gas:")
        print(f"  Base Fee: {base} Gwei")
        print(f"  🐢 慢速: {safe} Gwei (~${float(safe)*0.05:.2f})")
        print(f"  🚶 标准: {propose} Gwei (~${float(propose)*0.05:.2f})")
        print(f"  🚀 快速: {fast} Gwei (~${float(fast)*0.05:.2f})")
    else:
        print("  ❌ Etherscan API 不可用")
    
    print(f"\n💡 省钱技巧:")
    print("  • 周末凌晨 Gas 最低")
    print("  • 使用 L2 (Arbitrum/Optimism/Base) 省 90%+ Gas")
    print("  • Solana 费用 ~$0.00025 每笔")
    print("  • 批量交易比单笔省 Gas")
    print("  • https://etherscan.io/gastracker 查看实时Gas")

if __name__ == '__main__':
    main()
