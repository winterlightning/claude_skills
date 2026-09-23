"""A rectangular picture frame with an inset rectangular opening.
Construction: none. None; both concentric rectangles retained.
Keyshape VRECT_L; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a28d2c15-57a6-4f2e-bd21-647c70fa234d'
SOURCE_PATH = 'icon_set/work/todo-references/frame_a28d2c15-57a6-4f2e-bd21-647c70fa234d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'frame'
    keyshape = Keyshape.VRECT_L
    # Declared visible-ink extrema: (6, 2, 42, 46).
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('frame',)

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

        # Plan: two concentric rectangles with a shared 8-unit centerline inset.
        x,y,w,h=8,4,32,40
        self.add_polyline('outer',(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
        inset=8
        self.add_polyline('inner',(x+inset,y+inset),(x+w-inset,y+inset),
                          (x+w-inset,y+h-inset),(x+inset,y+h-inset),closed=True)
