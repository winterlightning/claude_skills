"""A square button containing a two-panel rectangle.
Plan: Nested rectangular panel has a horizontal divider at its midpoint; this preserves the drawing rather than interpreting the filename as arithmetic.
Construction: square-divide: rounded enclosure only; interior follows supplied two-panel reference
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1005348f-eefa-4453-b13a-0c67265a58f6'
SOURCE_PATH = 'icon_set/work/todo-references/square divide_1005348f-eefa-4453-b13a-0c67265a58f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-divide'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'divide')

    def build(self):
        self.box('frame',rad=5)
        self.add_polyline('panel',(15,15),(33,15),(33,24),(33,33),(15,33),(15,24),closed=True)
        self.add_line('divider',(15,24),(33,24))
        for part in (2,3,5,6):self.relate('connect','divider',f'panel-{part}')

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
