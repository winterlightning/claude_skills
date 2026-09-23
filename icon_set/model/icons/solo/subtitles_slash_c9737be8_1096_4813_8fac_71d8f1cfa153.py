from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9737be8-1096-4813-8fac-71d8f1cfa153'
SOURCE_PATH = 'icon_set/work/todo-references/subtitles slash_c9737be8-1096-4813-8fac-71d8f1cfa153.svg'
AUTHOR = 'gpt-6'
PLAN = 'Rounded speech bubble with a descending right tail and rising slash.'
CONSTRUCTION_REFERENCE = 'message-square: rounded speech enclosure and angular tail'

class Drawing(Solo48):
    icon_id = 'subtitles-slash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('subtitles', 'slash')

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
        self.add_line('top',(11,6),(37,6))
        self.add_arc('top-right',(37,6),(42,11),radius_x=5)
        self.add_line('right',(42,11),(42,29))
        self.add_arc('bottom-right',(42,29),(37,34),radius_x=5)
        tail=[(37,34),(36,34),(36,42),(28,34),(11,34)]
        for j in range(4): self.add_line(f'tail-{j+1}',tail[j],tail[j+1])
        self.add_arc('bottom-left',(11,34),(6,29),radius_x=5)
        self.add_line('left',(6,29),(6,11))
        self.add_arc('top-left',(6,11),(11,6),radius_x=5)
        self.add_contour('bubble','top','top-right','right','bottom-right','tail-1','tail-2','tail-3','tail-4','bottom-left','left','top-left',closed=True)
        self.add_line('slash',(16,25),(31,15))
