"""Front-facing car beneath three spray streams has a broad windshield and paired tires. Extrema 6,6,42,42.
Construction: car-front: symmetric windshield and rounded body corners
Reduction: Headlamps omitted to retain clear cabin/body bands; spray reduced to three long strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e8878e02-6a89-4f38-91b2-1f4b7dd92fdd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car repair wash 1_e8878e02-6a89-4f38-91b2-1f4b7dd92fdd.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='front-facing-car-under-spray'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('front', 'facing', 'car', 'under', 'spray')
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

        path('body',(6,30),[('L',(12,22)),('L',(36,22)),('L',(42,30)),('L',(42,35)),('A',(39,38),3,3,True),('L',(36,38)),('L',(12,38)),('L',(9,38)),('A',(6,35),3,3,True),('L',(6,30))],True)
        line('windshield',(6,30),(42,30));join('windshield','body')
        for x in (12,36):line('tire-'+str(x),(x,38),(x,42));join('tire-'+str(x),'body')
        for x in (12,24,36):line('spray-'+str(x),(x,6),(x-1,13))
