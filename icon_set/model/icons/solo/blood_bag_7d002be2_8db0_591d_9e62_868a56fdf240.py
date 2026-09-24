"""A blood collection bag has a top cap, blood drop and curved outlet tube.
Symbol plan: Rounded bag with centered rounded rectangular cap; mirrored drop around x=24; short curved tube exits from the base and turns right.
Keyshape visible bounds: (8, 2, 40, 46).
Construction references: Lucide droplet: pointed crown and rounded bottom; supplied reference: capped rounded bag and curved outlet..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d002be2-8db0-591d-9e62-868a56fdf240'
SOURCE_PATH = 'pictographic-primitives/health/blood bag_7d002be2-8db0-591d-9e62-868a56fdf240.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'blood-bag-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('blood', 'bag')
    def build(self):
        self.box('bag',10,12,38,39,4)
        self.add_line('cap-left',(20,12),(20,6))
        self.add_arc('cap-tl',(20,6),(22,4),radius_x=2)
        self.add_line('cap-top',(22,4),(26,4))
        self.add_arc('cap-tr',(26,4),(28,6),radius_x=2)
        self.add_line('cap-right',(28,6),(28,12))
        self.add_contour('cap','cap-left','cap-tl','cap-top','cap-tr','cap-right')
        self.relate('connect','bag','cap')
        # Bilaterally symmetric blood drop, one pointed crown and a round lower bowl.
        self.add_bezier('drop-left',(24,21),((22,23),(20,24),(20,26)))
        self.add_arc('drop-bottom',(20,26),(28,26),radius_x=4,sweep=False)
        self.add_bezier('drop-right',(28,26),((28,24),(26,23),(24,21)))
        self.add_contour('drop','drop-left','drop-bottom','drop-right',closed=True)
        self.add_arc('tube',(24,39),(29,44),radius_x=5,sweep=False)
        self.relate('connect','bag','tube')

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
