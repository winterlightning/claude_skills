"""An open folder with a broad upright back and skewed front.
Construction: folder-open. Minor corner fillets reduced to round joins.
Keyshape HRECT_L; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd7fb85d5-3ce1-5b14-bacb-ec568ad39a6c'
SOURCE_PATH = 'icon_set/work/todo-references/folder open_d7fb85d5-3ce1-5b14-bacb-ec568ad39a6c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folder-open'
    keyshape = Keyshape.HRECT_L
    # Declared visible-ink extrema: (2, 6, 46, 42).
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('folder', 'open')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def build(self):

        # Plan: tall tabbed back; front shares both lower-left and rear-right joints.
        self.add_polyline('back',(4,40),(4,8),(16,8),(22,14),(36,14),(36,22))
        self.add_polyline('front',(4,40),(4,28),(10,22),(44,22),(40,40),closed=True)
        self.relate('connect','back','front')
