"""Chef knife with a broad curved blade and a rounded diagonal grip at the heel. Extrema 6,6,42,42.
Construction: pocket-knife: rounded grip construction; supplied chef blade controls silhouette
Reduction: Rivet dots omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '88acc3ca-ec5a-4cec-af6f-f39df121e302'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='kitchen-chef-knife'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "food"
    aliases=()
    keywords=('kitchen', 'chef', 'knife')
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

        path('blade',(6,6),[('L',(30,24)),('L',(22,32)),('C',(6,6),(12,24),(6,16))],True)
        path('handle',(30,24),[('L',(40,34)),('C',(42,38),(42,35),(42,36)),('A',(38,42),4,4,True),('L',(32,42)),('L',(22,32))]);join('handle','blade')
