"""Three joined keyboard keys show up, left and right arrows.
Construction reference: none.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42a2cdda-9bae-4c47-b68a-7075bb296796'
SOURCE_PATH = 'icon_set/work/todo-references/keyboard button direction_42a2cdda-9bae-4c47-b68a-7075bb296796.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'keyboard-button-direction'
    keyshape = Keyshape.SQUARE
    # Visible ink extremes: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'button', 'direction')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: three equal directional cells in a T arrangement, sharing the top joint.
        self.add_polyline('keys',(16,6),(32,6),(32,24),(42,24),(42,42),(26,42),(26,24),(22,24),(22,42),(6,42),(6,24),(16,24),closed=True)
        for name,points in [('up',[(24,20),(24,12)]),('left',[(18,33),(10,33)]),('right',[(30,33),(38,33)])]:
            self.add_polyline(name,*points)
        self.add_polyline('up-tip',(20,16),(24,12),(28,16))
        self.add_polyline('left-tip',(14,29),(10,33),(14,37))
        self.add_polyline('right-tip',(34,29),(38,33),(34,37))
        for n in ('up','left','right'):self.relate('connect',n,n+'-tip')
