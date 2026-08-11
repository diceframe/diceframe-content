# 文档访问与维护

本仓库的文档直接在 GitHub 阅读，无需单独建立文档网站。

## 访问入口

```text
文档目录   https://github.com/diceframe/diceframe-content/tree/main/docs
用户协议   https://github.com/diceframe/diceframe-content/blob/main/content/legal/terms/1.0/zh.md
隐私政策   https://github.com/diceframe/diceframe-content/blob/main/content/legal/privacy/1.0/zh.md
```

官网需要展示文档、用户协议或隐私政策时，直接使用上述链接即可。

## 内容更新

- 修改公告：编辑 `content/announcements/zh.md` 或 `en.md`，并同步更新 `content/manifest.json` 中的 SHA-256。
- 修改用户协议或隐私政策：新建版本目录，例如 `legal/terms/1.1/`，再更新版本、路径和 SHA-256。新版本会要求用户重新确认。
- 修改使用文档：编辑 `docs/` 下的 Markdown 文件。

提交前运行 `python scripts/verify_content.py`，确认清单中的内容版本和 SHA-256 一致。
