from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ef84068a-8813-43c3-b7d5-546375fbf309'
SOURCE_PATH = 'icon_set/work/todo-references/start your machine learning journey_ef84068a-8813-43c3-b7d5-546375fbf309.svg'
AUTHOR = 'gpt-6'
PLAN = 'Open book at upper left beside a four-node learning network.'
CONSTRUCTION_REFERENCE = 'book-open and network: central book fold and repeated connected nodes'

class Drawing(Solo48):
    icon_id = 'start-your-machine-learning-journey'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('start', 'your', 'machine', 'learning', 'journey')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-upper', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-lower', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, left, top, right, bottom, r):
        # One rounded rectangle definition owns all matching corners.
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8]; member=f'{name}-{i}'
            if i%2: self.add_arc(member,start,end,radius_x=r)
            else: self.add_line(member,start,end)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        ends = [(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):
            self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def bust_body(self):
        # Shared shoulder radii; badge occludes the right shoulder and hem.
        self.add_line('body-left',(6,42),(6,40))
        self.add_arc('shoulder-left',(6,40),(16,30),radius_x=10)
        self.add_line('shoulder-top',(16,30),(24,30))
        self.add_arc('shoulder-right',(24,30),(30,36),radius_x=6)
        self.add_contour('shoulders','body-left','shoulder-left','shoulder-top','shoulder-right')
        self.add_line('hem',(6,42),(36,42))
        self.circle('badge',36,36,6)
        self.relate('connect','hem','body-left')
        self.relate('connect','hem','badge-lower')
        self.relate('connect','shoulder-right','badge-upper','badge-lower')

    def build(self):
        self.add_polyline('book',(6,24),(6,6),(16,11),(26,6),(26,17))
        self.add_line('book-bottom',(6,24),(13,28))
        self.add_line('fold',(16,11),(16,23))
        self.relate('connect','book','book-bottom','fold')
        self.circle('hub',23,29,5)
        for name,x,y,r in [('top',36,19,3),('right',39,31,3),('bottom',34,39,3)]:
            self.circle(name,x,y,r)
        self.add_line('hub-top',(27,26),(33,21))
        self.add_line('hub-right',(28,29),(36,31))
        self.add_line('hub-bottom',(27,32),(31,37))
        self.add_line('top-right',(38,21),(40,28))
        self.add_line('right-bottom',(38,34),(36,37))
