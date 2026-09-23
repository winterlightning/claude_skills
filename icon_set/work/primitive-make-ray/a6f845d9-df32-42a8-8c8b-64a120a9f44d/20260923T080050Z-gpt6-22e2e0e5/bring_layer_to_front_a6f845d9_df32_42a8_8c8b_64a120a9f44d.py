"""A solid lower layer rises toward a four-corner ghost square.

Symbol plan: one rounded lower square, four symmetric upper corner marks,
and a right-side curved arrow with a common tip. Lucide bring-to-front
informed the separated corner treatment; the upward sweep is directional.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a6f845d9-df32-42a8-8c8b-64a120a9f44d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/move to top_a6f845d9-df32-42a8-8c8b-64a120a9f44d.svg"
AUTHOR = "gpt-6"


class BringLayerToFront(Solo48):
    icon_id = "bring-layer-to-front"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "editing/layers"
    aliases = ("move to top", "raise layer")
    keywords = ("arrow", "square", "front", "order")

    def build(self) -> None:
        left, right, top, bottom, arm = 8, 23, 4, 19, 3
        self.add_polyline("ghost-nw", (left, top + arm), (left, top), (left + arm, top))
        self.add_polyline("ghost-ne", (right - arm, top), (right, top), (right, top + arm))
        self.add_polyline("ghost-se", (right, bottom - arm), (right, bottom), (right - arm, bottom))
        self.add_polyline("ghost-sw", (left + arm, bottom), (left, bottom), (left, bottom - arm))

        r = 3
        self.add_line("lower-top", (11, 29), (20, 29))
        self.add_arc("lower-ne", (20, 29), (23, 32), radius_x=r, sweep=True)
        self.add_line("lower-right", (23, 32), (23, 41))
        self.add_arc("lower-se", (23, 41), (20, 44), radius_x=r, sweep=True)
        self.add_line("lower-bottom", (20, 44), (11, 44))
        self.add_arc("lower-sw", (11, 44), (8, 41), radius_x=r, sweep=True)
        self.add_line("lower-left", (8, 41), (8, 32))
        self.add_arc("lower-nw", (8, 32), (11, 29), radius_x=r, sweep=True)
        self.add_contour("lower-square", "lower-top", "lower-ne", "lower-right", "lower-se", "lower-bottom", "lower-sw", "lower-left", "lower-nw", closed=True)

        self.add_bezier(
            "rising-arrow", (33, 44),
            ((38, 37), (40, 31), (40, 25)),
            ((40, 17), (36, 11), (32, 7)),
        )
        self.add_line("arrow-head-upper", (32, 7), (40, 11))
        self.add_line("arrow-head-lower", (32, 7), (34, 18))
        self.relate("connect", "rising-arrow", "arrow-head-upper")
        self.relate("connect", "rising-arrow", "arrow-head-lower")
