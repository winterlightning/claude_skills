"""A mobile phone displaying phone icon.
Construction reference: smartphone.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13ea825f-ae04-4150-a4b6-56b3bed9dc5d'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone phone_13ea825f-ae04-4150-a4b6-56b3bed9dc5d.svg'
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

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Curved handset with deliberately unequal terminal orientations.
        self.add_bezier('handset',(17,14),((14,18),(26,31),(31,27)))
        self.add_line('terminal-right-1',(31,27),(28,23))
        self.add_line('terminal-right-2',(28,23),(24,26))
        self.add_bezier('handset-inner',(24,26),((21,24),(20,23),(19,20)))
        self.add_line('terminal-left-1',(19,20),(22,17))
        self.add_line('terminal-left-2',(22,17),(19,13))
        self.add_line('terminal-left-3',(19,13),(17,14))
        self.add_contour('receiver','handset','terminal-right-1','terminal-right-2','handset-inner','terminal-left-1','terminal-left-2','terminal-left-3',closed=True)
