# quant-trading

美股量化交易策略和持仓管理

## 功能

- 每日自动分析美股数据
- 模拟交易（起始资金 100万$）
- Git 版本管理调仓记录

## 文件

- `portfolio.json` - 持仓数据
- `strategy.md` - 交易策略
- `quant-trading/SKILL.md` - OpenClaw Skill

## 定时任务

每天早上 8:05 自动执行分析并推送报告

## 使用

1. 修改 `strategy.md` 调整策略
2. 定时任务会自动读取策略执行交易
3. 所有变更通过 Git 版本管理
