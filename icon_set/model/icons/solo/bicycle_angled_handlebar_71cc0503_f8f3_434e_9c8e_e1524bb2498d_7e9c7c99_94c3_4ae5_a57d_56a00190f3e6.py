"""A bicycle with a rear stay, level top tube and upward angled handlebar. HRECT_L ink (6,6)-(42,42). Lucide bike informed paired wheels; rim attachments replace hub crossings. Both identical references are retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71cc0503-f8f3-434e-9c8e-e1524bb2498d'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'
SOURCE_REFERENCES = (('71cc0503-f8f3-434e-9c8e-e1524bb2498d', 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'), ('7e9c7c99-94c3-4ae5-a57d-56a00190f3e6', 'pictographic-primitives/transportation/bicycle_7e9c7c99-94c3-4ae5-a57d-56a00190f3e6.svg'))
AUTHOR = 'gpt-6'

class BicycleAngledHandlebar(Solo48):
    icon_id = 'bicycle-angled-handlebar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'cycling', 'pedal', 'transport', 'two wheels', 'ride', 'city bike')

    def build(self) -> None:
        # Identical wheels share radius and baseline; attachments are exact top extrema.
        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-right',(x,26),(x,40),radius_x=7)
            self.add_arc(side+'-left',(x,40),(x,26),radius_x=7)
            self.add_contour(side+'-wheel',side+'-right',side+'-left',closed=True)
        self.add_polyline('frame',(11,26),(19,16),(31,16))
        self.add_polyline('seat',(8,8),(16,8),(19,16))
        self.relate('connect','frame','rear-wheel')
        self.relate('connect','seat','frame')

        self.add_polyline('fork',(37,26),(31,16),(31,11),(37,8))
        self.relate('connect','fork','front-wheel')
        self.relate('connect','fork','frame')
