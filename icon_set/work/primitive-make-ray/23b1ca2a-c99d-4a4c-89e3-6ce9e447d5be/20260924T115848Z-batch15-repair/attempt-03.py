from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be'
SOURCE_PATH = 'icon_set/work/todo-references/Mobile Phone Cube_23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mobile-phone-cube'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('Mobile Phone Cube',)

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
        self.add_polyline('phone',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.add_polyline('cube',(24,12),(32,17),(32,27),(24,32),(16,27),(16,17),closed=True)
        self.add_polyline('top-seam',(16,17),(24,22),(32,17))
        self.add_line('front-seam',(24,22),(24,32))
        self.relate('connect','cube','top-seam')
        self.relate('connect','cube','front-seam')
        self.relate('connect','top-seam','front-seam')
