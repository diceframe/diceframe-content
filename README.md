# DiceFrame Content

DiceFrame 的公开内容仓库，包含公告、使用文档、用户协议和隐私政策。

## 仓库内容

- `content/`：公告、用户协议和隐私政策。
- `docs/`：面向玩家的中英文用户手册、部署文档（包括独立 WebUI）与插件生态技术文档（插件开发、插件索引与审核、Bot Bridge、音色发布、场景图），可直接在 GitHub 中阅读。与具体代码版本强绑定的架构、应用更新、规则引擎和实验功能契约保留在主仓库 [`diceframe/diceframe`](https://github.com/diceframe/diceframe/tree/main/docs)，这里提供入口和面向用户的摘要。官网仓库只负责展示和导航这些公开文档，不维护重复正文。

`content/manifest.json` 指向当前公开版本，是公告和法律文本的发布来源；历史法律版本继续保留。主程序仓库中的 `legal/` 仅保存随发行版打包的离线快照，应与这里对应版本的原文保持一致。

DiceFrame 客户端会读取这里发布的最新公开文本；历史版本继续保留，便于查阅和对照。

## 使用方式

可以通过以下地址直接阅读：

```text
公告原文：https://raw.githubusercontent.com/diceframe/diceframe-content/main/content/announcements/zh.md
条款原文：https://raw.githubusercontent.com/diceframe/diceframe-content/main/content/legal/terms/1.1/zh.md
隐私政策：https://raw.githubusercontent.com/diceframe/diceframe-content/main/content/legal/privacy/1.2/zh.md
文档目录：https://github.com/diceframe/diceframe-content/tree/main/docs
```

官网可直接链接到文档目录、用户协议和隐私政策。
