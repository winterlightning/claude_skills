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
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('top',(16, 4),(32, 4))
        self.add_bezier('tr',(32, 4),*(((35.74213152, 4), (39.06587168, 6.96800053), (40, 12)),))
        self.add_line('right',(40, 12),(40, 36))
        self.add_bezier('br',(40, 36),*(((39.06587168, 41.03199947), (35.74213152, 44), (32, 44)),))
        self.add_line('bottom',(32, 44),(16, 44))
        self.add_bezier('bl',(16, 44),*(((12.25786848, 44), (8.93412832, 41.03199947), (8, 36)),))
        self.add_line('left',(8, 36),(8, 12))
        self.add_bezier('tl',(8, 12),*(((8.93412832, 6.96800053), (12.25786848, 4), (16, 4)),))
        self.add_line('lamp-0',(24, 14),(24, 14))
        self.add_line('lamp-1',(24, 24),(24, 24))
        self.add_line('lamp-2',(24, 34),(24, 34))
        self.add_contour('housing',*('top', 'tr', 'right', 'br', 'bottom', 'bl', 'left', 'tl'),closed=True)
        self.relate('connect',*('top', 'tr'))
        self.relate('connect',*('top', 'tl'))
        self.relate('connect',*('tr', 'right'))
        self.relate('connect',*('right', 'br'))
        self.relate('connect',*('br', 'bottom'))
        self.relate('connect',*('bottom', 'bl'))
        self.relate('connect',*('bl', 'left'))
        self.relate('connect',*('left', 'tl'))
