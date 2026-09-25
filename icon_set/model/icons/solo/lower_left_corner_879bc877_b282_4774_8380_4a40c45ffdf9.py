"""One open lower-left corner with a smoothly rounded bend.

SQUARE extrema (6,6)-(42,42). A vertical, quarter-circle and baseline form
one continuous stroke. Lucide scan-line informed the tangent corner join.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "879bc877-b282-4774-8380-4a40c45ffdf9"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/corner_879bc877-b282-4774-8380-4a40c45ffdf9.svg"
AUTHOR = "gpt-6"


class LowerLeftCorner(Solo48):
    icon_id = "lower-left-corner"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("rounded lower left corner", "bottom left border")
    keywords = ("angle", "outline", "border", "elbow")

    def build(self) -> None:
        self.add_line("upright",(6,6),(6,38))
        self.add_arc("bend",(6,38),(10,42),radius_x=4,radius_y=4,sweep=False)
        self.add_line("baseline",(10,42),(42,42))
        self.add_contour("corner","upright","bend","baseline")
