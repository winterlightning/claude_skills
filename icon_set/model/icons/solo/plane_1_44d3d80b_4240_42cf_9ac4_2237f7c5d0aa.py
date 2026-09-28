"""A plane flies within circular return arrows.
Symbol plan: Circle radius 20 with opposite tangent arrowheads; a deliberately diagonal plane gesture retains the swept wing and rounded tail.
Keyshape visible bounds: (2, 2, 46, 46).
Construction references: Lucide plane: swept wing direction; supplied reference: circular arrows and open plane gesture..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44d3d80b-4240-42cf-9ac4-2237f7c5d0aa'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_44d3d80b-4240-42cf-9ac4-2237f7c5d0aa.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'plane-1-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('plane', '1')
    def build(self):
        cx,cy,r=24,24,20
        self.add_arc('orbit-top',(4,24),(44,24),radius_x=r)
        self.add_arc('orbit-bottom',(44,24),(4,24),radius_x=r)
        self.add_contour('orbit','orbit-top','orbit-bottom',closed=True)
        self.add_polyline('left-arrow',(8,16),(4,24),(8,24))
        self.add_polyline('right-arrow',(40,24),(44,24),(40,32))
        self.relate('connect','orbit','left-arrow')
        self.relate('connect','orbit','right-arrow')
        self.add_bezier('plane-tail',(16,25),((17,28),(19,30),(21,29)))
        self.add_line('plane-body-a',(21,29),(27,25))
        self.add_line('plane-body-b',(27,25),(32,21))
        self.add_contour('plane-body','plane-tail','plane-body-a','plane-body-b')
        self.add_line('plane-wing',(17,19),(27,25))
        self.relate('connect','plane-body','plane-wing')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
