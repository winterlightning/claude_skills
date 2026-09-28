"""A plane flies within circular return arrows.
Symbol plan: Circle radius 20 with opposite tangent arrowheads; a deliberately diagonal plane gesture retains the swept wing and rounded tail.
Keyshape visible bounds: (2, 2, 46, 46).
Construction references: Lucide plane: swept wing direction; supplied reference: circular arrows and open plane gesture..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
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
        # Exact circle nodes (12,16,20 triangle) and open arrow tips avoid pinched closed loops.
        self.add_arc('orbit-top',(4,24),(24,4),radius_x=20)
        self.add_arc('orbit-top-end',(24,4),(40,12),radius_x=20)
        self.add_contour('upper-orbit','orbit-top','orbit-top-end')
        self.add_arc('orbit-bottom',(44,24),(24,44),radius_x=20)
        self.add_arc('orbit-bottom-end',(24,44),(8,36),radius_x=20)
        self.add_contour('lower-orbit','orbit-bottom','orbit-bottom-end')
        self.add_polyline('left-arrow',(8,18),(4,24),(9,27));self.relate('connect','upper-orbit','left-arrow')
        self.add_polyline('right-arrow',(40,30),(44,24),(39,21));self.relate('connect','lower-orbit','right-arrow')
        self.add_bezier('plane-tail',(18,27),((20,29),(20,31),(23,29)))
        self.add_polyline('plane-body',(23,29),(26,26),(30,22))
        self.relate('connect','plane-tail','plane-body')
        self.add_line('plane-wing',(18,18),(26,26));self.relate('connect','plane-body','plane-wing')


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
