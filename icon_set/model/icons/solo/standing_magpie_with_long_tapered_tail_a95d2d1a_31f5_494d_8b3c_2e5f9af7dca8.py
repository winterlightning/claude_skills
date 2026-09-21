"""Standing Magpie with Long Tapered Tail
Plan: Directional bird with sloping back, tail, breast and paired feet.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bird: sloping silhouette, rounded breast and folded wing.
Reduction: Interior wing seam omitted after near-parallel spacing review; directional silhouette and two feet retained.  Tiny eye omitted; leg bends normalized for native clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a95d2d1a-31f5-494d-8b3c-2e5f9af7dca8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/magpie_a95d2d1a-31f5-494d-8b3c-2e5f9af7dca8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-magpie-with-long-tapered-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('magpie', 'bird', 'tail', 'wing', 'beak', 'animal', 'standing')

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
        path('bird',(42,38),[('L',(26,18)),('C',(17,6),(25,10),(23,6)),('A',(8,15),9,9,False),('L',(6,17)),('L',(10,20)),('C',(16,32),(9,27),(12,30)),('C',(26,34),(20,34),(23,34)),('C',(34,31),(29,34),(31,33)),('L',(42,38))],True)
        self.add_polyline('leg-left',(26,34),(26,42),(30,42));self.add_polyline('leg-right',(16,32),(14,42),(10,42))
        self.relate('connect','leg-left','bird');self.relate('connect','leg-right','bird')
