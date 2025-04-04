# 🚀 Crypto (Systematic) Trading Strategies using On-chain / Sentiment / Alternative data

A collection of cryptocurrency trading strategies and backtesting tools, focusing on turning alternative / on-chain data into trading systems.

It has:

- 🔄 Vectorized backtesting function for efficient strategy testing
- 💰 Basic Transaction cost modeling
- 📊 Performance metrics calculation

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Exchange Outflow Strategy

The [`exchange_outflows.py`](exchange_outflows.py) script demonstrates how to turn exchange outflow data into a trading strategy:

- 📤 High outflows might indicate infestor confidence, and reduce the assets available for immediate selling
- 📥 Low outflows might indicate that crypto assets on exchanges are pilingup
- 💰 Supports both long-only and long-short strategies


## 🔑 API Integration

The strategy integrates with:

- 🏦 Binance API for price data
- 📊 Unravel Markets API for exchange outflow data. Sign up for live access at [unravel.markets](https://unravel.markets)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
