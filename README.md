# quant-trading

美股量化交易策略和持仓管理

## 目录结构

```
quant-trading/
├── .skill/           # Agent Skill 配置
│   ├── SKILL.md    # Skill 定义
│   └── strategy.md # 交易策略配置
├── log/             # 交易日志
│   ├── portfolio.json  # 持仓数据
│   └── trades/        # 交易记录
├── backtest/        # 回测代码
│   └── backtest.py
└── README.md
```

## 功能

- **.skill/** - 交易策略配置（AI Agent 使用）
- **log/** - 持仓和交易记录
- **backtest/** - 历史回测代码

## 定时任务

每天早上 8:05 自动执行分析并推送报告

## 使用

1. 修改 `.skill/strategy.md` 调整策略
2. 定时任务会自动读取策略执行交易
3. 所有变更通过 Git 版本管理
4. 使用 `backtest/` 进行历史回测
