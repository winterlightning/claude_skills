"""mobile phone pound sign: complete SOLO48 repair.
Rebuilt the sterling sign with a round hook, explicit crossbar junction and level baseline. Removed the lower phone divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a70db137-a446-4f4c-b656-4fea14660981'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone pound sign_a70db137-a446-4f4c-b656-4fea14660981.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-pound-sign'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'pound', 'sign')

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
        self.rect('phone',8,4,32,40)
        self.add_arc('hook',(30,17),(22,17),radius_x=4,sweep=False)
        self.add_line('upper',(22,17),(22,23))
        self.add_line('lower',(22,23),(22,32))
        self.add_contour('pound','hook','upper','lower')
        self.add_polyline('bar',(17,23),(22,23),(28,23))
        self.add_polyline('foot',(17,32),(22,32),(31,32))
        self.relate('connect','pound','bar')
        self.relate('connect','pound','foot')
