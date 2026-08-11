# DiceFrame Content

DiceFrame 的公开内容仓库，包含公告、使用文档、用户协议和隐私政策。

## 内容规则

- `content/`：公告、用户协议和隐私政策。
- `docs/`：中英文使用文档，可直接在 GitHub 中阅读。
- 修改用户协议或隐私政策时，必须新增版本目录，不覆盖已发布版本。
- 修改 `content/` 后，同步更新 `content/manifest.json` 的版本和 SHA-256；运行 `python scripts/verify_content.py` 校验。
- 请勿提交账号信息、密钥、私人数据或内部资料。

## 使用方式

仓库发布后，可通过以下地址访问：

```text
公告原文：https://raw.githubusercontent.com/diceframe/diceframe-content/main/content/announcements/zh.md
条款原文：https://raw.githubusercontent.com/diceframe/diceframe-content/main/content/legal/terms/1.0/zh.md
文档目录：https://github.com/diceframe/diceframe-content/tree/main/docs
```

官网可直接链接到文档目录、用户协议和隐私政策。
