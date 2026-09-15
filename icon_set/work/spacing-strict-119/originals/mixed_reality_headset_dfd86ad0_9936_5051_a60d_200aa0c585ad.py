"""Wide visor with central nose indentation and right strap. Consistent circular corners informed by Lucide smartphone; intentional right-side connector."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfd86ad0-9936-5051-a60d-200aa0c585ad'
SOURCE_PATH = 'pictographic-primitives/technology/apple vision pro_dfd86ad0-9936-5051-a60d-200aa0c585ad.svg'
AUTHOR = 'gpt-6'

class MixedRealityHeadset(Solo48):
    icon_id = 'mixed-reality-headset'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('headset', 'mixed-reality', 'vision-pro', 'visor', 'spatial', 'vr', 'ar', 'goggles')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('top',(14, 8),(30, 8))
        self.add_bezier('tr',(30, 8),*(((35.90355937, 8), (41.5, 12.4771525), (42, 18)),))
        self.add_line('right',(42, 18),(42, 30))
        self.add_bezier('br',(42, 30),*(((41.5, 35.5228475), (35.90355937, 40), (30, 40)),))
        self.add_arc('nose-r',(30, 40),(22, 36),radius_x=10,radius_y=10,large_arc=False,sweep=True)
        self.add_arc('nose-l',(22, 36),(14, 40),radius_x=10,radius_y=10,large_arc=False,sweep=True)
        self.add_bezier('bl',(14, 40),*(((8.08595979, 39.03526374), (4, 34.82760764), (4, 30)),))
        self.add_line('left',(4, 30),(4, 18))
        self.add_bezier('tl',(4, 18),*(((4, 13.17239236), (8.08595979, 8.96473626), (14, 8)),))
        self.add_line('strap',(42, 23),(44, 23))
        self.add_contour('visor',*('top', 'tr', 'right', 'br', 'nose-r', 'nose-l', 'bl', 'left', 'tl'),closed=True)
        self.relate('connect',*('strap', 'visor'))
