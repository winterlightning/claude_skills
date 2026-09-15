"""Single read path for the frozen contract JSON.

Numeric rules live once, in ``model/contracts/*.json``. Every runtime type in
this package derives its constants from these documents rather than restating
them, so a contract edit cannot silently disagree with the code.

The one way to read anything other than the locked files is the
``ICON_CONTRACT_OVERLAY`` environment variable, which names a JSON file of
experimental values deep-merged over them. It exists so a proposed profile
number can be measured against the whole corpus without editing a locked
contract; ``icon_set/scripts/profile_lab.py`` sets it for its own subprocess
and clears it afterwards. Nothing in the build, the validator or the tests sets
it, and an overlaid document is stamped ``status: experimental`` so a rule
change can never be mistaken for a shipped one.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path

CONTRACTS_DIR = Path(__file__).resolve().parent / "contracts"

#: Points at a JSON file of experimental contract values, keyed by contract
#: stem. Set by ``icon_set/scripts/profile_lab.py`` in the subprocess it
#: measures under, and by nothing else. Unset -- the normal case, including
#: every test and every build -- the locked contracts are read verbatim.
OVERLAY_ENV = "ICON_CONTRACT_OVERLAY"


def _merge(base: dict, patch: dict) -> dict:
    """Deep-merge ``patch`` into a copy of ``base``; lists replace wholesale."""
    out = dict(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = value
    return out


@lru_cache(maxsize=None)
def load(name: str) -> dict:
    """Return a parsed contract document by file stem."""
    path = CONTRACTS_DIR / f"{name}.json"
    if not path.is_file():
        raise FileNotFoundError(f"missing contract: {path}")
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    overlay = os.environ.get(OVERLAY_ENV)
    if overlay:
        patch = json.loads(Path(overlay).read_text(encoding="utf-8")).get(name)
        if patch:
            data = _merge(data, patch)
            data["status"] = "experimental"
    return data


def icon_profile() -> dict:
    return load("icon-profile.v1")


def families() -> dict[str, dict]:
    """The three authored families and the profile, folder and dist each owns."""
    return {
        name: row for name, row in icon_profile()["families"].items()
        if not name.startswith("_")
    }


def family_for_profile(profile_name: str) -> str:
    """The one family that may author on ``profile_name``."""
    return icon_profile()["profiles"][profile_name]["family"]


def keyshapes() -> dict:
    return load("keyshapes.v1")


def composition_templates() -> dict:
    return load("composition-templates.v1")


def exceptions() -> dict:
    return load("exceptions.v1")


def categories() -> dict:
    return load("categories")


@lru_cache(maxsize=None)
def approved_free_keyshapes() -> dict[tuple[str, str], dict]:
    """Approved FREE records keyed by ``(icon_id, profile_name)``."""
    return {
        (record["icon_id"], record["profile"]): record
        for record in exceptions()["free_keyshapes"]
    }
