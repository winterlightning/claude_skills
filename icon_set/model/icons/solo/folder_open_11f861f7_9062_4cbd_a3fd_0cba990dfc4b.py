"""An open folder with an angled front flap.
Construction: folder-open. Tiny corner fillets on the sloping flap are reduced to round joins.
Keyshape HRECT_L; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '11f861f7-9062-4cbd-a3fd-0cba990dfc4b'
SOURCE_PATH = 'icon_set/work/todo-references/folder open_11f861f7-9062-4cbd-a3fd-0cba990dfc4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folder-open'
    keyshape = Keyshape.HRECT_L
    # Declared visible-ink extrema: (2, 6, 46, 42).
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "folders"
    categories = ("folders", "primitives")
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

        # Plan: tabbed back wall and a tilted front panel sharing the lower left.
        self.add_polyline('back',(4,40),(4,8),(16,8),(22,14),(36,14),(36,22))
        self.add_polyline('front',(4,40),(12,22),(44,22),(40,40),closed=True)
        self.relate('connect','back','front')
