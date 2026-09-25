from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='67a3758e-aa06-455b-bb00-226525eeddc2'
SOURCE_PATH='icon_set/work/todo-references/pill with checkmark and x_67a3758e-aa06-455b-bb00-226525eeddc2.svg'
AUTHOR='gpt-6'
PLAN='Horizontal capsule split diagonally, checkmark in left half and X in right half. Capsule end radii match.'
CONSTRUCTION_REFERENCES='Lucide pill: tangent capsule ends and diagonal division.'
OMISSIONS='No defining glyphs omitted.'
KEYSHAPE_INK_BOUNDS=(2, 8, 46, 40)

class Drawing(Solo48):
    icon_id='pill-with-checkmark-and-x'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'state'
    categories = ('state',)
    aliases=()
    keywords=('pill', 'with', 'checkmark', 'and', 'x')

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
        self.add_line('pill-top',(18,10),(30,10))
        self.add_arc('pill-right',(30,10),(30,38),radius_x=14)
        self.add_line('pill-bottom',(30,38),(18,38))
        self.add_arc('pill-left',(18,38),(18,10),radius_x=14)
        self.add_contour('pill','pill-top','pill-right','pill-bottom','pill-left',closed=True)
        self.add_line('split',(27,10),(21,38));self.relate('connect','pill','split')
        self.add_polyline('check',(10,24),(14,28),(20,20))
        self.cross('x',33,24,3,4)

KEYSHAPE_REASON='The capsule uses a wide 40×28 centerline envelope, (4,10)–(44,38).'
