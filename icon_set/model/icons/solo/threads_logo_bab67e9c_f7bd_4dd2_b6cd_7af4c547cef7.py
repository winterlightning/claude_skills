"""Tall looping at-like stroke with an inner counter and sweeping outer return. Use coherent cubics and shared loop junctions; retain the intentional asymmetric spiral."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bab67e9c-f7bd-4dd2-b6cd-7af4c547cef7'
SOURCE_PATH = 'pictographic-primitives/logos/thread logo_bab67e9c-f7bd-4dd2-b6cd-7af4c547cef7.svg'
AUTHOR = 'gpt-6'

class ThreadsLogo(Solo48):
    icon_id = 'threads-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('threads', 'meta', 'social', 'at-sign', 'logo', 'brand', 'instagram')

    def build(self):
        # Plan: Tall looping at-like stroke with an inner counter and sweeping outer return. Use coherent cubics and shared loop junctions; retain the intentional asymmetric spiral.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_bezier('outer',(40,17),((40,8),(33,4),(24,4)),((13,4),(8,13),(8,24)),((8,36),(14,44),(26,44)),((34,44),(40,40),(40,33)),((40,26),(34,23),(29,23)))
        self.add_bezier('loop',(29,23),((22,23),(18,26),(18,31)),((18,36),(30,38),(30,29)),((30,21),(30,15),(24,15)),((21,15),(19,16),(18,18)))
        self.add_contour('thread','outer','loop')

