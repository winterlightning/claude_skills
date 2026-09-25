"""mobile phone phone: complete SOLO48 repair.
Retained the curved telephone receiver with two turned terminals; reduced its crowded double outline to an open receiver stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13ea825f-ae04-4150-a4b6-56b3bed9dc5d'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone phone_13ea825f-ae04-4150-a4b6-56b3bed9dc5d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-phone'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'phone')

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

        # Open receiver silhouette keeps both ear terminals without tiny pockets.
        self.add_line('earpiece',(22,14),(17,14))
        self.add_bezier('receiver',(17,14),((17,23),(22,28),(31,28)))
        self.add_line('mouthpiece',(31,28),(31,23))
        self.add_contour('handset','earpiece','receiver','mouthpiece')
