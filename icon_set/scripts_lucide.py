"""Import shim so tests can reach ``scripts/lucide_reference.py``.

``icon_set/scripts/`` holds runnable entry points rather than an importable
package, so the reference helpers are re-exported here.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent / "scripts" / "lucide_reference.py"
_spec = importlib.util.spec_from_file_location("icon_set._lucide_impl", _SOURCE)
assert _spec and _spec.loader
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

REFERENCE_ROOT = _module.REFERENCE_ROOT
debug_path = _module.debug_path
inspect_reference = _module.inspect_reference
load_index = _module.load_index
original_path = _module.original_path
read_atoms = _module.read_atoms
search = _module.search

__all__ = [
    "REFERENCE_ROOT", "debug_path", "inspect_reference", "load_index",
    "original_path", "read_atoms", "search",
]
