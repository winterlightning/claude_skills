"""Reference reconstruction: nested geometry owned by the outer silhouette.
SQUARE keyshape preserves the square reference proportions.
Lucide panels-top-left informs tangent corner construction; reference supplies
part count and relative placement. Repeated loops share one parameterized owner.
No reference details omitted. Both axes mirror except the intentional upper-left inset.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '3eb43dbe-b8a7-44bc-8374-47881eaf72c0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/shadowbox_3eb43dbe-b8a7-44bc-8374-47881eaf72c0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'rounded-shadowbox-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Double Rounded Square Frame',)
    keywords = ('frame', 'shadowbox', 'square', 'rounded', 'border', 'opening')

    def rounded(self, name, lo, hi, radius):
        x,y=lo; X,Y=hi; r=radius
        points=[(x+r,y),(X-r,y),(X,y+r),(X,Y-r),(X-r,Y),(x+r,Y),(x,Y-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"; ids.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        self.rounded("outer",(6,6),(42,42),6)
        self.rounded("inner",(15,15),(33,33),3)
