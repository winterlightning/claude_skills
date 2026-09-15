'Camera: preserve raised viewfinder and circular lens; replace stretched ellipse and uneven body corners. Lucide camera reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6140d8-fbbf-56b5-a986-e3da6351b189'
SOURCE_PATH = 'pictographic-primitives/photography/camera_1d6140d8-fbbf-56b5-a986-e3da6351b189.svg'
AUTHOR = 'gpt-6'

class CameraPhotography(Solo48):
    icon_id = 'camera-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('camera', 'photography')

    def build(self) -> None:
        # Shared axis x=24: raised viewfinder, tangent body corners and a round lens.
        self.add_line('top-a',(8,12),(14,12))
        self.add_line('top-b',(14,12),(17,8))
        self.add_line('top-c',(17,8),(31,8))
        self.add_line('top-d',(31,8),(34,12))
        self.add_line('top-e',(34,12),(40,12))
        self.add_arc('tr',(40,12),(44,16),radius_x=4)
        self.add_line('right',(44,16),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,16))
        self.add_arc('tl',(4,16),(8,12),radius_x=4)
        self.add_contour('body','top-a','top-b','top-c','top-d','top-e','tr','right','br','bottom','bl','left','tl',closed=True)

        self.add_arc('lens-top', (17,24), (31,24), radius_x=7, radius_y=7)
        self.add_arc('lens-bottom', (31,24), (17,24), radius_x=7, radius_y=7)
        self.add_contour('lens', 'lens-top', 'lens-bottom', closed=True)
