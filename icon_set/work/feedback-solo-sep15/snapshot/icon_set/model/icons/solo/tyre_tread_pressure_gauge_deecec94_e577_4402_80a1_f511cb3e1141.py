"""tyre-tread-pressure-gauge: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deecec94-e577-4402-80a1-f511cb3e1141'
SOURCE_PATH = 'pictographic-primitives/transportation/tire air pressure level_deecec94-e577-4402-80a1-f511cb3e1141.svg'
AUTHOR = 'gpt-6'


class TyreTreadPressureGauge(Solo48):
    icon_id = 'tyre-tread-pressure-gauge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('tyre pressure', 'tire pressure', 'gauge', 'tread', 'tyre', 'inflation', 'car', 'dashboard')

    def build(self) -> None:

        # Upright tread has a centred dash series; hose is physically attached at right.
        self.add_line('tyre-top',(10,16),(20,16))
        self.add_arc('tyre-tr',(20,16),(24,20),radius_x=4)
        self.add_polyline('tyre-right',(24,20),(24,34),(24,38))
        self.add_arc('tyre-br',(24,38),(20,42),radius_x=4)
        self.add_line('tyre-bottom',(20,42),(10,42))
        self.add_arc('tyre-bl',(10,42),(6,38),radius_x=4)
        self.add_line('tyre-left',(6,38),(6,20))
        self.add_arc('tyre-tl',(6,20),(10,16),radius_x=4)
        self.add_contour('tyre','tyre-top','tyre-tr','tyre-right-1','tyre-right-2','tyre-br','tyre-bottom','tyre-bl','tyre-left','tyre-tl',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='tyre-right']
        for i,y in enumerate([25,33]): self.add_dot(f'tread-{i}',(15,y))
        self.add_arc('gauge-right',(34,6),(34,22),radius_x=8)
        self.add_arc('gauge-left',(34,22),(34,6),radius_x=8)
        self.add_contour('gauge','gauge-right','gauge-left',closed=True)
        self.add_line('needle',(34,14),(34,6))
        self.add_line('hose-upper',(34,22),(34,26))
        self.add_arc('hose-bend',(34,26),(26,34),radius_x=8)
        self.add_line('hose-end',(26,34),(24,34))
        self.add_contour('hose','hose-upper','hose-bend','hose-end')
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
