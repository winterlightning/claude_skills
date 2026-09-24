"""Primitive Cave Art Bull.

Plan: Cave-art bull facing left, bounds4,8,44,40. Two curved horns and four stick legs remain; intentional asymmetry of bent hind legs.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14947e0c-fbe9-4a62-8be2-bfa1ad2a4321'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/primitive symbols bull_14947e0c-fbe9-4a62-8be2-bfa1ad2a4321.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'primitive-bull-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('primitive', 'bull', 'profile')

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

        path('body',(12,16),[('C',(4,20),(8,12),(4,16)),('L',(4,24)),('L',(12,24)),('C',(24,30),(14,30),(18,30)),('L',(34,30)),('C',(44,22),(40,30),(44,27)),('C',(34,16),(44,16),(40,14)),('C',(12,16),(26,19),(18,14))])
        path('horn-upper',(12,16),[('C',(4,8),(12,10),(6,10))]);join('horn-upper','body')
        path('horn-lower',(12,16),[('C',(20,8),(12,10),(18,10))]);join('horn-lower','body');join('horn-lower','horn-upper')
        for name,a,b in [('front1',(14,27),(10,40)),('front2',(24,30),(22,40)),('back1',(34,30),(34,40)),('back2',(44,22),(44,40))]:line(name,a,b);join(name,'body')
