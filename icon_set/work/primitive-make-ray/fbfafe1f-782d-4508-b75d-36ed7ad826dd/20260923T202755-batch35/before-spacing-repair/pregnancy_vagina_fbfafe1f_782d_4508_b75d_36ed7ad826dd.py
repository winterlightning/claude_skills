"""A lower female torso with a heart-shaped pelvic symbol.

Symbol plan: heart: paired lobes and pointed base; human reference consulted for simple balanced anatomy.
Envelope: VRECT_L; derive its bounds from Keyshape.bounds_for(Profile.SOLO48).
Reduction: No defining features omitted; this is a torso fragment, with no head or detached gap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fbfafe1f-782d-4508-b75d-36ed7ad826dd'
SOURCE_PATH = 'icon_set/work/todo-references/pregnancy vagina_fbfafe1f-782d-4508-b75d-36ed7ad826dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pregnancy-vagina'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('pregnancy', 'vagina')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        axis=24
        for side,sign in [('left',1),('right',-1)]:
            def p(x,y): return (axis+sign*(x-axis),y)
            self.add_bezier('body-'+side,p(12,4),(p(18,19),p(8,21),p(8,33)),(p(8,38),p(9,42),p(11,44)))
        self.add_bezier('heart-left',(24,27),((18,20),(12,25),(17,31)),((19,33),(22,36),(24,38)))
        self.add_bezier('heart-right',(24,38),((26,36),(29,33),(31,31)),((36,25),(30,20),(24,27)))
        self.add_contour('heart','heart-left','heart-right',closed=True)
        self.add_line('pelvic-line',(24,38),(24,44))
        self.relate('connect','heart','pelvic-line')

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
