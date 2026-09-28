"""touring-bicycle: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc615adc-97ee-5f84-9531-39dc64ae388f'
SOURCE_PATH = 'pictographic-primitives/transportation/touring bike_fc615adc-97ee-5f84-9531-39dc64ae388f.svg'
AUTHOR = 'gpt-6'


class TouringBicycle(Solo48):
    icon_id = 'touring-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('touring bike', 'bicycle', 'bike', 'cycling', 'travel', 'road bike', 'pedal', 'transport')

    def build(self) -> None:

        # Paired wheels share radius and baseline; rear triangle and fork join the rims.
        for side,cx in [('rear',12),('front',36)]:
            self.add_arc(side+'-tr',(cx,24),(cx+8,32),radius_x=8)
            self.add_arc(side+'-br',(cx+8,32),(cx,40),radius_x=8)
            self.add_arc(side+'-bl',(cx,40),(cx-8,32),radius_x=8)
            self.add_arc(side+'-tl',(cx-8,32),(cx,24),radius_x=8)
            self.add_contour(side+'-wheel',*[side+'-'+s for s in ['tr','br','bl','tl']],closed=True)
        self.add_polyline('rear-stay',(12,32),(12,24),(20,16))
        self.add_polyline('chain-stay',(12,32),(20,32),(24,32))
        self.add_polyline('frame',(20,16),(24,32),(36,8),(20,16))
        self.add_polyline('fork',(36,32),(36,24),(36,16),(36,8),(42,8))
        self.add_line('saddle',(16,16),(20,16))
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
