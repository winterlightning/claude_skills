"""The ``solo`` family: SOLO48 subjects, authored in ``model/icons/solo/``.

A solo icon is one standalone subject drawn to be read on its own. It hosts
nothing and is hosted by nothing, so the whole 48x48 canvas belongs to the
subject -- which is what makes it the right home for a traced drawing whose
proportions matter. Geometry is authored directly in 48x48 space.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ...profiles import Profile, STROKE_WIDTH
from ... import contracts
from ..family import FamilyIcon

PROFILE = Profile.for_family("solo")
CANVAS = PROFILE.spec.canvas_size
CENTER = PROFILE.spec.center

# Specialized avatar authoring uses the solo family and its geometry rules.
HEAD_BODY_INK_GAP = contracts.icon_profile()["authoring"]["avatar"]["head_body_ink_gap"]
HEAD_BODY_CENTERLINE_GAP = HEAD_BODY_INK_GAP + STROKE_WIDTH


class Solo48(FamilyIcon):
    family = "solo"

    icon_id: str = ""
    keyshape: Keyshape = Keyshape.SQUARE
    semantic_role: str = "MAIN"
    semantic_kind: str = "noun"
    category: str = "objects"
    aliases: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()
