"""Fresh Apple Fruit.

Plan: Lobed apple with stem and pointed leaf. Bounds8,4,40,44.
Construction reference: apple.
Final review: Moved fruit lower to clear the leaf; retained apple lobes and stem.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dab56ea-1c91-48e4-9197-a2a2de0bb76d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/codling_8dab56ea-1c91-48e4-9197-a2a2de0bb76d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apple-with-upright-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('apple', 'with', 'upright', 'leaf')

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

        path('apple',(24,24),[('C',(8,28),(12,20),(8,24)),('C',(18,44),(8,36),(10,44)),('C',(24,41),(21,44),(22,41)),('C',(30,44),(26,41),(27,44)),('C',(40,28),(38,44),(40,36)),('C',(24,24),(40,24),(36,20))],True)
        line('stem',(24,24),(24,12));join('stem','apple')
        path('leaf',(24,12),[('C',(40,4),(24,4),(34,4)),('C',(24,12),(40,12),(32,12))],True);join('leaf','stem')
