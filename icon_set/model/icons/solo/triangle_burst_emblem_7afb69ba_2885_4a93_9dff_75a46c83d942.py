"""Five outward triangular lobes around a vertical stem. Four remain closed; the smallest lower-right lobe becomes an open chevron to avoid an undersized hole. Crossing diagonals reduce to shared central tips. No useful exact local Lucide match; mirrored middle lobes and intentional asymmetric upper/lower flags preserve the abstract emblem.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7afb69ba-2885-4a93-9dff-75a46c83d942'
SOURCE_PATH='pictographic-primitives/programing/interactive video service_7afb69ba-2885-4a93-9dff-75a46c83d942.svg'
AUTHOR='gpt-6'

class TriangleBurstEmblem(Solo48):
    icon_id='triangle-burst-emblem'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('triangles', 'video', 'interactive', 'emblem', 'play', 'burst', 'media', 'abstract')

    def build(self) -> None:
        def ring(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)

        def node(name,x,y,w,h):
            self.add_polyline(name,(x,y),(x+w//2,y),(x+w,y),(x+w,y+h),(x+w//2,y+h),(x,y+h),closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        self.add_polyline('upper-flag',(24,4),(36,9),(24,14),closed=True)
        self.add_polyline('left-triangle',(8,18),(24,24),(8,30),closed=True)
        self.add_polyline('right-triangle',(40,18),(40,30),(24,24),closed=True)
        self.add_polyline('lower-flag',(24,34),(24,44),(8,39),closed=True)
        self.add_polyline('small-lobe',(32,36),(40,40),(32,44))
        self.add_line('upper-stem',(24,14),(24,24))
        self.add_line('lower-stem',(24,24),(24,34))
        join('upper-flag','upper-stem')
        join('lower-flag','lower-stem')
        join('upper-stem','lower-stem','left-triangle','right-triangle')
