"""Wine Glass
Plan: Wine glass with mirrored bowl, short foot and axial stem.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide wine: centered stem and bowl.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82f1acbf-a3e8-40f6-a7a3-62af0f369409'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wine_82f1acbf-a3e8-40f6-a7a3-62af0f369409.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wine-glass-reference-82f1acbf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wine', 'glass', 'stemmed', 'drink', 'beverage', 'tableware')

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
        path('bowl',(12,4),[('L',(36,4)),('C',(40,18),(38,10),(40,13)),('C',(24,30),(40,25),(32,30)),('C',(8,18),(16,30),(8,25)),('C',(12,4),(8,13),(10,10))],True)
        line('stem',(24,30),(24,44));poly('foot',(14,44),(24,44),(34,44));join('stem','bowl');join('stem','foot')
