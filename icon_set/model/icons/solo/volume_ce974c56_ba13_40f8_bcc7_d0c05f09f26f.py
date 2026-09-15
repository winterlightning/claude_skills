'Speaker with two smooth sound waves: a consistent mouth silhouette and generous radial separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce974c56-ba13-40f8-bcc7-d0c05f09f26f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/volume_ce974c56-ba13-40f8-bcc7-d0c05f09f26f.svg'
AUTHOR = 'gpt-6'

class VolumeInterfaceEssential(Solo48):
    icon_id = 'volume-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('volume', 'interface-essential')

    def build(self) -> None:
        # Shared speaker silhouette and two concentric elliptical sound waves.
        self.add_polyline('speaker',(4,18),(12,18),(22,8),(22,40),(12,30),(4,30),closed=True)
        self.add_arc('wave-inner',(31,17),(31,31),radius_x=3,radius_y=7)
        self.add_arc('wave-outer',(38,12),(38,36),radius_x=6,radius_y=12)
