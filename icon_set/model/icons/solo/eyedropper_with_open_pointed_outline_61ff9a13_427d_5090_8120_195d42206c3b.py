"""Round bulb and diagonal pipette over a smooth open pointed outline.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide pipette: smooth diagonal tool silhouette and shared collar attachment.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '61ff9a13-427d-5090-8120-195d42206c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker 1_61ff9a13-427d-5090-8120-195d42206c3b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='eyedropper-with-open-pointed-outline'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'design'
    aliases=()
    keywords=('color picker 1',)
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
        path('tool',(24,14),[('L',(28,10)),('C',(36,6),(31,7),(33,6)),('C',(42,12),(40,6),(42,8)),('C',(38,20),(42,15),(41,17)),('L',(28,30)),('L',(20,32)),('L',(22,24)),('L',(24,14))],True)
        poly('collar',(20,10),(24,14),(34,24));join('collar','tool')
        path('outline',(12,22),[('A',(6,28),6,6,False),('C',(16,42),(6,34),(12,40))])
