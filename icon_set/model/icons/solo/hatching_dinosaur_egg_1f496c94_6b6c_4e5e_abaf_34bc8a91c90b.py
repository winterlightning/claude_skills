"""A baby dinosaur rising out of a cracked egg."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f496c94-6b6c-4e5e-abaf-34bc8a91c90b'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur egg hatch_1f496c94-6b6c-4e5e-abaf-34bc8a91c90b.svg'
AUTHOR = 'gpt-6'

class HatchingDinosaurEgg(Solo48):
    icon_id = 'hatching-dinosaur-egg'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('dinosaur', 'egg', 'hatch', 'baby', 'shell', 'prehistoric', 'birth', 'jurassic')

    def build(self):
        # Baby dinosaur head uses tangent cardinal arcs and a broad muzzle above a single cracked shell. Eye placed with generous head clearance. No useful Lucide hatchling match.
        self.add_arc('shell-bottom', (42, 28), (6, 28), radius_x=18, radius_y=14, sweep=True)
        self.add_line('crack-1', (6, 28), (15, 34))
        self.add_line('crack-2', (15, 34), (24, 28))
        self.add_line('crack-3', (24, 28), (33, 34))
        self.add_line('crack-4', (33, 34), (42, 28))
        self.add_contour('shell', 'shell-bottom', 'crack-1', 'crack-2', 'crack-3', 'crack-4', closed=True)
        self.add_line('neck', (33, 34), (33, 16))
        self.add_arc('head-top', (33, 16), (23, 6), radius_x=10, radius_y=10, sweep=False)
        self.add_line('forehead', (23, 6), (16, 6))
        self.add_arc('face', (16, 6), (6, 16), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('jaw-round', (6, 16), (14, 24), radius_x=8, radius_y=8, sweep=False)
        self.add_line('jaw', (14, 24), (18, 24))
        self.add_line('throat', (18, 24), (18, 32))
        self.add_contour('hatchling', 'neck', 'head-top', 'forehead', 'face', 'jaw-round', 'jaw', 'throat', closed=False)
        self.relate("connect", 'shell', 'hatchling')
        self.add_dot('eye', (23, 16))
