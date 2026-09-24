"""mobile phone plane: complete SOLO48 repair.
Retained the diagonal side-profile aircraft, with a swept fuselage and prominent wing joined at an exact shared node.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0a850f90-2953-422f-b95d-65062508b5a1'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone plane_0a850f90-2953-422f-b95d-65062508b5a1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-plane'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'plane')

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

        self.add_bezier('tail',(17,27),((20,28),(23,26),(25,24)))
        self.add_bezier('nose',(25,24),((28,21),(31,18),(31,14)))
        self.add_contour('fuselage','tail','nose')
        self.add_line('wing',(17,16),(25,24))
        self.relate('connect','fuselage','wing')
