"""A mobile phone displays a notification bell.
Construction reference: smartphone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '819857f6-7191-4e86-8585-718826dd7d33'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone bell_819857f6-7191-4e86-8585-718826dd7d33.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-bell'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'bell')

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

        # Shared symbol plan: upright phone, lower band, individually authored content.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Bell dome is a semicircle with tangent vertical sides.
        self.add_line('bell-left',(18,28),(18,22))
        self.add_arc('bell-dome',(18,22),(30,22),radius_x=6)
        self.add_line('bell-right',(30,22),(30,28))
        self.add_line('bell-base',(30,28),(18,28))
        self.add_contour('bell','bell-left','bell-dome','bell-right','bell-base',closed=True)
        self.add_line('crown',(24,13),(24,16))
        self.relate('connect','bell','crown')
