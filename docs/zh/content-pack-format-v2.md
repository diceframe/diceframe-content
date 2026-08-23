# Content Pack V2 格式

manifest 使用 `content_schema_version: 2`，并声明 `default_locale`。资源身份是
`(owner, kind, local_id)`；同一 owner 下的 kind/local_id 不得重复，不同 owner 可以复用 local_id。

资源 core 放在 `content/<kind>/`，语言 overlay 放在 `locales/<locale>/<kind>/`。locale 文件只能
提供展示与语言字段，校验器会拒绝 mechanics、权限和能力字段。V1 manifest 仍可安装，但新包应使用
V2 schema。
