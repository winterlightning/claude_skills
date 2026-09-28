"""A document with a clipped corner contains a clock face.
Symbol plan: Portrait document, clipped upper-right corner, centered clock circle with two joined hands.
Keyshape visible bounds: (6, 2, 42, 46).
Construction references: Lucide file-clock: clock hands and document silhouette; supplied reference: full clock enclosed within page..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e7ce785e-158f-41d6-9e8b-dcba4879acac'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock file 1_e7ce785e-158f-41d6-9e8b-dcba4879acac.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'time-clock-file-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('time', 'clock', 'file', '1')
    def build(self):
        self.add_polyline('file',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        self.circle('clock',24,26,10)
        self.add_polyline('hands',(24,21),(24,26),(28,30))

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
