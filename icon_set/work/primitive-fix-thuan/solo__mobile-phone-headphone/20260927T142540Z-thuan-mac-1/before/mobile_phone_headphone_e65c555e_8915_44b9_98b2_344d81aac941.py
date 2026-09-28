"""mobile phone headphone: complete SOLO48 repair.
Retained the arched headband and two downward ear ends; replaced the tiny outlined ear cushions with open stroke terminals.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e65c555e-8915-44b9-98b2-344d81aac941'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone headphone_e65c555e-8915-44b9-98b2-344d81aac941.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-headphone'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('mobile', 'phone', 'headphone')

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
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')
        self.add_arc('headband',(17,22),(31,22),radius_x=7)
        self.add_line('ear-left',(17,22),(17,28))
        self.add_line('ear-right',(31,22),(31,28))
        self.relate('connect','headband','ear-left')
        self.relate('connect','headband','ear-right')
