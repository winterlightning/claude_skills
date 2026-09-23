from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ff75519b-afd0-4da5-b995-1999fe2b031a'
SOURCE_PATH = 'icon_set/work/todo-references/stack unstack column_ff75519b-afd0-4da5-b995-1999fe2b031a.svg'
AUTHOR = 'gpt-6'
PLAN = 'A descending staircase of stacked column cells with two downward curved arrows.'
CONSTRUCTION_REFERENCE = 'No useful Lucide subject match; shared cell widths and repeated arrow construction'

class Drawing(Solo48):
    icon_id = 'stack-unstack-column'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('stack', 'unstack', 'column')

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
        self.add_polyline('column-top',(6,6),(14,6),(14,22),(6,22),closed=True)
        self.add_line('divider-top',(6,14),(14,14))
        self.relate('connect','divider-top','column-top')
        self.add_polyline('column-middle',(14,22),(22,22),(22,34),(14,34),closed=True)
        self.add_line('divider-middle',(14,28),(22,28))
        self.relate('connect','divider-middle','column-middle')
        self.relate('connect','column-top','column-middle')
        self.add_polyline('column-bottom',(22,34),(30,34),(30,42),(22,42),closed=True)
        self.relate('connect','column-middle','column-bottom')
        for name,x,y in [('first',28,10),('second',36,26)]:
            self.add_arc(name+'-turn',(x,y),(x+6,y+6),radius_x=6)
            self.add_arc(name+'-down',(x+6,y+6),(x,y+12),radius_x=6)
            self.add_contour(name+'-curve',name+'-turn',name+'-down')
            self.add_polyline(name+'-tip',(x+4,y+8),(x,y+12),(x+4,y+16))
            self.relate('connect',name+'-down',name+'-tip')
