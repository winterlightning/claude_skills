"""Five distinct rounded petals above a vertical stem and a left-facing leaf. Extrema 8,4,40,44.
Construction: flower-2: connected stem and a single leaf
Reduction: Small flower centre omitted; all five petals retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5ba3e5a-1e84-4926-9afb-e69a52e23191'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/corsage_f5ba3e5a-1e84-4926-9afb-e69a52e23191.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='five-petal-flower-with-side-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('five', 'petal', 'flower', 'with', 'side', 'leaf')
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

        path('bloom',(28,4),[('C',(34,11),(33,4),(34,7)),('C',(40,15),(38,9),(40,10)),('C',(35,21),(40,19),(38,21)),('C',(34,26),(39,24),(38,26)),('C',(28,22),(31,26),(30,25)),('C',(22,26),(26,25),(25,26)),('C',(21,21),(18,26),(17,24)),('C',(16,15),(18,21),(16,19)),('C',(22,11),(16,10),(18,9)),('C',(28,4),(22,7),(23,4))],True)
        line('stem',(28,22),(28,44));join('stem','bloom')
        path('leaf',(28,44),[('L',(18,44)),('A',(8,34),10,10,True),('L',(8,32)),('A',(28,44),20,12,True)],True);join('stem','leaf')
