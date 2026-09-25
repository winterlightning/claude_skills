from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3e518fa9-536c-4b17-8b74-cb45eff7aecc'
SOURCE_PATH='icon_set/work/todo-references/pin x mark 3_3e518fa9-536c-4b17-8b74-cb45eff7aecc.svg'
AUTHOR='gpt-6'
PLAN='Broad rounded pin with a larger circular hole over a wide ground X. Softer base distinguishes it from pin x mark 2.'
CONSTRUCTION_REFERENCES='Lucide map-pin: domed head and hole.'
OMISSIONS='None; broad X retained.'
KEYSHAPE_INK_BOUNDS=(8, 2, 40, 46)

class Drawing(Solo48):
    icon_id='pin-x-mark-3'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('pin', 'x', 'mark', '3')

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
        self.add_arc('dome',(10,18),(38,18),radius_x=14)
        self.add_bezier('right',(38,18),((38,24),(30,28),(26,30)),((25,31),(23,31),(22,30)))
        self.add_bezier('left',(22,30),((18,28),(10,24),(10,18)))
        self.add_contour('pin','dome','right','left',closed=True)
        self.circle('hole',24,17,3)
        self.cross('ground-x',24,40,9,4)

KEYSHAPE_REASON='The narrow marker-and-ground composition uses centerline extremes (10,4)–(38,44).'
FINAL_REDUCTIONS='No components omitted. Pin aperture and vertical pin proportions reduced to make room for the ground X.'
