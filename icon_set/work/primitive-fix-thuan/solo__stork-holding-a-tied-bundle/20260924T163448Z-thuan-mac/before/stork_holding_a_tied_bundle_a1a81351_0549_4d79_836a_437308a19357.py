"""Stork Holding a Tied Bundle
Plan: Right-facing long-necked stork holding teardrop bundle at beak tip.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Tiny eye and knot loops omitted; pointed beak reduced to one stroke and teardrop bundle retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1a81351-0549-4d79-836a-437308a19357'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby stork_a1a81351-0549-4d79-836a-437308a19357.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stork-holding-a-tied-bundle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('stork', 'bundle', 'baby', 'beak', 'bird', 'knot', 'carrying')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('stork',(6,42),[('C',(8,30),(12,42),(8,34)),('L',(6,18)),('C',(17,6),(6,8),(11,6)),('C',(24,14),(23,6),(24,10)),('L',(22,22)),('L',(20,26)),('C',(18,42),(18,34),(20,42))])
        line('beak',(24,14),(36,18));join('beak','stork')
        path('bundle',(36,18),[('C',(42,34),(39,24),(42,28)),('C',(35,42),(42,40),(38,42)),('C',(28,34),(32,42),(28,40)),('C',(36,18),(28,28),(33,22))],True);join('beak','bundle')
