"""The ``sub`` family: SUB32 glyphs, authored in ``model/icons/sub/``.

A sub icon is read small and hosted by others -- a verb, a state, a modifier,
or a simple noun shape that works as content. Its 32x32 canvas is exactly the
CONTAINER_COMBINE slot. Every coordinate is authored directly in final 32x32
space, backwards from the keyshape's four extreme values; nothing scales.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ...profiles import Profile
from ..family import FamilyIcon

PROFILE = Profile.for_family("sub")
CANVAS = PROFILE.spec.canvas_size
CENTER = PROFILE.spec.center


class Sub32(FamilyIcon):
    family = "sub"

    icon_id: str = ""
    keyshape: Keyshape = Keyshape.SQUARE
    semantic_role: str = "SUB"
    semantic_kind: str = "modifier"
    category: str = "primitives/mark"
    aliases: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()
