"""Standing Mallard with Broad Folded Wing
Plan: Left-facing mallard with curved neck, low broad body, raised tail and two legs.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Small eye and interior wing seam omitted; neck widened to preserve clear space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4faa8230-f0d7-4bab-b7dd-436d8fca34ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mallard_4faa8230-f0d7-4bab-b7dd-436d8fca34ee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-mallard-with-broad-folded-wing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('mallard', 'duck', 'bird', 'wing', 'bill', 'legs', 'waterfowl')

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
        path('mallard',(6,16),[('L',(14,12)),('C',(22,6),(14,6),(18,6)),('C',(30,14),(30,6),(30,10)),('L',(28,26)),('L',(42,27)),('C',(32,36),(39,32),(36,36)),('L',(22,36)),('C',(13,27),(14,36),(10,32)),('L',(17,20)),('C',(6,16),(20,16),(10,17))],True)
        for x in (22,32):self.add_line(f'leg-{x}',(x,36),(x,42));self.relate('connect',f'leg-{x}','mallard')
