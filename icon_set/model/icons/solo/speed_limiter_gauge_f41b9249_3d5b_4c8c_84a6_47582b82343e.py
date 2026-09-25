"""speed-limiter-gauge: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f41b9249-3d5b-4c8c-84a6-47582b82343e'
SOURCE_PATH = 'pictographic-primitives/transportation/speed limiter_f41b9249-3d5b-4c8c-84a6-47582b82343e.svg'
AUTHOR = 'gpt-6'


class SpeedLimiterGauge(Solo48):
    icon_id = 'speed-limiter-gauge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('speed limiter', 'gauge', 'speedometer', 'cruise control', 'limit', 'dashboard', 'car', 'dial')

    def build(self) -> None:

        # Arc owns the dial; two needles share a hub. Limit pin is above the dial.
        self.add_arc('dial',(6,42),(42,42),radius_x=18,radius_y=16)
        self.add_polyline('needles',(19,36),(24,42),(29,36))
        self.add_arc('pin-top',(36,6),(36,14),radius_x=4)
        self.add_arc('pin-bottom',(36,14),(36,6),radius_x=4)
        self.add_contour('pin','pin-top','pin-bottom',closed=True)
        self.add_line('pin-stalk',(36,14),(36,18))
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
