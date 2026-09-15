"""The ``container`` family: CONTAINER64 enclosures, in ``model/icons/container/``.

A container is a standalone noun in its own right and also the outer half of a
``CONTAINER_COMBINE``. Nothing inside it is reserved: draw the subject the way
the subject goes, with all the interior furniture it actually has. Whether a
given container clears a given sub icon is measured afterwards, per pair, by
the MIC check on the flattened composition -- ``compose.py`` reports it. The
protected slot that used to forbid ink in the middle 32x32 was withdrawn on
2026-09-07; ``contracts/composition-templates.v1.json`` records why.

The ``content-top-left`` / ``content-bottom-right`` anchors mark where a hosted
SUB32 child would land. They are a drafting reference, not a boundary: a
container may paint straight through them and simply not host that child.
Geometry is authored directly in 64x64 space.
"""

from __future__ import annotations

from ... import contracts
from ...keyshapes import Keyshape
from ...profiles import Profile
from ..family import FamilyIcon

PROFILE = Profile.for_family("container")
CANVAS = PROFILE.spec.canvas_size
CENTER = PROFILE.spec.center

def _content_region() -> tuple[int, int, int, int]:
    """Where a hosted SUB32 child lands, read from the composition contract.

    Derived rather than restated: the template names the child's profile and
    its position, so the region is that profile's canvas placed there.
    """
    template = contracts.composition_templates()["classes"]["CONTAINER_COMBINE"]
    content = template["children"][1]
    left, top = content["position"]
    size = Profile[content["profile"]].spec.canvas_size
    return (left, top, left + size, top + size)


#: Advisory: where a hosted child would sit. Not a rule.
CONTENT_REGION: tuple[int, int, int, int] = _content_region()


class Container64(FamilyIcon):
    family = "container"

    icon_id: str = ""
    keyshape: Keyshape = Keyshape.CIRCLE
    semantic_role: str = "MAIN"
    semantic_kind: str = "noun"
    category: str = "containers"
    aliases: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()

    def place_family_anchors(self) -> None:
        self.add_anchor("content-top-left", (CONTENT_REGION[0], CONTENT_REGION[1]))
        self.add_anchor("content-bottom-right", (CONTENT_REGION[2], CONTENT_REGION[3]))
