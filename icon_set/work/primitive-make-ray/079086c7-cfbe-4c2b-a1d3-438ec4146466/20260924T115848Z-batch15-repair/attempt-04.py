"""A mobile phone displaying skull icon.
Construction reference: smartphone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '079086c7-cfbe-4c2b-a1d3-438ec4146466'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone skull_079086c7-cfbe-4c2b-a1d3-438ec4146466.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-skull'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'skull')

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
        self.add_arc('cranium-left',(16,20),(24,12),radius_x=8)
        self.add_arc('cranium-right',(24,12),(32,20),radius_x=8)
        self.add_arc('eye-right-base',(32,20),(24,20),radius_x=4)
        self.add_arc('eye-left-base',(24,20),(16,20),radius_x=4)
        self.add_contour('cranium','cranium-left','cranium-right','eye-right-base','eye-left-base',closed=True)
        self.add_line('bridge',(24,12),(24,20))
        self.relate('connect','cranium','bridge')
        self.add_polyline('jaw-left',(16,20),(16,28),(20,32),(20,34))
        self.add_polyline('jaw-right',(32,20),(32,28),(28,32),(28,34))
        self.relate('connect','cranium','jaw-left')
        self.relate('connect','cranium','jaw-right')
