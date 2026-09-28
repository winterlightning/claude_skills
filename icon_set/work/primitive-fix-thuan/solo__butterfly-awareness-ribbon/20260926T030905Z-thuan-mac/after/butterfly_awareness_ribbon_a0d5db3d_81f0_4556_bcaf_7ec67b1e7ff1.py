"""A butterfly awareness ribbon (Down syndrome awareness): an awareness ribbon between two
open butterfly wings.

Symbol plan: mirrored about x=24. The ribbon is two straight strands along (+-4,8) that
cross at X=(24,32): each runs from its tail at y=40 up through X to a loop side at y=24,
and a smooth cubic loop (tangent to the strands, crest at y=17) joins the two strands over
the top. Each wing is an open cubic run like the reference: from its upper end beside the loop it
arcs up over the top corner (y=8) and down to the side extreme, comes back in to a notch at the waist, swells out again in a
smaller lower lobe and ends pointing back toward the ribbon, clear of it by 8+.
Lucide construction: 'ribbon' - two crossing strands with a rounded loop;
'butterfly' - wings as open lobed curves.
Keyshape HRECT_L: centerline x 4..44 (wing extremes), y 8..40 (wing tops, tails).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a0d5db3d-81f0-4556-bcaf-7ec67b1e7ff1"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__butterfly-awareness-ribbon/20260926T030905Z-thuan-mac/reference/down syndrome butterfly ribbin_a0d5db3d-81f0-4556-bcaf-7ec67b1e7ff1.svg"
AUTHOR = "claude-opus-5-5"


class ButterflyAwarenessRibbon(Solo48):
    icon_id = "butterfly-awareness-ribbon"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health/awareness"
    aliases = ("down-syndrome-butterfly-ribbon", "awareness-ribbon-butterfly", "butterfly-ribbon")
    keywords = ("awareness", "ribbon", "butterfly", "down-syndrome", "support", "cause", "charity", "health")

    def build(self) -> None:
        m = lambda p: (48 - p[0], p[1])
        # ribbon: strands cross at X=(24,32); loop joins their upper ends
        self.add_line("strand-rising", (20, 40), (28, 24))
        self.add_bezier("loop", (28, 24), ((29, 22), (27.5, 17), (24, 17)),
                        ((20.5, 17), (19, 22), (20, 24)))
        self.add_line("strand-falling", (20, 24), (28, 40))
        self.add_contour("ribbon", "strand-rising", "loop", "strand-falling")
        # wings: open lobed curves
        for side, f in (("left", lambda p: p), ("right", m)):
            self.add_bezier(f"wing-{side}", f((18, 10)),
                            (f((17, 8.5)), f((14.5, 8)), f((12, 8))),
                            (f((7, 8)), f((4, 11.5)), f((4, 16))),
                            (f((4, 20)), f((6, 24)), f((9, 25))),
                            (f((6.5, 26)), f((4, 28.5)), f((4, 32))),
                            (f((4, 35.5)), f((7, 38)), f((11, 38))))
