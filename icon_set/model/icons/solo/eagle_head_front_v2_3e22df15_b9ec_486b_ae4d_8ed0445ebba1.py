"""Inset the feather hem; joined the paired brows to an open hooked beak to remove crowding. Small closed beak removed.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: bird: coherent head curve and reduced beak; no exact front eagle match.
"""
# Independent repair of eagle-head-front; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e22df15-b9ec-486b-ae4d-8ed0445ebba1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle head_3e22df15-b9ec-486b-ae4d-8ed0445ebba1.svg'
AUTHOR = 'gpt-6'

class EagleHeadFrontVariant2(Solo48):
    icon_id = 'eagle-head-front-v2'
    variant_of = 'eagle-head-front'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('eagle', 'head', 'front', 'beak', 'feathers', 'raptor', 'bird', 'wildlife')

    def build(self) -> None:
        # SQUARE centerlines (6,6)-(42,42). Mirrored dome and three broad
        # feather lobes; brows meet a shared angular beak rather than crowd it.
        axis, shoulder, hem = 24, 24, 38
        self.add_arc('dome-left',(6,24),(24,6),radius_x=18)
        self.add_arc('dome-right',(24,6),(42,24),radius_x=18)
        self.add_line('side-right',(42,24),(42,38))
        self.add_arc('feather-right',(42,38),(30,38),radius_x=6,radius_y=2)
        self.add_arc('feather-center',(30,38),(18,38),radius_x=6,radius_y=4)
        self.add_arc('feather-left',(18,38),(6,38),radius_x=6,radius_y=2)
        self.add_line('side-left',(6,38),(6,24))
        self.add_contour('head','dome-left','dome-right','side-right','feather-right','feather-center','feather-left','side-left',closed=True)
        self.add_polyline('brows',(15,22),(24,26),(33,22))
        self.add_polyline('beak',(24,26),(27,30),(24,32))
        self.relate('connect','brows','beak')
