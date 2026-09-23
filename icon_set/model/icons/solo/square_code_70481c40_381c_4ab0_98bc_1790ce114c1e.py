"""Two code chevrons inside a circular border.
Plan: Circular enclosure retained despite filename; paired chevrons reflect about x24 with an eight-unit center gap.
Construction: square-code: paired mirrored angle brackets
Envelope: radius 22 about (24,24).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70481c40-381c-4ab0-98bc-1790ce114c1e'
SOURCE_PATH = 'icon_set/work/todo-references/square code_70481c40-381c-4ab0-98bc-1790ce114c1e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-code'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'code')

    def build(self):
        self.circle('frame',24,24,20)
        for side in (0,1):
            def p(x,y):return (48-x if side else x,y)
            self.add_polyline(f'chevron-{side}',p(20,16),p(13,24),p(20,32))

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
