# Content V2 本地化

Content V2 将内容身份与显示语言分开。每个资源使用稳定的 canonical `id`，语言内容放在
`locales/<locale>/` overlay 中。overlay 只能覆盖 `name`、`description`、`label`、提示词和
其他展示字段，不能修改骰制、数值、能力、权限、默认规则或其他 deterministic mechanics。

`en-US` 等区域语言先回退到 `en`，缺少目标语言时回退资源声明的 `default_locale`。不要使用
`name_en`、`name_ja` 或翻译后的名称作为资源身份。
