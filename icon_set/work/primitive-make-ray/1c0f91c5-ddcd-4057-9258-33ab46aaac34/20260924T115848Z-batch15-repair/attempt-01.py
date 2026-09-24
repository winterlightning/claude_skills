"""A mobile phone displays a euro sign.
Construction reference: smartphone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1c0f91c5-ddcd-4057-9258-33ab46aaac34'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-euro-sign'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'euro', 'sign')

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
        self.rect('phone',8,4,32,40)
        self.add_bezier('euro-upper',(31,13),((23,10),(17,14),(17,22)))
        self.add_bezier('euro-lower',(17,22),((17,30),(23,34),(31,31)))
        self.add_contour('euro','euro-upper','euro-lower')
        self.add_line('euro-bar',(17,22),(27,22))
        self.relate('connect','euro','euro-bar')
