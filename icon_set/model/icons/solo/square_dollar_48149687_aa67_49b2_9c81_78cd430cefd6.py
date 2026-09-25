"""A dollar sign inside a square.
Repair plan: Open S with attached upper and lower stem tips; opposite S lobes remain balanced.
Omissions: Internal stem spans, retaining the terminal dollar strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48149687-aa67-49b2-9c81-78cd430cefd6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/square dollar_48149687-aa67-49b2-9c81-78cd430cefd6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-dollar-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'dollar')

    def build(self):
        self.box('frame',rad=5)
        self.add_bezier('s-top',(30,18),((28,16),(26,16),(24,16)))
        self.add_bezier('s-upper',(24,16),((16,16),(16,22),(24,24)))
        self.add_bezier('s-lower',(24,24),((32,26),(32,32),(24,32)))
        self.add_bezier('s-bottom',(24,32),((22,32),(20,32),(18,30)))
        self.add_contour('s','s-top','s-upper','s-lower','s-bottom')
        self.add_line('stem-top',(24,15),(24,16))
        self.add_line('stem-bottom',(24,32),(24,33))
        for part in ('s-top','s-upper'):self.relate('connect','stem-top',part)
        for part in ('s-lower','s-bottom'):self.relate('connect','stem-bottom',part)

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
