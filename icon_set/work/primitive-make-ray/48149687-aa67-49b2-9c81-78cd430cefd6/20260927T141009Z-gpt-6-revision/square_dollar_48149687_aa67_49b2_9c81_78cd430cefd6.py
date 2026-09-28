"""A dollar sign inside a square.
Repair plan: Open S with attached upper and lower stem tips; opposite S lobes remain balanced.
Omissions: Internal stem spans, retaining the terminal dollar strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '48149687-aa67-49b2-9c81-78cd430cefd6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-dollar-solo/20260927T140026Z-thuan-mac-1/reference/square dollar_48149687-aa67-49b2-9c81-78cd430cefd6.svg'
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
        self.add_bezier('s-top',(30,18),((28,17),(26,17),(24,17)))
        self.add_bezier('s-upper',(24,17),((17,17),(17,22),(24,24)))
        self.add_bezier('s-lower',(24,24),((32,26),(32,31),(24,31)))
        self.add_bezier('s-bottom',(24,31),((22,31),(20,31),(18,29)))
        self.add_contour('s','s-top','s-upper','s-lower','s-bottom')
        self.add_line('stem-top',(24,15),(24,17))
        self.add_line('stem-bottom',(24,31),(24,33))
        self.relate('connect','s','stem-top')
        self.relate('connect','s','stem-bottom')

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
