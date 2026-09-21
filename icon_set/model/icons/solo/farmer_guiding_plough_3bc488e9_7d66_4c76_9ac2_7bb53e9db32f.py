"""Farmer Plowing the Soil.

Plan: Forward leaning farmer guiding plough. Head center22,11 radius5; torso junction17,23 gives exact8u centerline clearance along 5:12 axis. Bounds6,6,42,42.
Construction reference: human_ref/full_body_ref.png.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bc488e9-7d66-4c76-9ac2-7bb53e9db32f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plowman_3bc488e9-7d66-4c76-9ac2-7bb53e9db32f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'farmer-guiding-plough'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('farmer', 'guiding', 'plough')

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

        circle('head',22,11,5)
        path('torso',(17,23),[('C',(12,32),(15,28),(12,29))])
        poly('legs',(6,42),(12,32),(22,42));join('legs','torso')
        poly('arms',(17,23),(26,30),(32,30));join('arms','torso')
        poly('plough',(32,30),(36,38),(38,42),(42,42));join('arms','plough')
        path('share',(32,40),[('C',(38,42),(34,42),(36,42)),('L',(42,42))]);join('share','plough')
        self.mark_human_figure('farmer',head='head',torso='torso-0',torso_junction='start')
