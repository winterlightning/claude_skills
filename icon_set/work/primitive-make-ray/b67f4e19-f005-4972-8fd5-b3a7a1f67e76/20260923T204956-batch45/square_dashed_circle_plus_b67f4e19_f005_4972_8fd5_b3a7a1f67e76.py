"""A plus inside a dashed circular ring inside a rounded square.
Plan: Eight short ring dashes use symmetric cardinal and diagonal placements; plus shares its center.
Construction: square-dashed: spaced dash series; rounded-square outer contour
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b67f4e19-f005-4972-8fd5-b3a7a1f67e76'
SOURCE_PATH = 'icon_set/work/todo-references/square dashed circle plus_b67f4e19-f005-4972-8fd5-b3a7a1f67e76.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-dashed-circle-plus'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'dashed', 'circle', 'plus')

    def build(self):
        self.box('frame',rad=5)
        # Symmetric integer dash placements approximate one circular ring.
        pairs=[((21,14),(27,14)),((30,16),(32,18)),((34,21),(34,27)),((32,30),(30,32)),((27,34),(21,34)),((18,32),(16,30)),((14,27),(14,21)),((16,18),(18,16))]
        for i,(a,b) in enumerate(pairs):self.add_line(f'dash-{i}',a,b)
        self.add_polyline('plus-h',(20,24),(24,24),(28,24))
        self.add_polyline('plus-v',(24,20),(24,24),(24,28))
        for a in (1,2):
            for b in (1,2):self.relate('connect',f'plus-h-{a}',f'plus-v-{b}')

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
