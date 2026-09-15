"""Rebuilt mirrored horns and a broad circular jaw; retained both eyes and muzzle with proper clearance.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfa6681e-c282-4464-9e3f-8da4256d4f83'
SOURCE_PATH = 'pictographic-primitives/animals/buffalo_dfa6681e-c282-4464-9e3f-8da4256d4f83.svg'
AUTHOR = 'gpt-6'

class BuffaloHead(Solo48):
    icon_id = 'buffalo-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('buffalo', 'bison', 'head', 'horns', 'cattle', 'animal', 'wildlife', 'ox')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Mirrored horn quarters and broad round jaw.
        # Face stations leave a full eight-unit eye inset and a distinct muzzle.
        x,left,right,top,jaw_y,r=24,11,37,16,29,13
        self.add_arc('horn-left',(6,6),(left,top),radius_x=5,radius_y=10,sweep=False)
        self.add_line('brow',(left,top),(right,top))
        self.add_arc('horn-right',(right,top),(42,6),radius_x=5,radius_y=10,sweep=False)
        self.add_contour('horns','horn-left','brow','horn-right')
        self.add_line('left-cheek',(left,top),(left,jaw_y))
        self.add_arc('left-jaw',(left,jaw_y),(x,42),radius_x=r,sweep=False)
        self.add_arc('right-jaw',(x,42),(right,jaw_y),radius_x=r,sweep=False)
        self.add_line('right-cheek',(right,jaw_y),(right,top))
        self.add_contour('face','left-cheek','left-jaw','right-jaw','right-cheek')
        self.relate('connect','horns','face')
        for side,ex in [('left',20),('right',28)]:self.add_dot('eye-'+side,(ex,25))
        self.add_line('muzzle',(22,33),(26,33))
