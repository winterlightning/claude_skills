"An irregular crumpled paper ball floats above a tapered wastebasket divided by a rectangular grid. A short curved motion stroke appears at the upper right, above the basket's wide open rim.\nPlan: Crumpled paper above wastebasket with a short motion stroke. Reduce basket mesh to one vertical and one horizontal division.\nConstruction reference: No useful exact Lucide match; source-specific construction."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51c0ba7c-8e1e-4bcd-8e6e-7a81ea0b3029'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paper ball trash_51c0ba7c-8e1e-4bcd-8e6e-7a81ea0b3029.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paper-ball-above-wastebasket'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('paper', 'ball', 'above', 'wastebasket')

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

        poly('paper',(13,4),(20,6),(23,12),(18,18),(10,15),(8,9),(13,4))
        path('motion',(33,12),[('C',(40,8),(35,9),(38,8))])
        poly('basket',(8,27),(24,27),(40,27),(38,35),(36,44),(24,44),(12,44),(10,35),(8,27))
        line('mesh-v',(24,27),(24,44));line('mesh-h',(10,35),(38,35));join('basket','mesh-v');join('basket','mesh-h');join('mesh-v','mesh-h')
