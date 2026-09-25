"""Banded Oval Planula
Plan: Upright tapered larva with three repeated curved transverse bands.
Keyshape: VRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2173c4aa-7835-47b0-869a-416898094055'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/planula_2173c4aa-7835-47b0-869a-416898094055.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banded-oval-planula'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('planula', 'larva', 'organism', 'biology', 'oval', 'banded')

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
        path('body',(24,4),[('C',(34,14),(29,4),(32,8)),('C',(38,24),(37,17),(38,20)),('C',(34,34),(38,28),(37,31)),('C',(24,44),(32,40),(29,44)),('C',(14,34),(19,44),(16,40)),('C',(10,24),(11,31),(10,28)),('C',(14,14),(10,20),(11,17)),('C',(24,4),(16,8),(19,4))],True)
        for y,w in ((14,10),(24,14),(34,10)):
         path(f'band-{y}',(24-w,y),[('C',(24+w,y),(24-w//2,y+2),(24+w//2,y+2))]);join(f'band-{y}','body')
