from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a6bc318-1415-407d-8cee-66dc95d8d15f'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg'
AUTHOR = 'gpt-6'
PLAN = 'Campfire above a rectangular six-section fuel bed. Grid cells share intersections.'
CONSTRUCTION_REFERENCES = 'flame: asymmetric tongue and rounded lower bowl.'
OMISSIONS = 'None; six fuel sections retained.'

class Drawing(Solo48):
    icon_id = 'outdoors-fire-camp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('outdoors', 'fire', 'camp')

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
        self.add_arc('fire-left',(19,15),(24,6),radius_x=10,sweep=False)
        self.add_arc('fire-tip',(24,6),(30,17),radius_x=14,sweep=False)
        self.add_arc('fire-bowl',(30,17),(18,17),radius_x=6,radius_y=7)
        self.add_line('fire-notch',(18,17),(19,15))
        self.add_contour('flame','fire-left','fire-tip','fire-bowl','fire-notch',closed=True)
        self.box('fuel',6,30,36,12,2)
        self.add_line('fuel-horizontal',(6,36),(42,36));self.relate('connect','fuel','fuel-horizontal')
        for x in (18,30):
            self.add_polyline(f'fuel-divider-{x}',(x,30),(x,36),(x,42))
            self.relate('connect','fuel',f'fuel-divider-{x}')
            self.relate('connect','fuel-horizontal',f'fuel-divider-{x}')
