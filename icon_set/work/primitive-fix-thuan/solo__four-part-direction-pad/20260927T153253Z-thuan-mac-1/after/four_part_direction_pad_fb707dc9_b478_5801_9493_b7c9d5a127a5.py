"""Four-part direction pad (direction button).

Symbol plan: one pentagon arm (width 8, shaft 8, 45-degree tip ending
6 units from the centre) defined once for the top and rotated by quarter
turns about (24,24). The 45-degree tip edges of neighbouring arms are
parallel and 8.5 apart on centerlines.
Revision: the rejected drawing used short, squat arms with small house
openings; the reference arms are long pointers aimed at the centre.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fb707dc9-b478-5801-9493-b7c9d5a127a5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__four-part-direction-pad/20260927T153253Z-thuan-mac-1/reference/direction button_fb707dc9-b478-5801-9493-b7c9d5a127a5.svg"
AUTHOR = "claude-opus-5-5"

ARM = ((20, 6), (28, 6), (28, 14), (24, 18), (20, 14))


def _rotate(point, turns):
    x, y = point
    for _ in range(turns):
        x, y = 48 - y, x
    return x, y


class FourPartDirectionPad(Solo48):
    icon_id = "four-part-direction-pad"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface"
    categories = ("primitives", "interface")
    aliases = ("direction button", "d-pad")
    keywords = ("direction", "pad", "arrows", "controller", "navigation", "button")

    def build(self) -> None:
        for turns, name in enumerate(("up", "right", "down", "left")):
            self.add_polyline(f"arm-{name}", *(_rotate(p, turns) for p in ARM), closed=True)
