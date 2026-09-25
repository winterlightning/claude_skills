"""A circular seal with an inset rim and a broad forked banner.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide award (concentric badge hierarchy): geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='cb339990-49e6-46a8-ad97-83dd4ad21af5'
SOURCE_PATH='pictographic-primitives/rewards/intellectual property and tradmark_cb339990-49e6-46a8-ad97-83dd4ad21af5.svg'
AUTHOR='gpt-6'

class CircularEmblemWithBanner(Solo48):
    icon_id='circular-emblem-with-banner'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('award', 'reward', 'circular-emblem-with-banner')
    def build(self) -> None:
        self.add_arc('outer',(8,26),(40,26),radius_x=16,radius_y=20)
        self.add_arc('inner',(17,26),(31,26),radius_x=7,radius_y=11)
        self.add_polyline('banner',(6,26),(8,26),(17,26),(31,26),(40,26),(42,26),(36,34),(42,42),(6,42),(12,34),closed=True)
        self.relate('connect','outer','banner')
        self.relate('connect','inner','banner')
