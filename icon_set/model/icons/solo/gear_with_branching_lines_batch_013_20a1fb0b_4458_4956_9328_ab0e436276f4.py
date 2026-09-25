"""Rounded six-tooth gear connects to a three-way branching line. Extrema 4,8,44,40.
Construction: settings: rounded teeth instead of angular mitres
Reduction: Tiny central dot omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20a1fb0b-4458-4956-9328-ab0e436276f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='gear-with-branching-lines-batch-013'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases=()
    keywords=('gear', 'with', 'branching', 'lines', 'batch', '013')
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

        path('gear',(12,17),[('A',(16,10),4,7,True),('A',(20,17),4,7,True),('C',(28,17),(24,15),(28,12)),('C',(23,24),(28,21),(24,22)),('C',(28,31),(24,26),(28,27)),('C',(20,31),(28,36),(24,33)),('C',(16,38),(20,36),(19,38)),('C',(12,31),(13,38),(12,36)),('C',(4,31),(8,33),(4,36)),('C',(9,24),(4,27),(8,26)),('C',(4,17),(8,22),(4,21)),('C',(12,17),(4,12),(8,15))],True)
        poly('spine',(44,8),(38,8),(38,24),(38,40),(44,40));poly('arm',(23,24),(38,24),(44,24));join('arm','gear');join('arm','spine')
