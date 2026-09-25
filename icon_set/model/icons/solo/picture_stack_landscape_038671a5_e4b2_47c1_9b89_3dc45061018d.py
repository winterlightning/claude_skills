from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='038671a5-e4b2-47c1-9b89-3dc45061018d'
SOURCE_PATH='icon_set/work/todo-references/picture stack landscape_038671a5-e4b2-47c1-9b89-3dc45061018d.svg'
AUTHOR='gpt-6'
PLAN='Three stacked landscape pictures. Front owns sun, two mountain peaks and lower caption margin; two rear L outlines retain the layer count.'
CONSTRUCTION_REFERENCES='Lucide image: frame, round sun, joined peaks.'
OMISSIONS='No layers omitted; minor corner rounding simplified.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='picture-stack-landscape'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'images'
    aliases=()
    keywords=('picture', 'stack', 'landscape')

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
        self.box('front',6,6,26,26,2)
        self.add_polyline('rear-1',(32,12),(37,12),(37,37),(12,37),(12,32))
        self.add_polyline('rear-2',(37,18),(42,18),(42,42),(18,42),(18,37))
        self.relate('connect','front','rear-1');self.relate('connect','rear-1','rear-2')
        self.circle('sun',14,14,2)
        self.add_polyline('mountains',(10,27),(16,20),(20,24),(26,16),(32,27));self.relate('connect','front','mountains')
        self.add_line('margin',(6,27),(32,27));self.relate('connect','front','margin');self.relate('connect','mountains','margin')

KEYSHAPE_REASON='The whole composition is approximately square; the centerline extremes are (6,6)–(42,42).'
