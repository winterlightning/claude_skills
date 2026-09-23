"""A plug inside an open circle with a lower-right cancellation cross.

Symbol plan: plug: bowl and equal prongs; code: matched diagonal strokes.
Envelope: SQUARE; derive its bounds from Keyshape.bounds_for(Profile.SOLO48).
Reduction: No defining features omitted; open ring preserves room for the cross.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2fa2e764-f653-4eb6-b13a-4c6d7b198877'
SOURCE_PATH = 'icon_set/work/todo-references/plug circle xmark_2fa2e764-f653-4eb6-b13a-4c6d7b198877.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plug-circle-xmark'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('plug', 'circle', 'xmark')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_arc('ring-top',(6,24),(42,24),radius_x=18)
        self.add_arc('ring-bottom',(24,42),(6,24),radius_x=18)
        self.add_contour('ring','ring-bottom','ring-top')
        self.plug(cx=22,top=19,bottom=30)
        self.add_bezier('cable',(22,30),((22,37),(25,38),(29,38)))
        self.relate('connect','cable','plug-bowl')
        self.add_polyline('cross-down',(33,33),(37,37),(41,41))
        self.add_polyline('cross-up',(33,41),(37,37),(41,33))
        self.relate('connect','cross-down','cross-up')

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
