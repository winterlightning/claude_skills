"""A plug mounted inside a tall rounded rectangle, with its cable exiting below.

Symbol plan: plug: equal pins and a semicircular lower bowl.
Envelope: VRECT_M; derive its bounds from Keyshape.bounds_for(Profile.SOLO48).
Reduction: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0ef960fc-1a4e-4b67-9b67-283cc8cc1cf3'
SOURCE_PATH = 'icon_set/work/todo-references/plugin_0ef960fc-1a4e-4b67-9b67-283cc8cc1cf3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plugin'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('plugin',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_line('frame-top',(16,4),(32,4))
        self.add_arc('frame-tr',(32,4),(38,10),radius_x=6)
        self.add_line('frame-right',(38,10),(38,34))
        self.add_arc('frame-br',(38,34),(32,40),radius_x=6)
        self.add_polyline('frame-bottom',(32,40),(24,40),(16,40))
        self.add_arc('frame-bl',(16,40),(10,34),radius_x=6)
        self.add_line('frame-left',(10,34),(10,10))
        self.add_arc('frame-tl',(10,10),(16,4),radius_x=6)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br','frame-bottom-1','frame-bottom-2','frame-bl','frame-left','frame-tl',closed=True)
        self.plug(top=20,bottom=31)
        self.add_polyline('cable',(24,31),(24,40),(24,44))
        self.relate('connect','cable','plug-bowl')
        self.relate('connect','cable','frame')

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
