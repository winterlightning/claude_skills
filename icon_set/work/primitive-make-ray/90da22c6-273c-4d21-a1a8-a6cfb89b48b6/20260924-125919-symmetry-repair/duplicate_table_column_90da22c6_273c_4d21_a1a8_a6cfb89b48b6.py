"""Two matching three-cell columns with two directional copy arrows.
Plan: HRECT_L extremes (4,8)-(44,40); shared column width and rows;
repeat arrows about y=24, intentionally rightward. Lucide table-columns-split
informs the repeated divider construction. All reference parts retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "90da22c6-273c-4d21-a1a8-a6cfb89b48b6"
SOURCE_PATH = "pictographic-primitives/_uncategorized_16/duplicate column_90da22c6-273c-4d21-a1a8-a6cfb89b48b6.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "duplicate-table-column"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "data/tables"
    aliases = ("duplicate column",)
    keywords = ("copy", "column", "table")
    def build(self):
        width=8
        for name,x in (("source",4),("copy",36)):
            self.add_polyline(name,(x,8),(x+width,8),(x+width,40),(x,40),closed=True)
            for y in (19,29):
                n=f"{name}-row-{y}"
                self.add_line(n,(x,y),(x+width,y))
                self.relate("connect",name,n)
        for y in (16,32):
            n=f"arrow-{y}"
            self.add_line(n,(20,y),(28,y))
            self.add_polyline(n+"-head",(24,y-4),(28,y),(24,y+4))
            self.relate("connect",n,n+"-head")
