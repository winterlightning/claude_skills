"""Code angle brackets and a diagonal slash inside a rounded square.
Plan: Paired angle brackets reflect about x24; separate rising slash preserves reference code syntax.
Construction: square-code: paired angle brackets within rounded enclosure
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bace2392-58d6-42ff-85cc-dedbb5e924c6'
SOURCE_PATH = 'icon_set/work/todo-references/square code_bace2392-58d6-42ff-85cc-dedbb5e924c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-code-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'code')

    def build(self):
        self.box('frame',rad=5)
        for side in (0,1):
            def p(x,y):return (48-x if side else x,y)
            self.add_polyline(f'chevron-{side}',p(19,18),p(14,24),p(19,30))
        self.add_line('slash',(27,15),(21,33))

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
