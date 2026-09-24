"""A broad dairy can has a rounded lid, straight neck, sloping shoulders and rounded lower corners. Extrema 8,4,40,44.
Construction: milk: continuous neck-to-shoulder outline and rounded body
Reduction: Fine wire side handles omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6e17ac5-4fa7-466b-8fb9-4a1985a11ad7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/milk can_d6e17ac5-4fa7-466b-8fb9-4a1985a11ad7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='lidded-dairy-milk-can'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('lidded', 'dairy', 'milk', 'can')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('lid',(12,12),[('L',(12,8)),('A',(16,4),4,4,True),('L',(32,4)),('A',(36,8),4,4,True),('L',(36,12)),('L',(32,12)),('L',(16,12)),('L',(12,12))],True)
        path('can',(16,12),[('L',(16,20)),('L',(8,28)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,28)),('L',(32,20)),('L',(32,12))]);join('can','lid')
        line('shoulder-rule',(16,20),(32,20));join('shoulder-rule','can')
