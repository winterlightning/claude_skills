'Speaker with two smooth sound waves: a consistent mouth silhouette and generous radial separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa52487-9375-4e6d-9147-20a9cf6027d3'
SOURCE_PATH = 'icons-json/audio/volume control medium 1_ffa52487-9375-4e6d-9147-20a9cf6027d3.json'
AUTHOR = 'gpt-6'

class VolumeControlMedium1(Solo48):
    icon_id = 'volume-control-medium-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'medium', 'audio')

    def build(self) -> None:
        # Shared speaker silhouette and two concentric elliptical sound waves.
        self.add_polyline('speaker',(4,18),(12,18),(22,8),(22,40),(12,30),(4,30),closed=True)
        self.add_arc('wave-inner',(31,17),(31,31),radius_x=3,radius_y=7)
        self.add_arc('wave-outer',(38,12),(38,36),radius_x=6,radius_y=12)
