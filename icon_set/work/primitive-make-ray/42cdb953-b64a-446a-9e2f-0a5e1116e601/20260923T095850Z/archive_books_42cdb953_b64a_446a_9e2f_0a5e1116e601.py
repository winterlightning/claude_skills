"""Three upright archive binders with spine labels and circular finger holes.

Plan: Three identical rounded rectangles in a centered series, shared width and radius. HRECT_L extremes (4,8)-(44,40). Lucide book informs tangent rounded corners. All identifying details retained; dense three-column topology may block MIC.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '42cdb953-b64a-446a-9e2f-0a5e1116e601'
SOURCE_PATH = 'icon_set/work/todo-references/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'archive-books'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('archive', 'books')
    def build(self):
        for i in range(3):
            x=4+15*i
            self.roundrect(f'binder-{i}',x,8,x+10,40,2)
            self.add_polyline(f'label-{i}',(x+3,14),(x+7,14),(x+7,26),(x+3,26),closed=True)
            self.circle(f'hole-{i}',x+5,33,2)

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
