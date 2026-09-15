"""taxi-front-oval-lights: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18bfa812-5b8a-5ae5-b6cc-3bf1f014cd6c'
SOURCE_PATH = 'pictographic-primitives/transportation/taxi_18bfa812-5b8a-5ae5-b6cc-3bf1f014cd6c.svg'
AUTHOR = 'gpt-6'


class TaxiFrontOvalLights(Solo48):
    icon_id = 'taxi-front-oval-lights'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('taxi', 'cab', 'car', 'front', 'roof sign', 'vehicle', 'ride', 'transport')

    def build(self) -> None:

        # Body, paired lights and tyres share x=24; roof sign meets the cabin top.
        self.add_polyline('roof',(10,22),(14,14),(20,14),(28,14),(34,14),(38,22))
        self.add_polyline('sign',(20,14),(20,6),(28,6),(28,14))
        self.add_line('body-top',(10,22),(38,22))
        self.add_arc('body-tr',(38,22),(42,26),radius_x=4)
        self.add_line('body-right',(42,26),(42,36))
        self.add_arc('body-br',(42,36),(38,40),radius_x=4)
        self.add_line('body-bottom',(38,40),(10,40))
        self.add_arc('body-bl',(10,40),(6,36),radius_x=4)
        self.add_line('body-left',(6,36),(6,26))
        self.add_arc('body-tl',(6,26),(10,22),radius_x=4)
        self.add_contour('body','body-top','body-tr','body-right','body-br','body-bottom','body-bl','body-left','body-tl',closed=True)
        for side,x in [('left',10),('right',38)]: self.add_line('tyre-'+side,(x,40),(x,42))
        self.add_line('light-left',(15,31),(17,31))
        self.add_line('light-right',(31,31),(33,31))
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
