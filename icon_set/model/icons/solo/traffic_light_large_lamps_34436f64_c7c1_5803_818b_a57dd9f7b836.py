"""traffic-light-large-lamps: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34436f64-c7c1-5803-818b-a57dd9f7b836'
SOURCE_PATH = 'pictographic-primitives/transportation/traffic light_34436f64-c7c1-5803-818b-a57dd9f7b836.svg'
AUTHOR = 'gpt-6'


class TrafficLightLargeLamps(Solo48):
    icon_id = 'traffic-light-large-lamps'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('traffic light', 'signal', 'stoplight', 'road', 'intersection', 'traffic', 'lights', 'junction')

    def build(self) -> None:

        # Rounded signal body and an evenly spaced vertical lamp series.
        self.add_line('top',(16,6),(32,6))
        self.add_arc('tr',(32,6),(40,12),radius_x=8)
        self.add_line('right',(40,12),(40,36))
        self.add_arc('br',(40,36),(32,42),radius_x=8)
        self.add_line('bottom',(32,42),(16,42))
        self.add_arc('bl',(16,42),(8,36),radius_x=8)
        self.add_line('left',(8,36),(8,12))
        self.add_arc('tl',(8,12),(16,6),radius_x=8)
        self.add_contour('housing','top','tr','right','br','bottom','bl','left','tl',closed=True)
        for i,y in enumerate([14,24,34]): self.add_dot(f'lamp-{i}',(24,y))
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
