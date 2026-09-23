"""A preferences panel joined to a half gear.

Symbol plan: settings: alternating teeth and gaps; half gear attached to a straight panel.
Envelope: VRECT_L. The upright composition benefits from the 32-by-40 centerline envelope, (8,4)–(40,44).
Reduction: No defining features omitted.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = 'fea7afa8-61b7-411c-860f-fcb3e2894cf6'
SOURCE_PATH = 'icon_set/work/todo-references/preferences_fea7afa8-61b7-411c-860f-fcb3e2894cf6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'preferences'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('preferences',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_polyline('panel',(25,4),(25,12),(25,20),(25,32),(25,36),(25,44),(8,44),(8,4),closed=True)
        for i,y in enumerate((12,28)): self.add_line(f'panel-mark-{i}',(16,y),(16,y+8))
        self.add_polyline('gear',(25,12),(29,13),(33,9),(39,15),(35,20),(40,20),(40,28),(35,28),(39,33),(33,39),(29,35),(25,36))
        self.relate('connect','gear','panel')
        self.add_arc('gear-hub',(25,20),(25,32),radius_x=6)
        self.relate('connect','gear-hub','panel')

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
