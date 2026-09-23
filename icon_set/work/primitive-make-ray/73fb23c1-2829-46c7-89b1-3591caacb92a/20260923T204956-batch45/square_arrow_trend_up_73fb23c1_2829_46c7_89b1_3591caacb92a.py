"""A rising zigzag trend arrow inside a rounded square.
Plan: Rounded square owns a rising zigzag and attached right-angle arrowhead; direction is intentionally asymmetric.
Construction: trending-up: zigzag and shared arrow endpoint
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '73fb23c1-2829-46c7-89b1-3591caacb92a'
SOURCE_PATH = 'icon_set/work/todo-references/square arrow trend up_73fb23c1-2829-46c7-89b1-3591caacb92a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-arrow-trend-up'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'arrow', 'trend', 'up')

    def build(self):
        self.box('frame')
        self.add_polyline('trend',(15,30),(21,24),(26,28),(33,18))
        self.add_polyline('head',(27,18),(33,18),(33,24))
        for i in (1,2):self.relate('connect','trend-3',f'head-{i}')

    def box(self,name,l=6,t=6,r=42,b=42,rad=4):
        mx,my=(l+r)//2,(t+b)//2
        pts=[(mx,t),(r-rad,t),(r,t+rad),(r,my),(r,b-rad),(r-rad,b),(mx,b),(l+rad,b),(l,b-rad),(l,my),(l,t+rad),(l+rad,t)]
        for i in range(12):
            a,z=pts[i],pts[(i+1)%12]
            if i in (1,4,7,10):self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(12)),closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def arrow(self,name,start,tip,a,b):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',a,tip,b)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')
