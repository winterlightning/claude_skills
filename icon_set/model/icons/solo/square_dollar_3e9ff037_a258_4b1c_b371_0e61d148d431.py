"""A dollar sign inside a slightly rounded square.
Plan: Smooth S consists of four tangent cubic runs; short upper and lower stem extensions preserve the open center of the reference.
Construction: No local square-dollar-sign match found; rounded-square construction follows square-check, and S is hand-authored from the supplied reference.
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e9ff037-a258-4b1c-b371-0e61d148d431'
SOURCE_PATH = 'icon_set/work/todo-references/square dollar_3e9ff037-a258-4b1c-b371-0e61d148d431.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-dollar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('square', 'dollar')

    def build(self):
        self.box('frame',rad=2)
        self.add_bezier('s-top',(30,18),((28,16),(26,16),(24,16)))
        self.add_bezier('s-upper',(24,16),((16,16),(16,22),(24,24)))
        self.add_bezier('s-lower',(24,24),((32,26),(32,32),(24,32)))
        self.add_bezier('s-bottom',(24,32),((22,32),(20,32),(18,30)))
        self.add_contour('s','s-top','s-upper','s-lower','s-bottom')
        self.add_line('stem-top',(24,15),(24,16))
        self.add_line('stem-bottom',(24,32),(24,33))
        for part in ('s-top','s-upper'):self.relate('connect','stem-top',part)
        for part in ('s-lower','s-bottom'):self.relate('connect','stem-bottom',part)
        if False:
            self.add_line('stem-upper',(24,16),(24,24))
            self.add_line('stem-lower',(24,24),(24,32))
            for part in ('s-top','s-upper','s-lower'):self.relate('connect','stem-upper',part)
            for part in ('s-upper','s-lower','s-bottom'):self.relate('connect','stem-lower',part)
            self.relate('connect','stem-top','stem-upper')
            self.relate('connect','stem-upper','stem-lower')
            self.relate('connect','stem-lower','stem-bottom')

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
