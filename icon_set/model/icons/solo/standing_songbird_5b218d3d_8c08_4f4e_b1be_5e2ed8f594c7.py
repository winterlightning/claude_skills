"""Standing Songbird
Plan: Directional bird with sloping back, tail, breast and paired feet.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bird: sloping silhouette, rounded breast and folded wing.
Reduction: Interior wing seam omitted after near-parallel spacing review; directional silhouette and two feet retained.  Tiny eye omitted; leg bends normalized for native clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b218d3d-8c08-4f4e-b1be-5e2ed8f594c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wren_5b218d3d-8c08-4f4e-b1be-5e2ed8f594c7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-songbird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bird', 'wren', 'songbird', 'animal', 'wing', 'nature')

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
        path('bird',(6,38),[('L',(22,18)),('C',(31,6),(23,10),(25,6)),('A',(40,15),9,9,True),('L',(42,17)),('L',(38,20)),('C',(32,32),(39,27),(36,30)),('C',(22,34),(28,34),(25,34)),('C',(14,31),(19,34),(17,33)),('L',(6,38))],True)
        self.add_polyline('leg-left',(22,34),(22,42),(18,42));self.add_polyline('leg-right',(32,32),(34,42),(38,42))
        self.relate('connect','leg-left','bird');self.relate('connect','leg-right','bird')
