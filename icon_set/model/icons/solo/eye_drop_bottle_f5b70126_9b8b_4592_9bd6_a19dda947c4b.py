"""Rounded diagonal medicine bottle, broad nozzle and teardrop.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide pipette: smooth diagonal tool silhouette and shared collar attachment.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5b70126-9b8b-4592-9bd6-a19dda947c4b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/eye drop medicine_f5b70126-9b8b-4592-9bd6-a19dda947c4b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='eye-drop-bottle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/health'
    aliases=()
    keywords=('eye drop medicine',)
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
        path('bottle',(18,16),[('L',(32,6)),('C',(36,8),(34,6),(35,6)),('L',(42,20)),('C',(40,24),(42,22),(42,23)),('L',(28,30)),('L',(14,24)),('L',(18,16))],True)
        line('collar',(18,16),(28,30));join('collar','bottle')
        path('drop',(10,32),[('C',(6,38),(8,34),(6,36)),('A',(14,38),4,4,False),('C',(10,32),(14,36),(12,34))],True)
