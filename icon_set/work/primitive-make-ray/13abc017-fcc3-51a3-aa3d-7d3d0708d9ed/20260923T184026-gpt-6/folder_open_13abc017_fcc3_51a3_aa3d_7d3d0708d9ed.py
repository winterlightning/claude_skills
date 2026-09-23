"""An open folder with a tab on its front panel.
Construction: folder-open. Small rounded corner transitions become round joins.
Keyshape HRECT_L; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '13abc017-fcc3-51a3-aa3d-7d3d0708d9ed'
SOURCE_PATH = 'icon_set/work/todo-references/folder open_13abc017-fcc3-51a3-aa3d-7d3d0708d9ed.svg'
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

        # Plan: detached rear lip above a broad, tapered tabbed front.
        self.add_polyline('rear',(8,8),(40,8),(40,16))
        self.add_polyline('front',(4,18),(16,18),(20,26),(44,26),(40,40),(8,40),closed=True)
