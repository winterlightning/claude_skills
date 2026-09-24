from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7b4f6d04-e199-443e-be81-3c0acef5ca62'
SOURCE_PATH='icon_set/work/todo-references/picture polaroid landscape_7b4f6d04-e199-443e-be81-3c0acef5ca62.svg'
AUTHOR='gpt-6'
PLAN='Polaroid landscape with two mountain peaks, upper-left sun and a wide bottom margin. Frame owns baseline attachments.'
CONSTRUCTION_REFERENCES='Lucide image: framed peaks and round sun.'
OMISSIONS='Sun reduced to a small circle; corners use rounded stroke joins.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='picture-polaroid-landscape'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('picture', 'polaroid', 'landscape')

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
        self.add_polyline('frame',(6,6),(42,6),(42,34),(42,42),(6,42),(6,34),closed=True)
        self.add_line('margin',(6,34),(42,34));self.relate('connect','frame','margin')
        self.circle('sun',16,16,2)
        self.add_polyline('mountains',(10,34),(18,28),(24,34),(32,22),(42,34));self.relate('connect','mountains','margin');self.relate('connect','mountains','frame')

KEYSHAPE_REASON='The whole composition is approximately square; the centerline extremes are (6,6)–(42,42).'
