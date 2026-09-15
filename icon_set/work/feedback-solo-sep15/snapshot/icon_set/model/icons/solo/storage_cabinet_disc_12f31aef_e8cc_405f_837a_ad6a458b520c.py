"""An isometric compartmented cabinet with a disc beside its open lower-left face. Lucide box informs three-face geometry. Dense grid becomes one roof divider and one front divider; the disc becomes a small ring and the lower-left gap is enlarged. Intentional perspective asymmetry.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='12f31aef-e8cc-405f-837a-ad6a458b520c'
SOURCE_PATH='pictographic-primitives/programing/elemental mediastore_12f31aef-e8cc-405f-837a-ad6a458b520c.svg'
AUTHOR='gpt-6'

class StorageCabinetDisc(Solo48):
    icon_id='storage-cabinet-disc'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('storage', 'cabinet', 'media', 'box', 'disc', 'archive', 'shelves', 'store')

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

        self.add_polyline('cabinet',(4,24),(4,18),(14,13),(24,8),(44,18),(44,30),(34,35),(24,40))
        self.add_line('face-left',(4,18),(24,28))
        self.add_polyline('face-right',(44,18),(34,23),(24,28))
        self.add_line('front-corner',(24,28),(24,40))
        join('face-left','face-right','front-corner')
        for member in ('face-left','face-right','front-corner'): join('cabinet',member)
        self.add_line('top-divider',(14,13),(34,23))
        self.add_line('front-divider',(34,23),(34,35))
        join('top-divider','cabinet')
        join('front-divider','cabinet')
        join('top-divider','front-divider','face-right')
        ring('disc',10,35,3)
