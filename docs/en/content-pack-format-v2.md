# Content Pack V2 Format

The manifest declares `content_schema_version: 2` and a `default_locale`. Resource identity is the
tuple `(owner, kind, local_id)`: a kind/local_id pair must be unique within one owner, while different
owners may reuse the same local_id.

Core resources live under `content/<kind>/`; locale overlays live under
`locales/<locale>/<kind>/`. Locale files may contain display and linguistic fields only. The validator
rejects mechanics, capability, and permission fields. V1 manifests remain installable, but new packs
should use the V2 schema.
