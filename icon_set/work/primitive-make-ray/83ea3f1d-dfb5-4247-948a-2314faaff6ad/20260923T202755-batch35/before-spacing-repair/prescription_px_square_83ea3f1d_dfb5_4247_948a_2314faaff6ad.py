"""An Rx prescription mark inside a rounded square.

Symbol plan: Source supplies letter geometry; rounded frame follows the Lucide printer enclosure vocabulary.
Envelope: SQUARE; derive its bounds from Keyshape.bounds_for(Profile.SOLO48).
Reduction: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '83ea3f1d-dfb5-4247-948a-2314faaff6ad'
SOURCE_PATH = 'icon_set/work/todo-references/prescription px square_83ea3f1d-dfb5-4247-948a-2314faaff6ad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'prescription-px-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('prescription', 'px', 'square')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.rounded('frame',6,6,42,42,5)
        self.add_polyline('r-upright',(16,33),(16,24),(16,14),(24,14))
        self.add_arc('r-bowl',(24,14),(24,24),radius_x=5)
        self.add_line('r-return',(24,24),(16,24))
        self.relate('connect','r-upright','r-bowl')
        self.relate('connect','r-upright','r-return')
        self.relate('connect','r-bowl','r-return')
        self.add_polyline('rx-down',(24,24),(28,28),(33,33))
        self.add_polyline('rx-up',(24,32),(28,28),(32,24))
        self.relate('connect','rx-down','rx-up')
        self.relate('connect','rx-down','r-bowl')
        self.relate('connect','rx-down','r-return')

    def circle(self, name, cx, cy, r):
        points = [(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members = []
        for i, (a,b) in enumerate(zip(points, points[1:])):
            member = f"{name}-{i}"
            self.add_arc(member, a, b, radius_x=r)
            members.append(member)
        self.add_contour(name, *members, closed=True)

    def rounded(self, name, left, top, right, bottom, r):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r),(left+r,top)]
        members = []
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member = f"{name}-{i}"
            if i % 2: self.add_arc(member,a,b,radius_x=r)
            else: self.add_line(member,a,b)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def plug(self, cx=24, top=21, bottom=32):
        # Shared bowl width and mirrored prongs; cable joins bottom apex.
        r=8
        self.add_polyline('plug-top',(cx-r,top),(cx-4,top),(cx+4,top),(cx+r,top))
        self.add_line('plug-right',(cx+r,top),(cx+r,bottom-r))
        self.add_arc('plug-right-curve',(cx+r,bottom-r),(cx,bottom),radius_x=r)
        self.add_arc('plug-left-curve',(cx,bottom),(cx-r,bottom-r),radius_x=r)
        self.add_line('plug-left',(cx-r,bottom-r),(cx-r,top))
        self.add_contour('plug-bowl','plug-right','plug-right-curve','plug-left-curve','plug-left')
        self.relate('connect','plug-top','plug-bowl')
        for i,x in enumerate((cx-4,cx+4)):
            self.add_line(f'prong-{i}',(x,top-8),(x,top))
            self.relate('connect',f'prong-{i}','plug-top')
