from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='97e073c3-c54d-4538-82ad-6e96f7d3a5cd'
SOURCE_PATH='icon_set/work/todo-references/pin x mark 1_97e073c3-c54d-4538-82ad-6e96f7d3a5cd.svg'
AUTHOR='gpt-6'
PLAN='Round map marker containing X, with a short narrow triangular tail below. Head symmetry and X share x=24.'
CONSTRUCTION_REFERENCES='Lucide map-pin: rounded head and point; X is hand-authored.'
OMISSIONS='None.'
KEYSHAPE_INK_BOUNDS=(6, 2, 42, 46)

class Drawing(Solo48):
    icon_id='pin-x-mark-1'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('pin', 'x', 'mark', '1')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,rx,ry,diagonal=True):
        if diagonal:
            self.add_polyline(name+'-a',(cx-rx,cy-ry),(cx,cy),(cx+rx,cy+ry))
            self.add_polyline(name+'-b',(cx+rx,cy-ry),(cx,cy),(cx-rx,cy+ry))
        else:
            self.add_polyline(name+'-a',(cx-rx,cy),(cx,cy),(cx+rx,cy))
            self.add_polyline(name+'-b',(cx,cy-ry),(cx,cy),(cx,cy+ry))
        self.relate('connect',name+'-a',name+'-b')

    def pin(self,name,cx,top,r,tip,style='broad'):
        cy=top+r
        self.add_arc(name+'-dome',(cx-r,cy),(cx+r,cy),radius_x=r)
        if style=='narrow':
            self.add_bezier(name+'-right',(cx+r,cy),((cx+r,cy+8),(cx+r-4,cy+11),(cx+7,tip-9)),((cx+3,tip-6),(cx+2,tip-4),(cx,tip)))
            self.add_bezier(name+'-left',(cx,tip),((cx-2,tip-4),(cx-3,tip-6),(cx-7,tip-9)),((cx-r+4,cy+11),(cx-r,cy+8),(cx-r,cy)))
        else:
            self.add_bezier(name+'-right',(cx+r,cy),((cx+r,cy+7),(cx+7,tip-6),(cx,tip)))
            self.add_bezier(name+'-left',(cx,tip),((cx-7,tip-6),(cx-r,cy+7),(cx-r,cy)))
        self.add_contour(name,name+'-dome',name+'-right',name+'-left',closed=True)

    def build(self):
        self.add_arc('dome',(8,20),(40,20),radius_x=16)
        self.add_bezier('right',(40,20),((40,27),(35,33),(28,35)))
        self.add_line('tail-1',(28,35),(24,44));self.add_line('tail-2',(24,44),(20,35))
        self.add_bezier('left',(20,35),((13,33),(8,27),(8,20)))
        self.add_contour('pin','dome','right','tail-1','tail-2','left',closed=True)
        self.cross('x',24,20,5,5)

KEYSHAPE_REASON='The upright complete composition uses centerline extremes (8,4)–(40,44).'
