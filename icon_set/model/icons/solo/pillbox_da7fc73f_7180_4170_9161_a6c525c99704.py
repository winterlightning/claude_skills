"""Pillbox with a lid seam and medical plus.
Plan: SQUARE fits the box and centered medical symbol.
Reduction: Corner radius reduced and lid seam lowered slightly; no identifying feature omitted.
Construction: monitor: coherent rounded rectangle construction. Lid attachments are explicit wall nodes; medical cross has shared center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='da7fc73f-7180-4170-9161-a6c525c99704'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pillbox_da7fc73f-7180-4170-9161-a6c525c99704.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='pillbox'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('pillbox',)

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
            elif a[0]==b[0] and min(a[1],b[1])<15<max(a[1],b[1]):
                members.pop()
                self.add_line(part+'-a',a,(a[0],15));self.add_line(part+'-b',(a[0],15),b)
                members.extend((part+'-a',part+'-b'))
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
        self.box('box',6,6,36,36,4)
        self.add_line('lid',(6,15),(42,15));self.relate('connect','box','lid')
        self.cross('medical-plus',24,28,5,5,False)

