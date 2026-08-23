# DiceFrame 文档

本仓库是 DiceFrame 面向用户的公开内容源：公告、法律文本、用户手册、部署说明与插件生态技术文档维护在这里，并由官网和客户端引用。与具体代码版本强绑定的架构、应用更新、规则引擎和实验功能契约保留在主仓库 [`diceframe/diceframe`](https://github.com/diceframe/diceframe/tree/main/docs)；官网仓库 [`diceframe/diceframe-site`](https://github.com/diceframe/diceframe-site) 只负责展示和导航，不保存另一份文档正文。

| 中文 | English |
| --- | --- |
| [使用指南](zh/guide.md) | [Guide](en/guide.md) |
| [语音功能（可选）](zh/voice.md) | [Optional voice features](en/voice.md) |
| [部署说明](zh/deploy.md) | [Deployment](en/deploy.md) |
| [独立部署 WebUI](zh/standalone-webui.md) | [Standalone WebUI deployment](en/standalone-webui.md) |
| [插件开发指南](zh/plugin-development.md) | [Plugin development](en/plugin-development.md) |
| [插件索引与审核](zh/plugin-registry.md) | [Plugin registry](en/plugin-registry.md) |
| [Bot Bridge 核心](zh/bot-bridge-core.md) | [Bot Bridge core](en/bot-bridge-core.md) |
| [发布音色预设](zh/voice-pack-publishing.md) | [Publishing voice presets](en/voice-pack-publishing.md) |
| [冒险头图链路规范](zh/scene-images.md) | — |

主仓库中的版本绑定文档包括[规则与骰子](https://github.com/diceframe/diceframe/blob/main/docs/zh/rules-and-dice.md)、[玩家直连](https://github.com/diceframe/diceframe/blob/main/docs/zh/direct-connect.md)和[架构说明](https://github.com/diceframe/diceframe/blob/main/docs/ARCHITECTURE_CN.md)。

公开公告和法律文件位于仓库根目录的 [`content/`](../content/)。修改公告时，依赖公告源的服务可能需要同步或重新部署；普通文档更新由官网直接读取，不需要复制到 DiceFrame Hub。

## Content V2 入口

内容包的 manifest 版本彼此独立：`schema_version: 1` 是插件 manifest 主版本，
`content_schema_version: 2` 表示 canonical 内容格式，`locale_schema_version: 1` 表示 typed
locale overlay。资源引用使用 `ResourceRef`（`owner + kind + local_id`），例如
`plugin:starter-content-v2:item:moon_blade`；翻译名称不是身份，locale 也不能修改 mechanics。

- [Content V2 格式（中文）](zh/content-pack-format-v2.md) / [English](en/content-pack-format-v2.md)
- [Content V2 本地化（中文）](zh/content-localization-v2.md) / [English](en/content-localization-v2.md)
- [V1 到 V2 迁移（中文）](zh/content-pack-migration-v1-v2.md) / [English](en/content-pack-migration-v1-v2.md)
- [主仓库 starter-content-v2 示例](https://github.com/diceframe/diceframe/tree/main/plugins/examples/starter-content-v2)
