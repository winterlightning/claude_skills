"""An iPod-like player has a triangular play control above a circular button.
Construction reference: tablet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95b0fd3b-05a5-49bd-b7c9-29486aaf4857'
SOURCE_PATH = 'icon_set/work/todo-references/ipod play_95b0fd3b-05a5-49bd-b7c9-29486aaf4857.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'ipod-play'
    keyshape = Keyshape.VRECT_L
    # Visible ink extremes: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('ipod', 'play')

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

        # Plan: upright rounded rectangle split into display and lower button band.
        self.rect('body',8,4,32,40)
        self.add_line('separator',(8,28),(40,28))
        self.relate('connect','body','separator')
        self.add_polyline('play',(18,12),(28,18),(18,24),closed=True)
        self.circle('button',24,36,3)
