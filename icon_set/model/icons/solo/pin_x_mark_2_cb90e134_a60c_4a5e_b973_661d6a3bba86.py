from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='cb90e134-a60c-4a5e-b973-661d6a3bba86'
SOURCE_PATH='icon_set/work/todo-references/pin x mark 2_cb90e134-a60c-4a5e-b973-661d6a3bba86.svg'
AUTHOR='gpt-6'
PLAN='Location pin with round hole over a small ground X. The narrow crossing stays centered on the tip.'
CONSTRUCTION_REFERENCES='Lucide map-pin: circular hole and tapered pin.'
OMISSIONS='Ground X compressed vertically to maintain the pin above it.'
KEYSHAPE_INK_BOUNDS=(8, 2, 40, 46)

class Drawing(Solo48):
    icon_id='pin-x-mark-2'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('pin', 'x', 'mark', '2')

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
        self.pin('pin',24,4,14,32)
        self.circle('hole',24,18,3)
        self.cross('ground-x',24,41,6,3)

KEYSHAPE_REASON='The narrow marker-and-ground composition uses centerline extremes (10,4)–(38,44).'
FINAL_REDUCTIONS='No components omitted. Pin aperture and vertical pin proportions reduced to make room for the ground X.'
