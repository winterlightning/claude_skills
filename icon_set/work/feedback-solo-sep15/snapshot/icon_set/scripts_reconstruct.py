"""Import shim so tests can reach ``scripts/reconstruct.py``.

``icon_set/scripts/`` holds runnable entry points rather than an importable
package, so the batch trace/reconstruct helpers are re-exported here for the
test suite and for any caller that wants them as a library.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent / "scripts" / "reconstruct.py"
_spec = importlib.util.spec_from_file_location("icon_set._reconstruct_impl", _SOURCE)
assert _spec and _spec.loader
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

TOLERANCE = _module.TOLERANCE
WORK = _module.WORK
slug_of = _module.slug_of
trace_one = _module.trace_one
main = _module.main
_base_slug = _module._base_slug
_fidelity = _module._fidelity
_match = _module._match
_sources = _module._sources
