"""A prescription sheet carries an Rx mark and a text rule.
Symbol plan: Portrait sheet; geometric R bowl with 8-unit bar spacing; explicit shared crossing at (26,25) for Rx; one lower text rule.
Keyshape visible bounds: (6, 2, 42, 46).
Construction references: Supplied reference: Rx and text on a rounded prescription page; Lucide file-text: page enclosure and text rule..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0b1e330-cc81-522c-9a29-44fd4f8881cf'
SOURCE_PATH = 'pictographic-primitives/health/prescription drug paper_e0b1e330-cc81-522c-9a29-44fd4f8881cf.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'prescription-drug-paper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('prescription', 'drug', 'paper')
    def build(self):
        self.box('paper',8,4,40,44,4)
        # R is a continuous stroke; X is made from two diagonals meeting at (26,25).
        self.add_line('r-stem',(17,25),(17,13))
        self.add_line('r-top',(17,13),(22,13))
        self.add_arc('r-bowl',(22,13),(22,21),radius_x=4)
        self.add_line('r-return',(22,21),(17,21))
        self.add_contour('r','r-stem','r-top','r-bowl','r-return')
        self.add_polyline('r-leg',(22,21),(26,25),(28,27))
        self.add_polyline('x-cross',(30,21),(26,25),(24,27))
        self.relate('connect','r','r-leg')
        self.relate('connect','r-leg','x-cross')
        self.add_line('text',(17,35),(31,35))

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
