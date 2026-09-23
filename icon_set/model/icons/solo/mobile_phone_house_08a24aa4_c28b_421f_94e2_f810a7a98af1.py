"""A mobile phone displaying house icon.
Construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08a24aa4-c28b-421f-94e2-f810a7a98af1'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone house_08a24aa4-c28b-421f-94e2-f810a7a98af1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-house'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'house')

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

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Single mirrored house contour, with no door in the reference.
        self.add_polyline('house',(17,28),(17,20),(24,13),(31,20),(31,28),closed=True)
