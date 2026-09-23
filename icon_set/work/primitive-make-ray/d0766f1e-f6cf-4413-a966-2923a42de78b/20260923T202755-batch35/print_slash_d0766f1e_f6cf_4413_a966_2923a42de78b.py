"""A printer and output sheet crossed by a diagonal slash.

Symbol plan: printer: nested input sheet, rounded housing and output sheet; slash keeps the input direction.
Envelope: SQUARE. The complete composition has a square overall envelope and uses the (6,6)–(42,42) centerline extremes.
Reduction: Tiny status indicator omitted, as it is absent from the supplied drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd0766f1e-f6cf-4413-a966-2923a42de78b'
SOURCE_PATH = 'icon_set/work/todo-references/print slash_d0766f1e-f6cf-4413-a966-2923a42de78b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'print-slash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('print', 'slash')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.rounded('printer',6,14,42,34,5)
        self.add_polyline('input-paper',(14,14),(14,6),(34,6),(34,14))
        self.relate('connect','input-paper','printer')
        self.rounded('output-paper',14,26,34,42,3)
        self.add_line('disabled-slash',(6,42),(42,6))

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
