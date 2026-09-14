"""shock-absorber: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01782115-840f-4608-80a2-63dafd53ad81'
SOURCE_PATH = 'pictographic-primitives/transportation/suspension dampers_01782115-840f-4608-80a2-63dafd53ad81.svg'
AUTHOR = 'gpt-6'

class ShockAbsorberVariant4(Solo48):
    icon_id = 'shock-absorber-v4'
    variant_of = 'shock-absorber-v2'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('shock absorber', 'suspension', 'damper', 'car', 'strut', 'mechanic', 'automotive', 'repair')

    def build(self) -> None:
        """Opening repair: Made the lower mounting eye circular instead of a thin lens."""
        self.add_polyline('body', (8, 12), (18, 12), (30, 12), (40, 12), (40, 28), (24, 28), (8, 28), closed=True)
        self.add_arc('mount', (18, 12), (30, 12), radius_x=6, radius_y=8)
        self.add_line('piston', (24, 28), (24, 36))
        self.add_arc('eye-right', (24, 36), (24, 44), radius_x=3, radius_y=3)
        self.add_arc('eye-left', (24, 44), (24, 36), radius_x=3, radius_y=3)
        self.add_contour('eye', 'eye-right', 'eye-left', closed=True)
        for i, a in enumerate(self.primitives):
            for b in self.primitives[i + 1:]:
                if a.start in (b.start, b.end) or a.end in (b.start, b.end):
                    self.relate('connect', a.element_id, b.element_id)
