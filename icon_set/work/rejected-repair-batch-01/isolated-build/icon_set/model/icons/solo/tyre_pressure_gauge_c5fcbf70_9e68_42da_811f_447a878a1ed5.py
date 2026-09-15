"""tyre-pressure-gauge: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5fcbf70-9e68-42da-811f-447a878a1ed5'
SOURCE_PATH = 'pictographic-primitives/transportation/tire air pressure level 1_c5fcbf70-9e68-42da-811f-447a878a1ed5.svg'
AUTHOR = 'gpt-6'


class TyrePressureGauge(Solo48):
    icon_id = 'tyre-pressure-gauge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('tyre pressure', 'tire pressure', 'gauge', 'tyre', 'wheel', 'inflation', 'car', 'maintenance')

    def build(self) -> None:

        # Pressure gauge owns its needle; a curved hose attaches to the oval tyre.
        self.add_arc('gauge-right',(14,6),(14,22),radius_x=8)
        self.add_arc('gauge-left',(14,22),(14,6),radius_x=8)
        self.add_contour('gauge','gauge-right','gauge-left',closed=True)
        self.add_line('needle',(14,14),(14,6))
        self.add_line('hose-upper',(14,22),(14,24))
        self.add_arc('hose-bend',(14,24),(20,30),radius_x=6,sweep=False)
        self.add_line('hose-end',(20,30),(24,30))
        self.add_contour('hose','hose-upper','hose-bend','hose-end')
        self.add_arc('tyre-top',(24,30),(42,30),radius_x=9,radius_y=12)
        self.add_arc('tyre-bottom',(42,30),(24,30),radius_x=9,radius_y=12)
        self.add_contour('tyre','tyre-top','tyre-bottom',closed=True)
        self.add_dot('hub',(33,30))
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
