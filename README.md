# Active Risk Overlays for Crypto Assets with Predictive Exogenous Risk Factors

A collection of strategies, backtesting tools, focusing on turning alternative / on-chain data into predictive risk factors to manage portfolio volatility.

It's intended as a sample repository, containing:

- Vectorized backtesting function for efficient strategy testing
- Basic Transaction cost modeling
- Performance metrics calculation

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Exchange Outflow Risk Overlay

The [`exchange_outflows.py`](exchange_outflows.py) script demonstrates how to turn exchange outflow data into an effective active risk overlay on top of Bitcoin:

- High outflows might indicate infestor confidence, and reduce the assets available for immediate selling
- Low outflows might indicate that crypto assets on exchanges are pilingup


## API Integration

The repository uses:

- Unravel Core API to access Predictive Risk Factors. Sign up for live access at [unravel](https://unravel.markets/). Trial API Key included, that provides weekly data for 2022-2024.
- Binance API for price data


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
