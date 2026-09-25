"""Running Human Figure.

Plan: Rightward runner with raised front arm and bent rear leg. Circular head radius5 at29,11; torso begins24,23, exact13 center distance and8 outline gap. Bounds6,6,42,42.
Construction reference: human_ref/full_body_ref.png and approved approaching-ball circular-head/torso-axis construction
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52f16dbe-73c2-42ac-a2e9-1cf3f2731bef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/athletics team running_52f16dbe-73c2-42ac-a2e9-1cf3f2731bef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'running-figure-with-raised-front-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('running', 'figure', 'with', 'raised', 'front', 'arm')

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

        path('head',(24,11),[('A',(34,11),5,5,True),('A',(24,11),5,5,True)],True)
        line('torso',(24,23),(20,33));self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
        poly('back-arm',(24,23),(16,20),(10,26));join('back-arm','torso')
        poly('front-arm',(24,23),(34,28),(42,22));join('front-arm','torso');join('front-arm','back-arm')
        poly('back-leg',(20,33),(16,38),(6,36));poly('front-leg',(20,33),(30,36),(28,42));join('back-leg','torso');join('front-leg','torso');join('back-leg','front-leg')
