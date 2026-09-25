"""Radiating Eight Pointed Sparkle.

Plan: Eight radiating rays, cardinal reach20 and diagonal endpoints14 from center. Rotational symmetry; central opening remains empty.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4dfab29-6891-4931-8754-e2b2269435e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flare_e4dfab29-6891-4931-8754-e2b2269435e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eight-radiating-rays'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('eight', 'radiating', 'rays')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        for name,a,b in [('n',(24,4),(24,14)),('s',(24,34),(24,44)),('w',(4,24),(14,24)),('e',(34,24),(44,24)),('nw',(10,10),(16,16)),('ne',(38,10),(32,16)),('sw',(10,38),(16,32)),('se',(38,38),(32,32))]:line(name,a,b)
