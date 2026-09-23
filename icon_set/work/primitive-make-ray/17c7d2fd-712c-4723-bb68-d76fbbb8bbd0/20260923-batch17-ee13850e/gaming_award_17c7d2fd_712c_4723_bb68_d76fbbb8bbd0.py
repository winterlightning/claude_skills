"""An open laurel wreath with three leaves on each crossing branch.
SOLO48 SQUARE; geometry authored independently from the rendered reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '17c7d2fd-712c-4723-bb68-d76fbbb8bbd0'
SOURCE_PATH = 'icon_set/work/todo-references/gaming award_17c7d2fd-712c-4723-bb68-d76fbbb8bbd0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'gaming-award'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/award'
    aliases = ()
    keywords = ('gaming', 'award')

    def line(self, n, a, b):
        self.add_line(n,a,b)

    def arc(self,n,a,b,rx,ry=None,sweep=True):
        self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)

    def rect(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.arc(f"{n}-{i}",a,b,r)
            else:self.line(f"{n}-{i}",a,b)
        self.add_contour(n,*(f"{n}-{i}" for i in range(8)),closed=True)

    def build(self):
        # Plan: paired branches reflected about x=24; three pointed leaves per side.
        axis=24
        for side in (-1,1):
            p=lambda x,y:(axis+side*x,y)
            n='left' if side<0 else 'right'
            self.arc(n+'-stem',p(12,16),p(-10,42),28,28,side>0)
            leaves=[((12,16),(12,6),5,8),((15,24),(18,18),6,6),((10,33),(18,31),6,6)]
            for i,(a,b,rx,ry) in enumerate(leaves):
                self.arc(f'{n}-leaf{i}a',p(*a),p(*b),rx,ry,True)
                self.arc(f'{n}-leaf{i}b',p(*b),p(*a),rx,ry,True)
                self.add_contour(f'{n}-leaf{i}',f'{n}-leaf{i}a',f'{n}-leaf{i}b',closed=True)
            self.relate('connect',n+'-stem',n+'-leaf0')
        self.relate('connect','left-stem','right-stem')
