from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df6e98df-8c0b-4cb1-a4f6-d0483b468f10'
SOURCE_PATH = 'icon_set/work/todo-references/openvpn logo_df6e98df-8c0b-4cb1-a4f6-d0483b468f10.svg'
AUTHOR = 'gpt-6'
PLAN = 'OpenVPN emblem: open circular outer arch surrounding a keyhole. Shared axis x=24.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; circle and coherent keyhole contours are authored directly.'
OMISSIONS = 'No semantic elements omitted.'

class Drawing(Solo48):
    icon_id = 'openvpn-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('openvpn', 'logo')

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
        self.add_arc('outer',(12,40),(36,40),radius_x=20,large_arc=True)
        self.add_arc('keyhole-head',(21,24),(27,24),radius_x=5,large_arc=True)
        self.add_line('keyhole-right',(27,24),(29,36))
        self.add_arc('keyhole-base',(29,36),(19,36),radius_x=5,radius_y=2)
        self.add_line('keyhole-left',(19,36),(21,24))
        self.add_contour('keyhole','keyhole-head','keyhole-right','keyhole-base','keyhole-left',closed=True)
