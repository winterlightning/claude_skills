"""Striped Hooked Candy Cane
Plan: Hooked candy cane; shared hook center and two diagonal shaft stripes.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Fewer stripes to maintain readable bands."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f0e3043-e53d-4295-a857-28ae7f3f3097'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cake sugar cane_3f0e3043-e53d-4295-a857-28ae7f3f3097.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'striped-hooked-candy-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('candy-cane', 'candy', 'stripes', 'hook', 'christmas', 'sweet', 'holiday')

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
        path('cane',(8,20),[('A',(40,20),16,16,True),('L',(40,28)),('L',(40,37)),('L',(40,38)),('A',(28,38),6,6,True),('L',(28,31)),('L',(28,22)),('L',(28,20)),('A',(20,20),4,4,False),('A',(8,20),6,6,True)],True)
        for y in (22,31):line(f'stripe-{y}',(28,y),(40,y+6));join(f'stripe-{y}','cane')
