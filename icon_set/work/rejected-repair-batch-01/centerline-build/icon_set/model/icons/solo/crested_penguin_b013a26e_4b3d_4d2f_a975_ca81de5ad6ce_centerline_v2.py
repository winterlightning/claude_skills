"""Bring the flipper tips away from the belly and make their outward curves smoother; use a broader, flatter beak to distinguish the penguin from a generic smiling face.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b013a26e-4b3d-4d2f-a975-ca81de5ad6ce'
SOURCE_PATH = 'pictographic-primitives/animals/penguin crested_b013a26e-4b3d-4d2f-a975-ca81de5ad6ce.svg'
AUTHOR = 'gpt-6'

class CrestedPenguin(Solo48):
    icon_id = 'crested-penguin-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('rockhopper-penguin',)
    keywords = ('penguin', 'crest', 'bird', 'antarctic', 'flippers', 'rockhopper', 'standing', 'cold')

    def build(self) -> None:
        self.add_bezier('crown', (14, 12), ((16, 8), (20, 6), (24, 6)), ((28, 6), (32, 8), (34, 12)))
        self.add_bezier('right', (34, 12), ((37, 18), (37, 28), (36, 34)), ((35, 39), (29, 42), (24, 42)))
        self.add_bezier('left', (24, 42), ((19, 42), (13, 39), (12, 34)), ((11, 28), (11, 18), (14, 12)))
        self.add_contour('body', 'crown', 'right', 'left', closed=True)
        self.add_bezier('flipper-left', (14, 12), ((8, 18), (6, 29), (6, 36)))
        self.add_bezier('flipper-right', (34, 12), ((40, 18), (42, 29), (42, 36)))
        self.add_line('crest-left', (14, 12), (6, 7))
        self.add_line('crest-right', (34, 12), (42, 7))
        for a, b in (('flipper-left', 'body'), ('flipper-right', 'body'), ('crest-left', 'body'), ('crest-right', 'body'), ('crest-left', 'flipper-left'), ('crest-right', 'flipper-right')):
            self.relate('connect', a, b)
        self.add_dot('eye-left', (20, 21))
        self.add_dot('eye-right', (28, 21))
        self.add_polyline('beak', (20, 30), (24, 32), (28, 30))
    variant_of = 'crested-penguin'
    variant_label = 'Batch 01 centerline repair'
