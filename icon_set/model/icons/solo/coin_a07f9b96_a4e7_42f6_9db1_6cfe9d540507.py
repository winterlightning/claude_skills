"""A round coin bears an S-shaped dollar mark.
Symbol plan: Circular rim centered at 24; one smooth S stroke with real top and bottom attachment nodes for currency ticks.
Keyshape visible bounds: (2, 2, 46, 46).
Construction references: Lucide coins: round coin outline; supplied reference: flowing S and separate short currency extensions..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a07f9b96-a4e7-42f6-9db1-6cfe9d540507'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_12/coin_a07f9b96-a4e7-42f6-9db1-6cfe9d540507.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'coin'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('coin',)
    def build(self):
        self.circle('coin',24,24,20)
        self.add_bezier('dollar-top',(29,18),((29,16),(27,15),(24,15)))
        self.add_bezier('dollar-upper',(24,15),((20,15),(18,17),(18,20)),((18,23),(21,23),(24,24)))
        self.add_bezier('dollar-lower',(24,24),((27,25),(30,25),(30,28)),((30,31),(28,33),(24,33)))
        self.add_bezier('dollar-bottom',(24,33),((21,33),(19,32),(18,30)))
        self.add_contour('dollar','dollar-top','dollar-upper','dollar-lower','dollar-bottom')
        self.add_line('top-tick',(24,13),(24,15))
        self.add_line('bottom-tick',(24,33),(24,35))
        self.relate('connect','dollar','top-tick')
        self.relate('connect','dollar','bottom-tick')

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
