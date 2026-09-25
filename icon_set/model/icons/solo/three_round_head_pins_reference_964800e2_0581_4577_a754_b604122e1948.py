"""Three Sewing Pins.

Plan: Three round heads and long left-pointing shafts; bounds4,8,44,40. Shared radius3 with three distinct source angles.
Construction reference: pin.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '964800e2-0581-4577-a754-b604122e1948'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/needles three_964800e2-0581-4577-a754-b604122e1948.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-round-head-pins-reference'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'round', 'head', 'pins', 'reference')

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

        for j,(x,y,a) in enumerate([(35,11,(4,14)),(41,24,(4,24)),(35,37,(4,34))]):
         path(f'head-{j}',(x-3,y),[('A',(x+3,y),3,3,True),('A',(x-3,y),3,3,True)],True)
         line(f'shaft-{j}',a,(x-3,y));join(f'shaft-{j}',f'head-{j}')
