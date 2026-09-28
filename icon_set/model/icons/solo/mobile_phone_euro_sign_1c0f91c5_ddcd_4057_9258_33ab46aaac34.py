"""Revision of the claimed reference after comparing original and rejected drawing."""
"""mobile phone euro sign: complete SOLO48 repair.
Opened the euro curve and joined its crossbar at an explicit curve endpoint. Removed the lower phone divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c0f91c5-ddcd-4057-9258-33ab46aaac34'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-euro-sign/20260927T142529Z-thuan-mac-1/reference/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-euro-sign'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('mobile', 'phone', 'euro', 'sign')

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
        # Restored bottom bezel and moved the euro sign clear of it.
        self.rect('phone',8,4,32,40)
        self.add_line('bezel',(8,36),(40,36)); self.relate('connect','phone','bezel')
        self.add_bezier('euro-upper',(31,14),((23,12),(17,15),(17,21)))
        self.add_bezier('euro-lower',(17,21),((17,26),(23,28),(31,26)))
        self.add_contour('euro','euro-upper','euro-lower')
        self.add_line('euro-bar',(17,21),(27,21)); self.relate('connect','euro','euro-bar')
