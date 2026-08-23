# Content Pack V2 格式

manifest 使用以下独立版本字段：

```json
{"schema_version": 1, "content_schema_version": 2, "locale_schema_version": 1, "default_locale": "en"}
```

`schema_version` 是插件 manifest 版本；`content_schema_version` 是内容资源模型（支持 1 或 2）；
`locale_schema_version` 是 typed locale overlay 格式（支持 1）；`default_locale` 是包级语言回退。
未知 future version 会被宿主拒绝。资源身份是 `(owner, kind, local_id)`，也就是 `ResourceRef`，
例如 `core:item:longsword` 或 `plugin:my-pack:item:moon_blade`；稳定 canonical ID 包括
`fighter`、`longsword`、`chain_mail`、`athletics` 和 `str`。`longsword` 可以显示为“长剑”、
`Longsword` 或“ロングソード”，但身份始终是 `longsword`。同一 owner 下的 kind/local_id
不得重复，不同 owner 可以复用 local_id。

资源 core 放在 `content/<kind>/`，语言 overlay 放在 `locales/<locale>/<kind>/`。locale 文件只能
提供展示与语言字段，校验器会拒绝 mechanics、权限和能力字段。V1 manifest 仍可安装，但新包应使用
V2 schema。

## 可复制的道具示例

```text
my-pack/content/items/moon_blade.json
my-pack/locales/en/items/moon_blade.json
```

core 文件：

```json
{"id":"moon_blade","type":"weapon","damage_dice":"1d8"}
```

locale 文件：

```json
{"locale_schema_version":1,"locale":"en","target":{"kind":"item","id":"moon_blade"},"fields":{"name":"Moon Blade","description":"A blade that catches moonlight."}}
```

locale 查找顺序是 exact → base → 包的 `default_locale` → default 的 base → core 展示字段。
`damage_dice`、`ac_base` 等 mechanics 只能写在 core，写入 locale 会被宿主拒绝。规则和世界使用
plain ID，跨插件重复会拒绝；普通 item、class、spell、npc 和 character template 使用 namespaced
`ResourceRef` 共存。

## 世界 Locale 示例

世界 core 拥有 canonical 的 `starter_lorebook` 条目 ID、类型、tier 和其他机制。世界 locale 只能按
这些稳定 ID 覆盖显示字段，不能替换条目列表或改变机制：

```json
{"starter_lorebook":{"npc_guide":{"name":"Guide","keywords":["guide"],"content":"当地向导。"}}}
```

`npc_guide` 必须已经存在于 core 世界。世界 locale 还可以提供 `world_name`、`description`、
`world_setting` 和 `starter_scene`；`suggested_difficulty` 始终由 core 提供。
