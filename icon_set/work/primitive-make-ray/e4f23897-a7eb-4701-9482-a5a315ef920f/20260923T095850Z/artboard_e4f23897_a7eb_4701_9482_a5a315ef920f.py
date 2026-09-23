"""A square artboard with eight detached corner registration ticks.

Plan: Square frame centered on (24,24); eight ticks derived by axis reflection. SQUARE extremes (6,6)-(42,42). Inner frame reduced to allocate exact 8-unit centerline gaps. No useful Lucide subject match needed; all eight ticks retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e4f23897-a7eb-4701-9482-a5a315ef920f'
SOURCE_PATH = 'icon_set/work/todo-references/artboard_e4f23897-a7eb-4701-9482-a5a315ef920f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'artboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('artboard',)
    def build(self):
        lo,hi=16,32
        self.add_polyline('board',(lo,lo),(hi,lo),(hi,hi),(lo,hi),closed=True)
        for i,p in enumerate((lo,hi)):
            self.add_line(f'left-{i}',(6,p),(8,p))
            self.add_line(f'right-{i}',(40,p),(42,p))
            self.add_line(f'top-{i}',(p,6),(p,8))
            self.add_line(f'bottom-{i}',(p,40),(p,42))

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def roundrect(self,name,x0,y0,x1,y1,r):
        nodes=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)
