"""Standing Bird with Long Tail
Plan: Low long-tailed right-facing bird with two slanted legs.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: Lucide bird: coherent bird outline.
Reduction: Interior wing and tiny eye omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a2b5aa4-d388-4132-a05e-c3c916be6c08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blackbird_2a2b5aa4-d388-4132-a05e-c3c916be6c08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-bird-with-long-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bird', 'songbird', 'tail', 'beak', 'wing', 'standing', 'wildlife')

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
        path('bird',(6,34),[('L',(25,15)),('C',(34,6),(27,10),(29,6)),('L',(42,12)),('L',(38,17)),('C',(26,32),(38,26),(33,31)),('L',(12,34)),('L',(6,34))],True)
        self.add_polyline('leg-a',(12,34),(16,42),(20,42));self.add_polyline('leg-b',(26,32),(34,42),(40,42));self.relate('connect','leg-a','bird');self.relate('connect','leg-b','bird')
