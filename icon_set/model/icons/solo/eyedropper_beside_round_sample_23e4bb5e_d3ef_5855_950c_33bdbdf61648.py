"""Coherent diagonal pipette with round bulb and separate round sample.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide pipette: smooth diagonal tool silhouette and shared collar attachment.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '23e4bb5e-d3ef-5855-950c-33bdbdf61648'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker 3_23e4bb5e-d3ef-5855-950c-33bdbdf61648.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='eyedropper-beside-round-sample'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'design'
    aliases=()
    keywords=('color picker 3',)
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
        path('tool',(24,14),[('L',(28,10)),('C',(38,20),(36,2),(46,12)),('L',(34,24)),('L',(16,34)),('L',(6,36)),('L',(8,26)),('L',(24,14))],True)
        poly('collar',(18,6),(24,14),(34,24));join('collar','tool')
        circle('sample',38,38,4)
