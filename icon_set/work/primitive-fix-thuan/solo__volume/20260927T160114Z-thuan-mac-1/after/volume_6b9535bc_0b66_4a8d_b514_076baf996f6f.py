'Speaker with two smooth sound waves: a consistent mouth silhouette and generous radial separation.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b9535bc-0b66-4a8d-b514-076baf996f6f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__volume/20260927T160114Z-thuan-mac-1/reference/volume_6b9535bc-0b66-4a8d-b514-076baf996f6f.svg'
AUTHOR = 'gpt-6'

class Volume(Solo48):
    icon_id = 'volume'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('volume', 'interface-essential')

    def build(self) -> None:
        # Shared speaker silhouette and two concentric elliptical sound waves.
        self.add_bezier('speaker',(22,8),((22,18),(22,30),(22,40)),((18,36),(15,33),(12,30)),((7,30),(4,31),(4,26)),((4,22),(4,18),(8,18)),((10,18),(11,18),(12,18)),((16,15),(19,11),(22,8)))
        self.add_contour('speaker-outline','speaker',closed=True)
        self.add_arc('wave-inner',(31,17),(31,31),radius_x=3,radius_y=7)
        self.add_arc('wave-outer',(38,12),(38,36),radius_x=6,radius_y=12)
