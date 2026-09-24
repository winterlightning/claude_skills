"""A mobile phone displaying skull icon.
Construction reference: smartphone.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
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

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Bilateral skull dome, cheek transitions and open jaw strokes.
        self.add_arc('skull-top',(17,20),(31,20),radius_x=7)
        self.add_bezier('cheek-right',(31,20),((31,24),(28,24),(28,26)))
        self.add_line('jaw-right',(28,26),(28,29))
        self.add_bezier('cheek-left',(20,26),((20,24),(17,24),(17,20)))
        self.add_line('jaw-left',(20,29),(20,26))
        self.add_line('jaw-center',(24,27),(24,29))
        self.add_contour('skull','jaw-left','cheek-left','skull-top','cheek-right','jaw-right')
        for x in (21,27):self.add_dot('eye-'+str(x),(x,20))
