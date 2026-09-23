"""A CSS3 shield bearing the angular numeral three.

Symbol plan: shield: bilateral tapered enclosure; digit reconstructed by hand from the supplied CSS logo.
Envelope: SQUARE. The complete composition has a square overall envelope and uses the (6,6)–(42,42) centerline extremes.
Reduction: No defining features omitted; diagonal numeral is deliberately asymmetric.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = 'e2d37e28-a199-438d-9557-6d0ac7e39107'
SOURCE_PATH = 'icon_set/work/todo-references/programming language css 3_e2d37e28-a199-438d-9557-6d0ac7e39107.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'programming-language-css-3'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('programming', 'language', 'css', '3')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        axis=24
        self.add_polyline('shield',(6,6),(42,6),(38,37),(24,42),(10,37),closed=True)
        self.add_polyline('three',(16,15),(32,15),(22,24),(30,24),(28,31),(24,33),(18,31),(17,27))

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
