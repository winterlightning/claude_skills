"""Three upright archive books.
Plan: HRECT_L fits three equal eight-unit spines and two eight-unit gaps.
Reduction: Removed spine labels and finger holes; they cannot fit inside the narrow spines.
Construction: Lucide book-open: simple book outlines; supplied reference determines the three-spine series.
Layout: Repeated equal spines centered on x=24."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '42cdb953-b64a-446a-9e2f-0a5e1116e601'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg'
AUTHOR = "gpt-6"

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
            x=4+16*i
            self.roundrect(f'binder-{i}',x,8,x+8,40,2)

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
