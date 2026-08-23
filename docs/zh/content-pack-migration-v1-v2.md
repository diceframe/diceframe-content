# Content Pack V1 到 V2 迁移

1. 为规则、世界、职业、道具等资源分配稳定的 canonical `local_id`。
2. 把 `name_en`、`name_ja` 和本地化全文复制拆到 `locales/<locale>/`。
3. 保留旧字段和未知用户字段，先通过 V1 adapter 读取，再投影到 V2 identity。
4. 运行主仓库 validator 与 locale mechanics snapshot；失败时不要写入新包。

迁移不删除用户存档、不重写旧数据库，也不把翻译名称重新当作身份。旧包可继续使用，后续保存时再
逐步生成 V2 表示。
