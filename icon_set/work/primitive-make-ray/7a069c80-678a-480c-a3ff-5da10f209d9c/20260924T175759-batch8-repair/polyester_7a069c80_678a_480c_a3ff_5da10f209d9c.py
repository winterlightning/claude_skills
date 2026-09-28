"""A polyester sheet with a woven grid.
Plan: SQUARE fits the clipped-corner sheet and centered grid.
Reduction: Reduced three strands per direction to two; omitted the crowded inner fold crease while retaining the clipped corner.
Construction: Lucide file-text: one clear sheet outline around sparse content.
Layout: Orthogonal grid uses shared strand spacing and actual crossing nodes; clipped corner is intentionally asymmetric."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7a069c80-678a-480c-a3ff-5da10f209d9c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/polyester_7a069c80-678a-480c-a3ff-5da10f209d9c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'polyester'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('polyester',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_polyline('sheet',(30,6),(10,6),(6,10),(6,38),(10,42),(38,42),(42,38),(42,18),(30,6))
        xs=(16,26); ys=(22,32)
        for i,x in enumerate(xs): self.add_polyline(f'vertical-{i}',(x,20),*((x,y) for y in ys),(x,34))
        for j,y in enumerate(ys):
            self.add_polyline(f'horizontal-{j}',(14,y),*((x,y) for x in xs),(32,y))
            for i in range(2): self.relate('connect',f'vertical-{i}',f'horizontal-{j}')

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
