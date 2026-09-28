"""Smooth scalloped foam, rounded mug, two spaced ribs and generous handle.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
No useful exact Lucide match inspected; supplied reference guided the geometric reconstruction.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ae952df2-68f4-565e-b88a-dcfb00a56475'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer mug_ae952df2-68f4-565e-b88a-dcfb00a56475.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='foaming-beer-mug-with-two-vertical-ribs'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases=()
    keywords=('beer mug',)
    def build(self):
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('body',(6,18),[('L',(6,38)),('A',(10,42),4,4,False),('L',(30,42)),('A',(34,38),4,4,False),('L',(34,30)),('L',(34,18))])
        path('foam',(6,18),[('C',(10,10),(6,14),(6,10)),('C',(22,6),(10,6),(18,6)),('C',(30,10),(26,6),(30,6)),('A',(34,14),4,4,True),('L',(34,18)),('L',(18,18)),('C',(6,18),(14,22),(6,22))])
        path('handle',(34,18),[('A',(34,30),8,6,True)])
        join('body','foam');join('body','handle');join('foam','handle')
        for x in (15,25):line(f'rib-{x}',(x,29),(x,33))
