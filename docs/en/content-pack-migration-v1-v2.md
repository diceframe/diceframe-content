# Migrating Content Packs from V1 to V2

1. Assign stable canonical `local_id` values to rules, worlds, classes, items, and other resources.
2. Move `name_en`, `name_ja`, and full localized copies into `locales/<locale>/` overlays.
3. Preserve legacy and unknown user fields; read them through the V1 adapter before projecting V2 identity.
4. Run the main-repository validator and locale mechanics snapshots before publishing the pack.

Migration does not delete saves or rewrite old databases, and translated names never become identities.
Legacy packs remain usable while their V2 representation is generated incrementally.
