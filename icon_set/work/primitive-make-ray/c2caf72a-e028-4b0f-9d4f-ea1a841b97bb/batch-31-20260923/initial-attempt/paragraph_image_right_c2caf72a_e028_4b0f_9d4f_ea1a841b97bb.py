from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c2caf72a-e028-4b0f-9d4f-ea1a841b97bb'
SOURCE_PATH = 'icon_set/work/todo-references/paragraph image right_c2caf72a-e028-4b0f-9d4f-ea1a841b97bb.svg'
AUTHOR = 'gpt-6'
PLAN = 'Paragraph panel with an image at upper right and text rules at left and below.'
CONSTRUCTION_REFERENCES = 'monitor: rounded rectangular enclosure.'
OMISSIONS = 'Four text rows reduced to three to improve spacing.'

class Drawing(Solo48):
    icon_id = 'paragraph-image-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('paragraph', 'image', 'right')

    def circle(self, name, cx, cy, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; members.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')

    def build(self):
        self.box('panel',6,6,36,36,3)
        self.box('image',27,14,8,8,2)
        self.add_line('text-short',(14,16),(19,16))
        for i,y in enumerate((26,34)):
            self.add_line(f'text-{i}',(14,y),(34,y))
