"""An isometric compartmented cabinet with a disc beside its open lower-left face. Lucide box informs three-face geometry. Dense grid becomes one roof divider and one front divider; the disc becomes a small ring and the lower-left gap is enlarged. Intentional perspective asymmetry.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='12f31aef-e8cc-405f-837a-ad6a458b520c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__storage-cabinet-disc/20260927T155415Z-thuan-mac-1/reference/elemental mediastore_12f31aef-e8cc-405f-837a-ad6a458b520c.svg'
AUTHOR='gpt-6'

class StorageCabinetDisc(Solo48):
    icon_id='storage-cabinet-disc'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('storage', 'cabinet', 'media', 'box', 'disc', 'archive', 'shelves', 'store')

    def build(self) -> None:
        def ring(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        # The tall upright volume and its open lower-left corner follow the reference.
        self.add_polyline('cabinet',(6,26),(6,16),(24,6),(42,16),(42,34),(24,42))
        self.add_polyline('roof-seam',(6,16),(24,26),(42,16))
        self.add_line('front-edge',(24,26),(24,42))
        self.add_line('compartment-seam',(33,21),(33,38))
        join('cabinet','roof-seam','front-edge','compartment-seam')
        ring('disc',10,38,4)
