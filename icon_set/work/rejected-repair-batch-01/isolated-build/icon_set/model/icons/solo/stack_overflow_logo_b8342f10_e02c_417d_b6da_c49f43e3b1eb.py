"""Open tray with four rising bars on a fanning series. Reduce outlined bars to monoline strokes and maintain the recognizable upward clockwise fan."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8342f10-e02c-417d-b6da-c49f43e3b1eb'
SOURCE_PATH = 'pictographic-primitives/logos/stack overflow logo_b8342f10-e02c-417d-b6da-c49f43e3b1eb.svg'
AUTHOR = 'gpt-6'

class StackOverflowLogo(Solo48):
    icon_id = 'stack-overflow-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('stack-overflow', 'developer', 'questions', 'stack', 'logo', 'brand', 'community')

    def build(self):
        # Plan: Open tray with four rising bars on a fanning series. Reduce outlined bars to monoline strokes and maintain the recognizable upward clockwise fan.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('tray',(8,32),(8,44),(32,44),(32,32))
        for j,(a,b) in enumerate([((16,35),(24,35)),((12,23),(25,26)),((20,13),(32,20)),((30,4),(40,12))]):self.add_line('bar-'+str(j),a,b)

