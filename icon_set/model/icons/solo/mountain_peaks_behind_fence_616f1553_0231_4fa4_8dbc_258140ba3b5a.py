"""Mountain Peaks behind Fence
Plan: Two peaks and round sun behind four-post two-rail fence.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '616f1553-0231-4fa4-8dbc-258140ba3b5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/outdoors landscape meadow_616f1553-0231-4fa4-8dbc-258140ba3b5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mountain-peaks-behind-fence'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mountains', 'fence', 'sun', 'landscape', 'peaks', 'outdoors')

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
        circle('sun',29,10,4)
        poly('mountains',(6,25),(16,18),(27,25),(35,22),(42,25))
        for y in (33,42):poly(f'rail-{y}',(6,y),(18,y),(30,y),(42,y))
        for x in (6,18,30,42):poly(f'post-{x}',(x,33),(x,42));join(f'post-{x}','rail-33');join(f'post-{x}','rail-42')
