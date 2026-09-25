"""mobile phone music note: complete SOLO48 repair.
Retained the round note head, upright stem and single flag; shortened the flag to clear the head.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9541eb00-a034-4794-a052-1575ee33b845'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone music note_9541eb00-a034-4794-a052-1575ee33b845.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-music-note'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('mobile', 'phone', 'music', 'note')

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
            else:
                cuts=[a,b]
                if name=='phone' and a[0]==b[0] and min(a[1],b[1])<36<max(a[1],b[1]):
                    cuts=[a,(a[0],36),b]
                if len(cuts)==3:
                    self.add_line(n+'a',cuts[0],cuts[1]);self.add_line(n+'b',cuts[1],cuts[2])
                    names.extend([n+'a',n+'b']);continue
                self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # One note head, upright stem, and a flowing flag.
        self.circle('note-head',20,25,3)
        self.add_line('note-stem',(23,25),(23,13))
        self.add_bezier('flag',(23,13),((25,15),(31,14),(30,19)))
        self.relate('connect','note-head','note-stem')
        self.relate('connect','note-stem','flag')
