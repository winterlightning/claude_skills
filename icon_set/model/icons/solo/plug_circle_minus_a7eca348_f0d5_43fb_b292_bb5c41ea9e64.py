"""A plug in a circle with a cable curving down and right.

Symbol plan: plug: shared bowl radii and mirrored prongs; circular enclosure with cable attachment.
Envelope: CIRCLE. The enclosing circular rim is the dominant silhouette, centered at (24,24) with radius 20 on the centerline.
Reduction: No minus is visible in the supplied reference; none was invented.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = 'a7eca348-f0d5-43fb-b292-bb5c41ea9e64'
SOURCE_PATH = 'icon_set/work/todo-references/plug circle minus_a7eca348-f0d5-43fb-b292-bb5c41ea9e64.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plug-circle-minus'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('plug', 'circle', 'minus')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        # The 12-16-20 triangle supplies exact cable/rim junctions.
        self.add_arc('ring-first',(36,40),(12,8),radius_x=20)
        self.add_arc('ring-second',(12,8),(36,40),radius_x=20)
        self.add_contour('ring','ring-first','ring-second',closed=True)
        self.plug()
        self.add_bezier('cable',(24,32),((24,38),(28,40),(36,40)))
        self.relate('connect','cable','plug-bowl')
        self.relate('connect','cable','ring')

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
