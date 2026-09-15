"""A radio antenna broadcasts above a trapezoidal airport base.

Construction: radio-tower: mirrored wave arcs, centered transmitter and tapering support.
Reduction: One wave per side; omitted doorway, intermediate box and head divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58573359-f61e-52a8-b710-7818357fd8e0'
SOURCE_PATH = 'pictographic-primitives/travel/airport signal_58573359-f61e-52a8-b710-7818357fd8e0.svg'
AUTHOR = 'gpt-6'


class AirportSignalAntenna(Solo48):
    icon_id = 'airport-signal-antenna'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airport', 'antenna', 'signal', 'radar', 'radio', 'waves', 'tower', 'communication')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42); repeated waves share radii.
        self.add_arc('wave-left',(10,6),(10,24),radius_x=4,radius_y=9,sweep=False)
        self.add_arc('wave-right',(38,6),(38,24),radius_x=4,radius_y=9)
        self.add_arc('head-right',(24,12),(24,18),radius_x=3)
        self.add_arc('head-left',(24,18),(24,12),radius_x=3)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_line('stem',(24,18),(24,30))
        self.add_polyline('base',(18,30),(24,30),(30,30),(36,42),(12,42),closed=True)
        self.relate('connect','head','stem')
        self.relate('connect','stem','base')
