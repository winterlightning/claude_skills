"""Scooter with Security Camera.

Plan: Retained the security camera above the scooter, camera mount, handlebar, seat, deck and two wheels. Simplified the scooter body to structural strokes.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '109ac4f6-204a-4d3b-8da5-f02fdf8bb3cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/scooter parking security_109ac4f6-204a-4d3b-8da5-f02fdf8bb3cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'security-camera-watching-a-scooter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('security', 'camera', 'watching', 'a', 'scooter')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('camera',(8,6),(24,10),(22,18),(6,14),(8,6),closed=True)
        poly('mount',(10,15),(10,18),(6,20));join('mount','camera')
        line('deck',(16,38),(34,38));poly('front',(38,34),(38,18),(32,18))
        line('seat',(18,26),(26,26));line('post',(24,26),(24,38));join('post','seat');join('post','deck')
        circle('rear-wheel',12,38,4);circle('front-wheel',38,38,4);join('rear-wheel','deck');join('front-wheel','deck');join('front-wheel','front')
