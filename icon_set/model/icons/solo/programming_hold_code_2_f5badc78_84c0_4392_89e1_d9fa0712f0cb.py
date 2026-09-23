"""Two cupped hands holding angle brackets and a code slash.

Symbol plan: code: matching opposing chevrons; hand: coherent palm/finger outlines; human reference consulted.
Envelope: SQUARE. The complete composition has a square overall envelope and uses the (6,6)–(42,42) centerline extremes.
Reduction: Small thumb creases omitted; code punctuation and both hands retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = 'f5badc78-84c0-4392-89e1-d9fa0712f0cb'
SOURCE_PATH = 'icon_set/work/todo-references/programming hold code 2_f5badc78-84c0-4392-89e1-d9fa0712f0cb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'programming-hold-code-2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('programming', 'hold', 'code', '2')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        axis=24
        self.add_polyline('code-left',(12,6),(6,12),(12,18))
        self.add_polyline('code-right',(36,6),(42,12),(36,18))
        self.add_line('code-slash',(26,6),(22,18))
        for side,sign in [('left',1),('right',-1)]:
            def p(x,y): return (axis+sign*(x-axis),y)
            self.add_bezier('hand-'+side,p(12,42),(p(12,38),p(6,36),p(6,33)),(p(6,31),p(6,30),p(6,29)),(p(6,26),p(10,26),p(10,29)))
            self.add_line('finger-'+side,p(10,29),p(10,34))
            self.add_bezier('palm-'+side,p(10,34),(p(10,31),p(12,30),p(14,32)),(p(16,34),p(20,36),p(20,39)),(p(20,40),p(20,41),p(20,42)))
            self.add_contour('cupped-'+side,'hand-'+side,'finger-'+side,'palm-'+side)

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
