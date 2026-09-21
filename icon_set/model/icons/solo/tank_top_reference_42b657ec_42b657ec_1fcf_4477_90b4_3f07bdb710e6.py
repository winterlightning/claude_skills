"""Tank Top
Plan: Broad straps, rounded neckline, curved armholes and flat hem.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide shirt: continuous garment outline.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42b657ec-1fcf-4477-90b4-3f07bdb710e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/top_42b657ec-1fcf-4477-90b4-3f07bdb710e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tank-top-reference-42b657ec'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tank', 'top', 'shirt', 'clothing', 'sleeveless', 'garment', 'fashion', 'straps')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('top',(6,25),[('C',(10,17),(10,22),(10,19)),('L',(10,6)),('L',(18,6)),('L',(18,13)),('A',(30,13),6,6,False),('L',(30,6)),('L',(38,6)),('L',(38,17)),('C',(42,25),(38,19),(38,22)),('L',(42,42)),('L',(6,42)),('L',(6,25))],True)
