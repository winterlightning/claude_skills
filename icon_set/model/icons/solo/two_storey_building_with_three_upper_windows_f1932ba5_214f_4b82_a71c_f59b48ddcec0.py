'A straight-sided building has a broad rounded roof cap above three small rectangular upper windows. A horizontal floor line separates the upper level from a tall arched entrance centered below.\nPlan: Two floors, three upper window marks and lower arched entrance.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1932ba5-214f-4b82-a71c-f59b48ddcec0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shopping mall_f1932ba5-214f-4b82-a71c-f59b48ddcec0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-storey-building-with-three-upper-windows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('two', 'storey', 'building', 'with', 'three', 'upper', 'windows')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        poly('building',(8,4),(40,4),(40,24),(40,44),(30,44),(18,44),(8,44),(8,24),(8,4))
        line('floor',(8,24),(40,24));join('floor','building')
        for x in (16,24,32):line(f'window-{x}',(x,12),(x,16))
        path('door',(18,44),[('L',(18,38)),('A',(30,38),6,6,True),('L',(30,44))]);join('door','building')
