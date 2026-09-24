"""A bull beneath an upward financial-trend arrow.
Plan: HRECT_L gives the animal and separate arrow a broad composition. Visible ink bounds: (2, 6, 46, 42).
Reduction: Horn simplified to an open curve; outlined legs reduced to two strokes; minor leg crease omitted. Retained head, hump, body, tail and rising arrow.
Construction: No useful exact local Lucide bull match; supplied reference guides the horn, lowered head, body and financial arrow."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '936d0079-3089-4c8c-bc22-422921c13e69'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/saving bull_936d0079-3089-4c8c-bc22-422921c13e69.svg'
AUTHOR = 'gpt-6'
PLAN = 'A bull beneath an upward financial-trend arrow.'
OMISSIONS = 'Horn simplified to an open curve; outlined legs reduced to two strokes; minor leg crease omitted. Retained head, hump, body, tail and rising arrow.'
CONSTRUCTION_REFERENCES = 'No useful exact local Lucide bull match; supplied reference guides the horn, lowered head, body and financial arrow.'
KEYSHAPE_INK_BOUNDS = (2, 6, 46, 42)

class AuthoredIcon(Solo48):
    icon_id = 'saving-bull'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('saving', 'bull')

    def build(self):
        self.add_bezier('back-front', (8, 28), ((14, 24), (16, 22), (22, 22)))
        self.add_bezier('back-rear', (22, 22), ((28, 22), (30, 26), (36, 26)))
        self.add_arc('rump-top', (36, 26), (40, 30), radius_x=4)
        self.add_arc('rump-bottom', (40, 30), (36, 34), radius_x=4)
        self.add_line('belly-right', (36, 34), (28, 34))
        self.add_line('belly-left', (28, 34), (20, 34))
        self.add_bezier('chin', (20, 34), ((18, 34), (16, 38), (12, 38)), ((8, 38), (8, 36), (8, 32)))
        self.add_line('muzzle', (8, 32), (8, 28))
        self.add_contour('animal', 'back-front', 'back-rear', 'rump-top', 'rump-bottom', 'belly-right', 'belly-left', 'chin', 'muzzle', closed=True)
        self.add_bezier('horn', (8, 28), ((4, 28), (4, 22), (4, 18)))
        self.relate('connect', 'horn', 'animal')
        for (name, x) in [('front', 28), ('rear', 36)]:
            self.add_line(name + '-leg', (x, 34), (x, 40))
            self.relate('connect', 'animal', name + '-leg')
        self.add_polyline('tail', (40, 30), (44, 34), (44, 40))
        self.relate('connect', 'tail', 'animal')
        self.add_line('trend', (36, 16), (44, 8))
        self.add_polyline('arrow', (36, 8), (44, 8), (44, 16))
        self.relate('connect', 'trend', 'arrow')
