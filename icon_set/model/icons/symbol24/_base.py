"""The ``symbol24`` family: SYMBOL24 symbols, authored in ``model/icons/symbol24/``.

A 24x24 symbol with the library's uniform 4-unit stroke. It is drawn fresh or
redrawn from a 32x32 sub or symbol (``icon_set/scripts/symbol24.py from32``
writes a mechanical 3/4 draft that must then be repaired on this grid). Every
coordinate ends up authored directly in final 24x24 space; the stroke never
scales, so a 32 drawing's gaps shrink and have to be rebalanced, not accepted.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ...profiles import Profile
from ..family import FamilyIcon

PROFILE = Profile.for_family("symbol24")
CANVAS = PROFILE.spec.canvas_size
CENTER = PROFILE.spec.center


class Symbol24(FamilyIcon):
    family = "symbol24"

    icon_id: str = ""
    keyshape: Keyshape = Keyshape.SQUARE
    semantic_role: str = "SUB"
    semantic_kind: str = "modifier"
    category: str = "primitives/mark"
    aliases: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()
