"""Two Tower Suspension Bridge
Plan: Symmetric suspension bridge with two towers, cable dips and two water rows.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Deck shortened to span the two towers; outer cables, two supports and two water rows retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86b37e1a-0047-497f-8897-cc61b8ea2db2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bridge golden gate_86b37e1a-0047-497f-8897-cc61b8ea2db2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-tower-suspension-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bridge', 'suspension', 'water', 'cables', 'towers', 'structure', 'river')

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
        for x in (12,36):poly(f'tower-{x}',(x,6),(x,22),(x,30))
        poly('deck',(12,22),(24,22),(36,22))
        path('cable',(6,22),[('C',(12,6),(6,17),(8,10)),('C',(24,22),(18,12),(18,22)),('C',(36,6),(30,22),(30,12)),('C',(42,22),(40,10),(42,17))]);join('deck','cable')
        for x in (12,36):join(f'tower-{x}','deck');join(f'tower-{x}','cable')
        for y in (32,42):path(f'water-{y}',(6,y),[('C',(12,y-2),(8,y),(10,y-2)),('C',(24,y),(16,y-2),(20,y)),('C',(36,y-2),(28,y),(32,y-2)),('C',(42,y),(38,y-2),(40,y))])
        for x in (12,36):join(f'tower-{x}','water-32')
