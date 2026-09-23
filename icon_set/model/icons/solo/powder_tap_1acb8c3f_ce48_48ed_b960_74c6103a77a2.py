"""A circular powder compact with a curved diagonal division inside.

Symbol plan: No useful exact Lucide match; circles and one smooth divided inner disk come from the supplied reference.
Envelope: CIRCLE. The enclosing circular rim is the dominant silhouette, centered at (24,24) with radius 20 on the centerline.
Reduction: No defining features omitted; inner disk reduced to give the outer ring breathing room.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '1acb8c3f-ce48-48ed-b960-74c6103a77a2'
SOURCE_PATH = 'icon_set/work/todo-references/powder tap_1acb8c3f-ce48-48ed-b960-74c6103a77a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'powder-tap'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('powder', 'tap')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.circle('rim',24,24,20)
        # 6-8-10 triangle gives exact seam endpoints on the inner disk.
        self.add_arc('disk-upper',(16,30),(32,18),radius_x=10)
        self.add_arc('disk-lower',(32,18),(16,30),radius_x=10)
        self.add_contour('disk','disk-upper','disk-lower',closed=True)
        self.add_bezier('powder-seam',(16,30),((20,23),(26,18),(32,18)))
        self.relate('connect','powder-seam','disk')

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
