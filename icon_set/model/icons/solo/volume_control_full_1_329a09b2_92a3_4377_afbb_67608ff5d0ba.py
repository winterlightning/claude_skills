'Speaker with two smooth sound waves: a consistent mouth silhouette and generous radial separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '329a09b2-92a3-4377-afbb-67608ff5d0ba'
SOURCE_PATH = 'icons-json/audio/volume control full 1_329a09b2-92a3-4377-afbb-67608ff5d0ba.json'
AUTHOR = 'gpt-6'

class VolumeControlFull1(Solo48):
    icon_id = 'volume-control-full-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'full', 'audio')

    def build(self) -> None:
        # Shared speaker silhouette and two concentric elliptical sound waves.
        self.add_polyline('speaker',(4,18),(12,18),(22,8),(22,40),(12,30),(4,30),closed=True)
        self.add_arc('wave-inner',(31,17),(31,31),radius_x=3,radius_y=7)
        self.add_arc('wave-outer',(38,12),(38,36),radius_x=6,radius_y=12)
