# Variant of stacking-ring-toy; parent file remains unchanged.
"""Stacking toy with three broad rings and a simple rounded peg, omitting the bear crown and one ring. VRECT_XL retains a stable widening base; shared radii and mirrored construction follow Lucide principles without an exact subject match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '11f12d81-7f9c-589f-99c1-4d862f93acd8'
SOURCE_PATH = 'pictographic-primitives/babies/toy_11f12d81-7f9c-589f-99c1-4d862f93acd8.svg'
AUTHOR = 'gpt-6'

class StackingRingToyVariant2(Solo48):
    icon_id = 'stacking-ring-toy-v2'
    variant_of = 'stacking-ring-toy'
    variant_label = 'Three broad rings'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('stacking', 'ring', 'toy', 'infant', 'nursery')

    def build(self) -> None:
        # VRECT_XL centerline extremes (5,2)-(43,46).
        self.add_arc('peg-top', (19,7), (29,7), radius_x=5)
        self.add_line('peg-right', (29,7), (29,10))
        self.add_line('peg-left', (19,10), (19,7))
        self.add_contour('peg', 'peg-left', 'peg-top', 'peg-right')
        for name,left,right,top,bottom in [('top',18,30,10,22), ('middle',15,33,22,34), ('bottom',11,37,34,46)]:
            self.add_line(name+'-top', (left,top), (right,top))
            self.add_arc(name+'-right', (right,top), (right,bottom), radius_x=6)
            self.add_line(name+'-bottom', (right,bottom), (left,bottom))
            self.add_arc(name+'-left', (left,bottom), (left,top), radius_x=6)
            self.add_contour(name, name+'-top', name+'-right', name+'-bottom', name+'-left', closed=True)
        self.relate('connect', 'peg', 'top')
        self.relate('connect', 'top', 'middle')
        self.relate('connect', 'middle', 'bottom')
