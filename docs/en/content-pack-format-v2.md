# Content Pack V2 Format

The manifest uses independent version fields:

```json
{"schema_version":1,"content_schema_version":2,"locale_schema_version":1,"default_locale":"en"}
```

`schema_version` is the plugin manifest version; `content_schema_version` is the content resource model
(1 or 2); `locale_schema_version` is the typed locale overlay format (currently 1); and `default_locale`
is the package fallback. Unknown future versions are rejected. Resource identity is the `(owner, kind,
local_id)` tuple represented by `ResourceRef`, for example `core:item:longsword` or
`plugin:my-pack:item:moon_blade`. Canonical IDs include `fighter`, `longsword`, `chain_mail`,
`athletics`, and `str`; `longsword` may be displayed as `长剑`, `Longsword`, or `ロングソード`,
but the identity remains `longsword`.

Core resources live under `content/<kind>/`; locale overlays live under
`locales/<locale>/<kind>/`. Locale files may contain display and linguistic fields only. The validator
rejects mechanics, capability, and permission fields. V1 manifests remain installable, but new packs
should use the V2 schema.

## Copyable Item Example

```text
my-pack/content/items/moon_blade.json
my-pack/locales/en/items/moon_blade.json
```

Core: `{"id":"moon_blade","type":"weapon","damage_dice":"1d8"}`

Locale: `{"locale_schema_version":1,"locale":"en","target":{"kind":"item","id":"moon_blade"},"fields":{"name":"Moon Blade","description":"A blade that catches moonlight."}}`

Locale lookup is exact → base → package `default_locale` → its base → core display fields.
`damage_dice`, `ac_base`, and other mechanics belong only in core; putting them in locale is rejected.
Rules and worlds use plain IDs and reject duplicate IDs across plugins. Ordinary items, classes, spells,
NPCs, and character templates coexist through namespaced `ResourceRef` values.

## World Locale Example

World core owns the canonical `starter_lorebook` entry IDs, types, tiers, and other mechanics. A world
locale may only localize display fields by those stable IDs; it cannot replace the entry list or change
its mechanics:

```json
{"starter_lorebook":{"npc_guide":{"name":"Guide","keywords":["guide"],"content":"A local guide."}}}
```

`npc_guide` must already exist in the core world. World locale overlays may also provide
`world_name`, `description`, `world_setting`, and `starter_scene`; `suggested_difficulty` remains core.
