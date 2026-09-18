"""Editable search metadata, independent of geometry and build artifacts."""
from __future__ import annotations

import json
import re
from pathlib import Path
from types import SimpleNamespace
from . import contracts

ROOT = Path(__file__).resolve().parents[1] / "metadata"
FIELDS = ("name", "description", "tags", "aliases", "category", "keywords")


def metadata_path(icon, root: Path | None = None) -> Path:
    if icon.family not in contracts.families() or not re.fullmatch(
        r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", icon.icon_id
    ):
        raise ValueError(f"Invalid metadata identity: {icon.family}/{icon.icon_id}")
    return (ROOT if root is None else root) / icon.family / f"{icon.icon_id}.json"


def defaults(icon) -> dict:
    keywords = list(dict.fromkeys(getattr(icon, "keywords", ())))
    return {
        "schema_version": 1,
        "icon_id": icon.icon_id,
        "family": icon.family,
        "name": icon.icon_id.replace("-", " ").capitalize(),
        "description": getattr(icon, "description", ""),
        "tags": list(dict.fromkeys(getattr(icon, "tags", keywords))),
        "aliases": list(dict.fromkeys(getattr(icon, "aliases", ()))),
        "category": getattr(icon, "category", ""),
        "keywords": keywords,
    }


def validate(document: dict, icon) -> None:
    if not isinstance(document, dict):
        raise ValueError("Metadata must be a JSON object")
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        raise ValueError("Metadata schema_version must be 1")
    for field in ("icon_id", "family"):
        if document.get(field) != getattr(icon, field):
            raise ValueError(f"Metadata {field} does not match {getattr(icon, field)!r}")
    for field in ("name", "description", "category"):
        if not isinstance(document.get(field), str):
            raise ValueError(f"Metadata {field} must be a string")
    if not document["name"].strip():
        raise ValueError("Metadata name must not be blank")
    for field in ("tags", "aliases", "keywords"):
        values = document.get(field)
        if (not isinstance(values, list)
                or any(not isinstance(value, str) or not value.strip() for value in values)
                or len(values) != len(set(values))):
            raise ValueError(f"Metadata {field} must contain unique nonblank strings")


def load_metadata(icon, *, root: Path | None = None, create: bool = False) -> dict:
    """Read without caching; optionally seed missing files, never overwrite edits."""
    path = metadata_path(icon, root)
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        document = defaults(icon)
        validate(document, icon)
        if create:
            path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with path.open("x", encoding="utf-8") as stream:
                    stream.write(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
            except FileExistsError:
                return load_metadata(icon, root=root)
    except ValueError as error:
        raise ValueError(f"{path}: {error}") from error
    try:
        validate(document, icon)
    except ValueError as error:
        raise ValueError(f"{path}: {error}") from error
    return document


def record_metadata(icon) -> dict:
    # Unregistered geometry drafts may have no family.
    document = load_metadata(icon) if icon.family in contracts.families() else defaults(icon)
    return {field: document[field] for field in FIELDS}


def publish_metadata(records: list[dict], directory: Path, registered: dict) -> None:
    """Read source metadata without mutation; publish changed output sidecars only."""
    directory.mkdir(parents=True, exist_ok=True)
    keep = set()
    from ..scripts.profile_links import annotate as annotate_profile_links
    annotate_profile_links(records)
    for record in records:
        icon = registered.get(record["icon_id"])
        document = (load_metadata(icon) if icon is not None
                    else defaults(SimpleNamespace(**record)))
        for field in ('profile_sources','profile_derivatives'):
            if record.get(field):document[field]=record[field]
            else:document.pop(field,None)
        record.update({field: document[field] for field in FIELDS})
        filename = f"{record['icon_id']}.metadata.json"
        keep.add(filename)
        target = directory / filename
        content = json.dumps(document, indent=2, ensure_ascii=False) + "\n"
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
    for path in directory.glob("*.metadata.json"):
        if path.name not in keep:
            path.unlink()
