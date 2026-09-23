"""A five-point star floating over an award podium.

Symbol plan: star: alternating tips and valleys; consistent podium support spacing.
Envelope: VRECT_L. The upright composition benefits from the 32-by-40 centerline envelope, (8,4)–(40,44).
Reduction: Thin doubled podium rim reduced to one rail to preserve the star-to-platform gap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e768495f-4a83-4777-ba0c-6d66e88b98d4'
SOURCE_PATH = 'icon_set/work/todo-references/podium star_e768495f-4a83-4777-ba0c-6d66e88b98d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'podium-star'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('podium', 'star')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        axis=24
        left=[(24,4),(20,11),(12,12),(18,18),(16,24),(24,20)]
        right=[(2*axis-x,y) for x,y in reversed(left[1:-1])]
        self.add_polyline('star',*left,*right,closed=True)
        self.add_polyline('platform',(8,32),(12,32),(36,32),(40,32))
        self.add_polyline('baseline',(8,44),(12,44),(36,44),(40,44))
        for name,x in [('left',12),('right',36)]:
            self.add_line('post-'+name,(x,32),(x,44))
            self.relate('connect','post-'+name,'platform')
            self.relate('connect','post-'+name,'baseline')

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
