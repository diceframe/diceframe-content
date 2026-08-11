"""Validate hashes declared for client-fetched public content."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
MANIFEST = json.loads((CONTENT / "manifest.json").read_text(encoding="utf-8"))


def verify(path: object, expected: object) -> None:
    if not isinstance(path, str) or not isinstance(expected, str):
        raise ValueError("manifest requires a content path and SHA-256")
    target = (CONTENT / path).resolve()
    if CONTENT not in target.parents or not target.is_file():
        raise ValueError(f"invalid content path: {path}")
    actual = hashlib.sha256(target.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"SHA-256 mismatch: {path}")


for entry in MANIFEST.get("announcements", {}).values():
    if isinstance(entry, dict):
        verify(entry.get("path"), entry.get("sha256"))
    else:
        raise ValueError("invalid announcement manifest entry")

for document in MANIFEST.get("documents", {}).values():
    if not isinstance(document, dict):
        raise ValueError("invalid legal document manifest entry")
    for localized in document.get("languages", {}).values():
        if isinstance(localized, dict):
            verify(localized.get("path"), localized.get("sha256"))
        else:
            raise ValueError("invalid legal language manifest entry")
