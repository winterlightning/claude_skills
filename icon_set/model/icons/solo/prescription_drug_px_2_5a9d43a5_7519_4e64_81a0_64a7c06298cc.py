"""A prescription sheet bearing Rx.
Plan: SQUARE leaves room for a legible Rx and nine-unit margins.
Reduction: Omitted page curls and small writing lines; retained sheet and the full Rx mark.
Construction: Lucide file-text: clear document silhouette; supplied reference owns Rx construction.
Layout: Rx is intentionally asymmetric; crossing strokes share the same junction."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '5a9d43a5-7519-4e64-81a0-64a7c06298cc'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/prescription drug px 2_5a9d43a5-7519-4e64-81a0-64a7c06298cc.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'prescription-drug-px-2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('prescription', 'drug', 'px', '2')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        # SQUARE (6,6)-(42,42). A broad prescription sheet owns an enlarged Rx.
        # Tiny writing lines and the crowded paper roll are omitted.
        self.add_polyline('paper',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_polyline('r-stem',(15,31),(15,23),(15,15),(21,15))
        self.add_arc('r-bowl',(21,15),(21,23),radius_x=4)
        self.add_line('r-return',(21,23),(15,23))
        for a,b in [('r-stem','r-bowl'),('r-stem','r-return'),('r-bowl','r-return')]:self.relate('connect',a,b)
        self.add_polyline('rx-down',(21,23),(28,30),(31,33))
        self.add_polyline('rx-up',(25,33),(28,30),(32,26))
        for a,b in [('rx-down','rx-up'),('rx-down','r-bowl'),('rx-down','r-return')]:self.relate('connect',a,b)

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
