# Content Pack V1 到 V2 迁移

1. 为规则、世界、职业、道具等资源分配稳定的 canonical `local_id`。
2. 把 `name_en`、`name_ja` 和本地化全文复制拆到 `locales/<locale>/`。
3. 保留旧字段和未知用户字段；运行时由 V1 adapter 继续读取并兼容，迁移工具或作者明确转换后才写入 V2 identity，不会自动改写原包。
4. 运行主仓库 validator 与 locale mechanics snapshot；失败时不要写入新包。

迁移不删除用户存档、不重写旧数据库，也不把翻译名称重新当作身份。旧 V1 内容继续通过兼容适配器读取。
安装、加载、启动游戏或保存游戏都不会自动改写原始内容包。V2 表示只会由作者或明确的迁移工具主动生成。
