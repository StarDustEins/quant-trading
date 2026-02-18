#!/usr/bin/env python3
"""
量化交易回测脚本
基于历史数据测试策略表现
"""

import json
import csv
from datetime import datetime, timedelta
from typing import List, Dict

# 配置
INITIAL_CAPITAL = 1_000_000  # 起始资金 100万$
MAX_POSITIONS = 5  # 最大持仓数
MAX_POSITION_PCT = 0.30  # 单只股票上限 30%
STOP_LOSS_PCT = 0.05  # 止损线 5%
TAKE_PROFIT_PCT = 0.15  # 止盈线 15%


def load_history_data(csv_file: str) -> List[Dict]:
    """加载历史数据"""
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'date': row['date'],
                'symbol': row['symbol'],
                'open': float(row['open']),
                'high': float(row['high']),
                'low': float(row['low']),
                'close': float(row['close']),
                'volume': int(row['volume'])
            })
    return data


def calculate_returns(entry_price: float, exit_price: float) -> float:
    """计算收益率"""
    return (exit_price - entry_price) / entry_price


def backtest(data: List[Dict], strategy_rules: Dict) -> Dict:
    """回测"""
    cash = INITIAL_CAPITAL
    positions = {}  # {symbol: {'quantity': int, 'entry_price': float}}
    trades = []
    portfolio_value = []

    # 按日期分组
    by_date = {}
    for row in data:
        date = row['date']
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(row)

    for date, rows in sorted(by_date.items()):
        # 获取当日收盘价
        day_close = {r['symbol']: r['close'] for r in rows}
        
        # 检查止损/止盈
        for symbol, pos in list(positions.items()):
            if symbol in day_close:
                current_price = day_close[symbol]
                ret = calculate_returns(pos['entry_price'], current_price)
                
                # 止损
                if ret <= -STOP_LOSS_PCT:
                    proceeds = pos['quantity'] * current_price
                    cash += proceeds
                    trades.append({
                        'date': date,
                        'action': 'SELL',
                        'symbol': symbol,
                        'quantity': pos['quantity'],
                        'price': current_price,
                        'reason': 'STOP_LOSS'
                    })
                    del positions[symbol]
                # 止盈
                elif ret >= TAKE_PROFIT_PCT:
                    proceeds = pos['quantity'] * current_price
                    cash += proceeds
                    trades.append({
                        'date': date,
                        'action': 'SELL',
                        'symbol': symbol,
                        'quantity': pos['quantity'],
                        'price': current_price,
                        'reason': 'TAKE_PROFIT'
                    })
                    del positions[symbol]

        # 选股信号（示例：涨幅 > 2%）
        for row in rows:
            if len(positions) >= MAX_POSITIONS:
                break
            
            change = (row['close'] - row['open']) / row['open']
            if change > 0.02 and row['symbol'] not in positions:
                # 买入
                quantity = int((cash * 0.2) / row['close'])  # 20%仓位
                if quantity > 0:
                    cost = quantity * row['close']
                    cash -= cost
                    positions[row['symbol']] = {
                        'quantity': quantity,
                        'entry_price': row['close']
                    }
                    trades.append({
                        'date': date,
                        'action': 'BUY',
                        'symbol': row['symbol'],
                        'quantity': quantity,
                        'price': row['close'],
                        'reason': f'涨幅{change:.1%}'
                    })

        # 计算当日组合价值
        day_value = cash
        for symbol, pos in positions.items():
            if symbol in day_close:
                day_value += pos['quantity'] * day_close[symbol]
        portfolio_value.append({'date': date, 'value': day_value})

    # 最终平仓
    final_value = cash
    last_date = list(by_date.keys())[-1]
    for symbol, pos in positions.items():
        final_value += pos['quantity'] * day_close.get(symbol, pos['entry_price'])

    return {
        'initial_capital': INITIAL_CAPITAL,
        'final_value': final_value,
        'total_return': (final_value - INITIAL_CAPITAL) / INITIAL_CAPITAL,
        'trades': trades,
        'portfolio_value': portfolio_value
    }


def main():
    # 示例运行
    print("=" * 50)
    print("量化交易回测系统")
    print("=" * 50)
    print(f"起始资金: ${INITIAL_CAPITAL:,.2f}")
    print(f"最大持仓: {MAX_POSITIONS} 只")
    print(f"单只上限: {MAX_POSITION_PCT*100}%")
    print(f"止损线: {STOP_LOSS_PCT*100}%")
    print(f"止盈线: {TAKE_PROFIT_PCT*100}%")
    print("=" * 50)
    print("\n请使用以下命令加载数据并运行回测:")
    print("python backtest.py --data data.csv")


if __name__ == '__main__':
    main()
