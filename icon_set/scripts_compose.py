"""Import shim so tests can reach ``scripts/compose.py``.

``icon_set/scripts/`` holds runnable entry points rather than an importable
package, so the composition helper is re-exported here for the test suite and
for any caller that wants it as a library.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent / "scripts" / "compose.py"
_spec = importlib.util.spec_from_file_location("icon_set._compose_impl", _SOURCE)
assert _spec and _spec.loader
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

compose = _module.compose
template = _module.template
frozen_classes = _module.frozen_classes

__all__ = ["compose", "template", "frozen_classes"]
