"""Seed missing per-icon metadata files without overwriting existing edits.

Run: python3 -m icon_set.scripts.sync_metadata
"""
from icon_set.model.icons.registry import factories
from icon_set.model.metadata import load_metadata, metadata_path


def main():
    created = 0
    registered = factories()
    for icon in registered.values():
        missing = not metadata_path(icon).exists()
        load_metadata(icon, create=True)
        created += missing
    print(f"Validated {len(registered)} metadata files; created {created}.")


if __name__ == "__main__":
    main()
