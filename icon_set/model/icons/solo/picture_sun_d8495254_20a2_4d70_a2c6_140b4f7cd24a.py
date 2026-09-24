from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d8495254-20a2-4d70-a2c6-140b4f7cd24a'
SOURCE_PATH='icon_set/work/todo-references/picture sun_d8495254-20a2-4d70-a2c6-140b4f7cd24a.svg'
AUTHOR='gpt-6'
PLAN='Framed sunshine above overlapping rounded hills. Five ray marks share the sun center; hills remain deliberately unequal.'
CONSTRUCTION_REFERENCES='Lucide image: rounded frame; circle construction for sun.'
OMISSIONS='Ray lengths reduced; all five source directions retained.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='picture-sun'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('picture', 'sun')

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
        self.box('frame',6,6,36,36,4)
        self.circle('sun',24,20,4)
        self.add_line('ray-top',(24,11),(24,10))
        for name,a,b in [('left',(14,20),(13,20)),('right',(34,20),(35,20)),('nw',(17,13),(16,12)),('ne',(31,13),(32,12))]:self.add_line('ray-'+name,a,b)
        self.add_bezier('front-hill',(6,32),((13,25),(25,25),(29,36)));self.relate('connect','frame','front-hill')
        self.add_bezier('back-hill',(27,32),((33,28),(38,31),(42,36)));self.relate('connect','frame','back-hill')

KEYSHAPE_REASON='The whole composition is approximately square; the centerline extremes are (6,6)–(42,42).'
