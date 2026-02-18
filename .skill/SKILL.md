# Quant Trading Skill

美股量化交易分析 skill，基于 `.skill/strategy.md` 中的策略执行模拟交易。

## 文件结构

```
quant-trading/
├── .skill/
│   ├── SKILL.md      # 本文件
│   └── strategy.md  # 交易策略配置
├── log/
│   ├── portfolio.json  # 持仓数据
│   └── trades/         # 交易记录
├── backtest/
│   └── backtest.py    # 回测代码
└── README.md
```

## 功能

- 获取美股实时数据
- 分析市场走势，制定调仓策略
- 计算持仓盈亏
- Git 版本管理策略变更

## 每日任务

1. **读取持仓** - 从 `log/portfolio.json` 获取当前持仓
2. **获取数据** - 访问 Yahoo Finance 获取实时行情
3. **分析策略** - 根据 `.skill/strategy.md` 中的规则决定买卖
4. **更新持仓** - 修改 `log/portfolio.json`
5. **Git 提交** - 记录每次调仓变化
6. **生成报告** - 发送给用户

## 报告格式

```
📊 每日量化报告 - {日期}

💰 账户概况
- 起始资金：$1,000,000
- 当前总资产：$XXX,XXX
- 持仓盈亏：+$X,XXX / -$X,XXX (+X.XX%)

📈 当前持仓
| 股票 | 数量 | 成本价 | 现价 | 盈亏 |
|------|------|--------|------|------|
| XXX  | 100  | $150   | $160 | +$1000 |

📋 调仓计划
- 买入：XXX (理由)
- 卖出：XXX (理由)
```

## 策略调整

修改 `.skill/strategy.md` 文件调整策略，所有变更通过 Git 版本管理。
