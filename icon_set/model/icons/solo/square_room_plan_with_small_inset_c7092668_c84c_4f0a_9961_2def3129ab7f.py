"""Reference reconstruction: nested geometry owned by the outer silhouette.
SQUARE keyshape preserves the square reference proportions.
Lucide panels-top-left informs tangent corner construction; reference supplies
part count and relative placement. Repeated loops share one parameterized owner.
No reference details omitted. Both axes mirror except the intentional upper-left inset.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'c7092668-c84c-4f0a-9961-2def3129ab7f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/room_c7092668-c84c-4f0a-9961-2def3129ab7f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'square-room-plan-with-small-inset'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Small Square Inside Larger Square',)
    keywords = ('room', 'plan', 'square', 'inset', 'layout', 'outline')

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
        self.rounded("room",(6,6),(42,42),3)
        self.add_polyline("inset",(15,15),(23,15),(23,23),(15,23),closed=True)
