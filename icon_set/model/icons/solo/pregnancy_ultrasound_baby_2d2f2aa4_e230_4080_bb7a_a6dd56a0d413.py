"""A fan-shaped ultrasound field containing a curled fetus.

Symbol plan: human_ref/full_body_ref.png: minimal human silhouette; source fetal pose remains a connected anatomical outline.
Envelope: HRECT_L. The broad ultrasound fan uses the 40-by-32 centerline envelope, (4,8)–(44,40).
Reduction: Tiny anatomical detail omitted; curled head and body retained as one silhouette, so no detached head gap applies.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '2d2f2aa4-e230-4080-bb7a-a6dd56a0d413'
SOURCE_PATH = 'icon_set/work/todo-references/pregnancy ultrasound baby_2d2f2aa4-e230-4080-bb7a-a6dd56a0d413.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pregnancy-ultrasound-baby'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('pregnancy', 'ultrasound', 'baby')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_line('fan-sides-1',(4,28),(24,8))
        self.add_line('fan-sides-2',(24,8),(44,28))
        self.add_arc('fan-bottom',(44,28),(4,28),radius_x=20,radius_y=12)
        self.add_contour('fan','fan-sides-1','fan-sides-2','fan-bottom',closed=True)
        self.add_bezier('fetus',(25,26),((25,20),(32,20),(32,25)),((32,32),(24,35),(19,32)),((12,29),(18,22),(22,26)),((23,27),(24,26),(25,26)))
        self.add_contour('baby','fetus',closed=True)

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
