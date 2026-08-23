# Migrating Content Packs from V1 to V2

1. Assign stable canonical `local_id` values to rules, worlds, classes, items, and other resources.
2. Move `name_en`, `name_ja`, and full localized copies into `locales/<locale>/` overlays.
3. Preserve legacy and unknown user fields. Runtime V1 adapters continue to read them; only an explicit author/tool conversion writes V2 identity, and the original pack is not rewritten automatically.
4. Run the main-repository validator and locale mechanics snapshots before publishing the pack.

Migration does not delete saves or rewrite old databases, and translated names never become identities.
Legacy V1 packs remain readable through compatibility adapters. Installing, loading, starting, or saving
a game does not rewrite the original pack. Creating a V2 representation is an explicit author/tool
migration operation.
