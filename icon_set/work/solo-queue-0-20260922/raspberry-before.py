"""Fresh Raspberry Berry Fruit.

Plan: Tapered berry with broad repeated drupelet lobes and leafy crown. Bounds8,4,40,44. Omit tiny interior seeds.
Construction reference: No useful local Lucide match.
Final review: Not released: simplification loses the raspberry drupelets and three-leaf identity.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86657946-998d-44be-80c5-35a4d1b96f55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boysenberry_86657946-998d-44be-80c5-35a4d1b96f55.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raspberry-with-three-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('raspberry', 'with', 'three', 'leaves')

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

        path('berry',(16,24),[('C',(32,24),(16,20),(32,20)),('C',(40,28),(40,22),(40,24)),('C',(36,34),(40,32),(40,34)),('C',(30,40),(36,40),(34,40)),('C',(24,44),(30,44),(28,44)),('C',(18,40),(20,44),(18,44)),('C',(12,34),(14,40),(12,40)),('C',(8,28),(8,34),(8,32)),('C',(16,24),(8,24),(8,22))],True)
        path('leaf',(24,12),[('C',(40,4),(24,4),(34,4)),('C',(24,12),(40,12),(32,12))],True)
        line('stem',(24,12),(24,21));join('stem','leaf');join('stem','berry')
