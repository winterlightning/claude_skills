"""A crouching person shelters beneath a table with earthquake marks above.
Construction reference: human_ref/full_body_ref.png: crouching pose and coherent limbs. No useful exact Lucide scene match.
Reduction: The original continuous head-and-back silhouette is retained; no detached head is introduced. Small folds reduced.
Keyshape: SQUARE; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d2595e2-135f-48bd-8886-08c5da475869'
SOURCE_PATH = 'icon_set/work/todo-references/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'earthquake-hiding-proof-table'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('earthquake', 'hiding', 'proof', 'table')

    def path(self, name, start, segments, closed=False):
        members = []
        for i, spec in enumerate(segments):
            part = f"{name}-{i+1}"
            if len(spec) == 2:
                end = spec
                self.add_line(part, start, end)
            else:
                end, rx, ry, sweep = spec
                self.add_arc(part, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
            members.append(part)
            start = end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [((x+r,y),r,r,True),((x-r,y),r,r,True)], True)

    def rect(self, name, x, y, w, h, r=3):
        self.path(name, (x+r,y), [(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)], True)

    def build(self):
        # Plan: tabletop and two legs shelter a continuous crouched silhouette.
        # Human reference: icon_set/references/human_ref/full_body_ref.png.
        # Supplied pose has no detached circular head; the upper outline includes head/back.
        self.rect('tabletop',6,16,36,8,3)
        for x in (8,40):
            self.add_line(f'table-leg-{x}',(x,24),(x,42))
            self.relate('connect',f'table-leg-{x}','tabletop')
        for side in (-1,1):
            self.add_polyline(f'tremor-{side}',(24+side*18,10),(24+side*15,6),(24+side*11,10),(24+side*8,6))
        self.path('crouched-body',(34,39),[((31,36),3,3,False),(31,31),((27,27),4,4,False),(17,27),((13,31),4,4,False),(18,38),(14,38),((14,42),2,2,False),(21,42),((24,38),4,4,False),(21,32),(27,32),(25,39),(28,42)])
