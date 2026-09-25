"""Sun and Birds over Waves
Plan: Sun and three angular birds above two equal wave rows.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Sun rays omitted; three birds and two wave rows retained with shallower wave curves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a153065d-01c4-42c2-b412-5524c6b12347'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beach sun birds_a153065d-01c4-42c2-b412-5524c6b12347.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-and-birds-over-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sun', 'ocean', 'waves', 'birds', 'sea', 'landscape', 'weather')

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
        circle('sun',14,10,4)
        for i,(x,y) in enumerate([(31,6),(39,16),(25,19)]):poly(f'bird-{i}',(x-3,y),(x,y+3),(x+3,y))
        for y in (32,42):path(f'wave-{y}',(6,y),[('C',(18,y),(10,y-2),(14,y-2)),('C',(30,y),(22,y-2),(26,y-2)),('C',(42,y),(34,y-2),(38,y-2))])
