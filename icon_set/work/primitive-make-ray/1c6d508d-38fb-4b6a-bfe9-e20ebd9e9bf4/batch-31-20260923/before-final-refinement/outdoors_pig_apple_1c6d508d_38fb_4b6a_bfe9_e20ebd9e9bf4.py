from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg'
AUTHOR = 'gpt-6'
PLAN = 'Pig head facing an apple pictured on a rectangular panel. Preserve the overlapping snout.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; source supplies pig/apple arrangement.'
OMISSIONS = 'Tiny nostril and panel portion behind snout omitted.'

class Drawing(Solo48):
    icon_id = 'outdoors-pig-apple'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('outdoors', 'pig', 'apple')

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
        self.add_polyline('panel',(22,24),(22,6),(42,6),(42,38),(24,38))
        self.add_polyline('pig',(6,42),(12,34),(20,31),(22,25),(14,22),(11,15),(6,14),(6,20))
        self.add_arc('apple-left',(32,20),(26,24),radius_x=4)
        self.add_arc('apple-bottom',(26,24),(38,24),radius_x=6,radius_y=7,sweep=False)
        self.add_arc('apple-right',(38,24),(32,20),radius_x=4)
        self.add_contour('apple','apple-left','apple-bottom','apple-right',closed=True)
        self.add_line('apple-stem',(32,20),(34,15));self.relate('connect','apple','apple-stem')
