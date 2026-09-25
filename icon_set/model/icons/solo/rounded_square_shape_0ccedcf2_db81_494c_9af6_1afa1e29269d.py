"""One plain rounded square outline.

SQUARE extrema (6,6)-(42,42). All four radius-4 corners share one repeat
definition. Lucide square confirms tangent straight/quarter-arc joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "0ccedcf2-db81-494c-9af6-1afa1e29269d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/cracker_0ccedcf2-db81-494c-9af6-1afa1e29269d.svg"
AUTHOR = "gpt-6"


class RoundedSquareShape(Solo48):
    icon_id = "rounded-square-shape-solo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("round-corner square", "plain square")
    keywords = ("shape", "outline", "rectangle", "frame")

    def build(self) -> None:
        p=[(10,6),(38,6),(42,10),(42,38),(38,42),(10,42),(6,38),(6,10),(10,6)]
        parts=[]
        for i,(a,b) in enumerate(zip(p,p[1:])):
            name=f"edge-{i}"
            if i%2:self.add_arc(name,a,b,radius_x=4,radius_y=4,sweep=True)
            else:self.add_line(name,a,b)
            parts.append(name)
        self.add_contour("square",*parts,closed=True)
