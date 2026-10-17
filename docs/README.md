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

主仓库中的版本绑定文档包括：

| 内容 | 简体中文 | English |
| --- | --- | --- |
| AI 与界面设置 | [指南](https://github.com/diceframe/diceframe/blob/main/docs/zh/ai-settings.md) | [Guide](https://github.com/diceframe/diceframe/blob/main/docs/en/ai-settings.md) |
| 内容、角色与游玩 | [指南](https://github.com/diceframe/diceframe/blob/main/docs/zh/content-and-play.md) | [Guide](https://github.com/diceframe/diceframe/blob/main/docs/en/content-and-play.md) |
| 应用更新与恢复 | [指南](https://github.com/diceframe/diceframe/blob/main/docs/zh/updates.md) | [Guide](https://github.com/diceframe/diceframe/blob/main/docs/en/updates.md) |
| 规则与骰子 | [指南](https://github.com/diceframe/diceframe/blob/main/docs/zh/rules-and-dice.md) | [Guide](https://github.com/diceframe/diceframe/blob/main/docs/en/rules-and-dice.md) |
| 玩家直连 | [指南](https://github.com/diceframe/diceframe/blob/main/docs/zh/direct-connect.md) | [Guide](https://github.com/diceframe/diceframe/blob/main/docs/en/direct-connect.md) |
| 架构 | [说明](https://github.com/diceframe/diceframe/blob/main/docs/ARCHITECTURE_CN.md) | [Architecture](https://github.com/diceframe/diceframe/blob/main/docs/ARCHITECTURE_EN.md) |

公开公告和法律文件位于仓库根目录的 [`content/`](../content/)。修改公告时，依赖公告源的服务可能需要同步或重新部署；普通文档更新由官网直接读取，不需要复制到 DiceFrame Hub。

## 文档维护与界面变更

使用指南按主仓库已合入的界面编写，旧版本可能有不同菜单。功能的配置字段、权限、兼容性与迁移规则以对应版本的主仓库文档和实现为准；这里用操作步骤解释，并链接到契约来源，避免维护两份配置规范。

- 主仓库改变导航、按钮名称、默认值或操作前提时，同时核对本仓库的使用、部署、语音说明，以及插件文档引用的界面入口。
- 官方同步维护英语与简体中文；两种语言的操作路径和限制应一致。其他语言由社区维护，缺失界面文案的回退规则见主仓库[翻译政策](https://github.com/diceframe/diceframe/blob/main/docs/en/translations.md)。
- 修改后检查相对链接、跨仓库目标与相关截图。截图只使用演示数据，避免带入密钥、私有存档和个人信息。
- 未合入功能保留为提案，不写成当前可用操作。跨仓库变更使用关联的文档 PR，合并前复核主分支的实际界面；官网继续读取这里的正文，不再复制一份。

## Content V2 入口

内容包的 manifest 版本彼此独立：`schema_version: 1` 是插件 manifest 主版本，
`content_schema_version: 2` 表示 canonical 内容格式，`locale_schema_version: 1` 表示 typed
locale overlay。资源引用使用 `ResourceRef`（`owner + kind + local_id`），例如
`plugin:starter-content-v2:item:moon_blade`；翻译名称不是身份，locale 也不能修改 mechanics。

- [Content V2 格式（中文）](zh/content-pack-format-v2.md) / [English](en/content-pack-format-v2.md)
- [Content V2 本地化（中文）](zh/content-localization-v2.md) / [English](en/content-localization-v2.md)
- [V1 到 V2 迁移（中文）](zh/content-pack-migration-v1-v2.md) / [English](en/content-pack-migration-v1-v2.md)
- [主仓库 starter-content-v2 示例](https://github.com/diceframe/diceframe/tree/main/plugins/examples/starter-content-v2)
