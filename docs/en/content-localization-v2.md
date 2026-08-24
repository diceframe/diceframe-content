# Content V2 Localization

Content V2 separates resource identity from display language. Every resource has a stable canonical
`id`; language data lives in a `locales/<locale>/` overlay. An overlay may change names, descriptions,
labels, prompts, and other display fields, but never dice systems, numeric values, capabilities,
permissions, default rules, or other deterministic mechanics.

Regional locales such as `en-US` fall back to `en`, then to the resource's declared `default_locale`.
Do not use `name_en`, `name_ja`, or a translated name as a resource identity.
