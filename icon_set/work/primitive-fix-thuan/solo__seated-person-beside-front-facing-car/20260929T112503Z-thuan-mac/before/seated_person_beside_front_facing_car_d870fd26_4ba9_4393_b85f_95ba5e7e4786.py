"""Seated Person and Car.

Plan: Retained the seated person and front-facing car. Simplified the car windshield and person to clear strokes. Head radius 4 at (10,10), torso junction (10,22) give exactly 4 visible units of head-to-body clearance.
Construction reference: human_ref/full_body_ref.png: circular head and bent seated limbs; Lucide car-front for structural car outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd870fd26-4ba9-4393-b85f-95ba5e7e4786'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/disability in car_d870fd26-4ba9-4393-b85f-95ba5e7e4786.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-person-beside-front-facing-car'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('seated', 'person', 'beside', 'front', 'facing', 'car')

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

        circle('head',10,10,4)
        line('torso',(10,22),(10,34));self.mark_human_figure('driver',head='head',torso='torso',torso_junction='start')
        poly('legs',(10,34),(20,34),(28,42));join('legs','torso')
        poly('arm',(10,22),(16,24),(18,24));join('arm','torso')
        poly('car',(26,18),(26,10),(30,6),(38,6),(42,10),(42,18),(26,18),closed=True)
        
        line('wheel-a',(28,18),(28,21));line('wheel-b',(40,18),(40,21));join('wheel-a','car');join('wheel-b','car')
