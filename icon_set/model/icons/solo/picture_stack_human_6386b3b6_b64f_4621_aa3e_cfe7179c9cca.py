from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6386b3b6-b64f-4621-aa3e-cfe7179c9cca'
SOURCE_PATH='icon_set/work/todo-references/picture stack human_6386b3b6-b64f-4621-aa3e-cfe7179c9cca.svg'
AUTHOR='gpt-6'
PLAN='Stacked portrait pictures: front rounded panel with detached round head and smooth shoulders, rear panel visible at right.'
CONSTRUCTION_REFERENCES='Shared human-reference.md and human_ref/user.svg own head/shoulders; Lucide image supplies enclosure construction.'
OMISSIONS='Facial detail absent in source; none added. Rear picture is an exposed outline only.'
KEYSHAPE_INK_BOUNDS=(4, 4, 44, 44)

class Drawing(Solo48):
    icon_id='picture-stack-human'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'images'
    categories = ('images', 'primitives')
    aliases=()
    keywords=('picture', 'stack', 'human')

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
        self.box('front',6,6,28,36,6)
        self.add_arc('rear-top',(34,14),(42,22),radius_x=8)
        self.add_line('rear-side',(42,22),(42,26))
        self.add_arc('rear-bottom',(42,26),(34,34),radius_x=8)
        self.add_contour('rear','rear-top','rear-side','rear-bottom');self.relate('connect','front','rear')
        self.circle('head',20,19,4)
        self.add_bezier('shoulders',(12,42),((12,35),(15,31),(20,31)),((25,31),(28,35),(28,42)))
        self.relate('connect','front','shoulders')
        # Head bottom 23; shoulder apex 31: exactly 8 centerline / 4 ink.

KEYSHAPE_REASON='The whole composition is approximately square; the centerline extremes are (6,6)–(42,42).'
