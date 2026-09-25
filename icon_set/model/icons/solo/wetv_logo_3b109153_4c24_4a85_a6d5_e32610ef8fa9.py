"""Rounded play triangle overlaps a narrow rear capsule. Preserve both loops with explicit shared points on the vertical play edge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b109153-4c24-4a85-a6d5-e32610ef8fa9'
SOURCE_PATH = 'pictographic-primitives/logos/wetv logo_3b109153-4c24-4a85-a6d5-e32610ef8fa9.svg'
AUTHOR = 'gpt-6'

class WetvLogo(Solo48):
    icon_id = 'wetv-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('wetv', 'tencent', 'streaming', 'play', 'logo', 'brand', 'video')

    def build(self):
        # Plan: Rounded play triangle overlaps a narrow rear capsule. Preserve both loops with explicit shared points on the vertical play edge.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_bezier('play-round',(18,8),((24,8),(44,20),(44,24)),((44,28),(24,40),(18,40)),((14,40),(14,36),(14,32)))
        self.add_line('play-left',(14,32),(14,16))
        self.add_bezier('play-top',(14,16),((14,12),(14,8),(18,8)))
        self.add_contour('play','play-round','play-left','play-top',closed=True)
        self.add_bezier('rear',(14,16),((4,10),(4,16),(4,24)),((4,32),(4,38),(14,32)))
        self.relate('connect','play','rear')

