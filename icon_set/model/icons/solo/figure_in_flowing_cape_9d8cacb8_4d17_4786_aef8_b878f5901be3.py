"""Figure in Flowing Cape
Plan: Round head above broad left-descending cape and right fluttering panel.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Shared human full_body_ref.png: circular head and simple clothed figure.
Reduction: No limbs invented; cape carries the source silhouette. Head bottom16 to cape neck24 gives exact8 centerline gap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d8cacb8-4d17-4786-aef8-b878f5901be3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cape_9d8cacb8-4d17-4786-aef8-b878f5901be3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'figure-in-flowing-cape'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cape', 'figure', 'superhero', 'person', 'flowing', 'clothing', 'cloak')

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
        circle('head',26,11,5)
        path('cape',(26,24),[('C',(6,37),(18,24),(11,30)),('C',(19,42),(10,40),(13,42)),('L',(26,24)),('C',(42,36),(30,29),(34,34)),('C',(22,37),(37,41),(30,34))])
