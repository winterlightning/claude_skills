# Variant of crested-penguin; parent file remains unchanged.
'Crested penguin with a rounded head, uninterrupted body and long flippers. VRECT_XL (5,2)-(43,46) supports an upright body. Mirrored across x=24; pointed flipper notches removed. Lucide bird informed broad head and belly arcs.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b013a26e-4b3d-4d2f-a975-ca81de5ad6ce'
SOURCE_PATH = 'pictographic-primitives/animals/penguin crested_b013a26e-4b3d-4d2f-a975-ca81de5ad6ce.svg'
AUTHOR = 'gpt-6'

class CrestedPenguinVariant2(Solo48):
    icon_id = 'crested-penguin-v2'
    variant_of = 'crested-penguin'
    variant_label = 'Simpler penguin silhouette'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('rockhopper-penguin',)
    keywords = ('penguin', 'crest', 'bird', 'antarctic', 'flippers', 'rockhopper', 'standing', 'cold')

    def build(self) -> None:
        # VRECT_XL (5,2)-(43,46), mirrored about x=24.
        self.add_arc('head-left', (14,12), (24,2), radius_x=10)
        self.add_arc('head-right', (24,2), (34,12), radius_x=10)
        self.add_line('side-right', (34,12), (36,34))
        self.add_arc('belly-right', (36,34), (24,46), radius_x=12)
        self.add_arc('belly-left', (24,46), (12,34), radius_x=12)
        self.add_line('side-left', (12,34), (14,12))
        self.add_contour('body','head-left','head-right','side-right','belly-right','belly-left','side-left',closed=True)
        self.add_arc('flipper-left', (14,12), (5,34), radius_x=9, radius_y=22, sweep=False)
        self.add_arc('flipper-right', (34,12), (43,34), radius_x=9, radius_y=22)
        self.add_line('crest-left', (14,12), (5,7))
        self.add_line('crest-right', (34,12), (43,7))
        for part in ('flipper-left','flipper-right','crest-left','crest-right'):
            self.relate('connect','body',part)
        self.relate('connect','flipper-left','crest-left')
        self.relate('connect','flipper-right','crest-right')
        self.add_dot('eye-left',(21,15))
        self.add_dot('eye-right',(27,15))
        self.add_polyline('beak',(21,24),(24,27),(27,24))
