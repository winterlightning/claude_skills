"""A boarding pass contains an outlined airplane with two wings.
Symbol plan: Rounded horizontal ticket and a single complete diagonal airplane contour, with deliberate corners at wings and rounded nose.
Keyshape visible bounds: (2, 6, 46, 42).
Construction references: Lucide tickets-plane: ticket enclosure; Lucide plane: coherent wing silhouette and round nose..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3911cfa6-22d7-4747-95a0-fced35ce7946'
SOURCE_PATH = 'pictographic-primitives/travel/plane boarding pass_3911cfa6-22d7-4747-95a0-fced35ce7946.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'plane-boarding-pass'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('plane', 'boarding', 'pass')
    def build(self):
        self.box('ticket',4,8,44,40,4)
        members=[]
        for prefix,points in [('body',[(16,25),(20,29),(24,27),(24,33),(28,31),(30,24),(35,21)]),('return',[(32,17),(28,19),(22,16),(19,18),(24,22),(20,24),(18,23),(16,25)])]:
            for i,(a,b) in enumerate(zip(points,points[1:])):
                name=f'plane-{prefix}-{i}';self.add_line(name,a,b);members.append(name)
            if prefix=='body':
                self.add_arc('nose',(35,21),(32,17),radius_x=3,sweep=False);members.append('nose')
        self.add_contour('plane',*members,closed=True)

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
