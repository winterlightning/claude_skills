"""Reference reconstruction: nested geometry owned by the outer silhouette.
Square keyshape preserves balanced proportions; hexagon uses HRECT_L.
Lucide panels-top-left informs tangent corner construction; reference supplies
part count and relative placement. Repeated loops share one parameterized owner.
No reference details omitted. Both axes mirror except the intentional upper-left inset.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'c9953fdc-3825-4f26-8597-533126256825'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/remote access_c9953fdc-3825-4f26-8597-533126256825.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'double-hexagon-with-center-circle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Double Hexagon with Center Circle',)
    keywords = ('double', 'hexagon', 'with', 'center', 'circle')

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
        for name,points in (("outer",[(4,24),(14,8),(34,8),(44,24),(34,40),(14,40)]),("inner",[(14,24),(19,16),(29,16),(34,24),(29,32),(19,32)])):
            self.add_polyline(name,*points,closed=True)
        self.add_arc("center-a",(22,24),(26,24),radius_x=2)
        self.add_arc("center-b",(26,24),(22,24),radius_x=2)
        self.add_contour("center","center-a","center-b",closed=True)
