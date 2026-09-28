"""A mobile phone displays a round bug with six legs.
Symbol plan: Rounded vertical phone with footer; bug circle and mirrored paired legs about x=24.
Keyshape visible bounds: (6, 2, 42, 46).
Construction references: Lucide smartphone: rounded enclosure; supplied reference: bug, divider and six legs..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '600bc5a2-131a-4e43-b134-f5e672684c21'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone bug_600bc5a2-131a-4e43-b134-f5e672684c21.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'mobile-phone-bug'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('mobile', 'phone', 'bug')
    def build(self):
        self.box('phone',8,4,40,44,4)
        self.add_line('footer',(8,36),(40,36))
        self.relate('connect','phone','footer')
        cx,cy,r=24,20,5
        self.circle('bug',cx,cy,r)
        for side in [-1,1]:
            x=cx+side*r
            for name,y in [('upper',13),('lower',27)]:
                part=f'leg-{side}-{name}'
                self.add_line(part,(x,cy),(cx+side*7,y))
                self.relate('connect','bug',part)
            self.relate('connect',f'leg-{side}-upper',f'leg-{side}-lower')
        self.add_line('bug-crossbar',(17,20),(19,20))
        self.add_line('bug-right',(29,20),(31,20))
        for part in ['bug-crossbar','bug-right']:
            self.relate('connect','bug',part)
        for side,bar in [(-1,'bug-crossbar'),(1,'bug-right')]:
            for leg in ['upper','lower']:
                self.relate('connect',bar,f'leg-{side}-{leg}')

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
