"""Rounded page frame with top and bottom bands and three middle columns.

SQUARE extrema (6,6)-(42,42). Shared y=18/30 rails and x=18/30 columns
keep the grid equal. Lucide panels-top-left informed attached dividers.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8682d8fb-fe47-4e03-93f3-3235fb5083ee"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/composition layout_8682d8fb-fe47-4e03-93f3-3235fb5083ee.svg"
AUTHOR = "gpt-6"


class ThreeColumnGridInterfaceLayout(Solo48):
    icon_id = "three-column-grid-interface-layout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design/layouts"
    aliases = ("three column interface", "page grid")
    keywords = ("columns", "rows", "layout", "webpage")

    def build(self) -> None:
        pts = [(9,6),(39,6),(42,9),(42,18),(42,30),(42,39),(39,42),(9,42),(6,39),(6,30),(6,18),(6,9),(9,6)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            name=f"frame-{i}"
            if i in (1,5,7,11):
                self.add_arc(name,a,b,radius_x=3,radius_y=3,sweep=True)
            else:
                self.add_line(name,a,b)
            members.append(name)
        self.add_contour("frame",*members,closed=True)
        for name,y in (("upper-rail",18),("lower-rail",30)):
            self.add_line(name,(6,y),(42,y))
            self.relate("connect",name,"frame")
        for name,x in (("column-left",18),("column-right",30)):
            self.add_line(name,(x,18),(x,30))
            self.relate("connect",name,"upper-rail")
            self.relate("connect",name,"lower-rail")
