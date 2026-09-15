"""Mirrored shield-shaped cat face; Lucide cat informs paired eyes and continuous cheek arcs. Keeps pointed ears and T-shaped muzzle, omits whiskers absent in source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21e29b1c-8a04-474e-91fe-2c7c847aadfc'
SOURCE_PATH = 'pictographic-primitives/animals/cat head_21e29b1c-8a04-474e-91fe-2c7c847aadfc.svg'
AUTHOR = 'gpt-6'


class CatFace(Solo48):
    icon_id = 'cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('cat', 'kitten', 'face', 'head', 'feline', 'pet', 'ears', 'whiskers')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('ears-1', (6, 24), (6, 6))
        self.add_line('ears-2', (6, 6), (14, 10))
        self.add_line('ears-3', (14, 10), (34, 10))
        self.add_line('ears-4', (34, 10), (42, 6))
        self.add_line('ears-5', (42, 6), (42, 24))
        self.add_arc('cheek-right', (42, 24), (24, 42), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_arc('cheek-left', (24, 42), (6, 24), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_line('eye-left', (15, 24), (15, 24))
        self.add_line('eye-right', (33, 24), (33, 24))
        self.add_line('nose-left', (20, 34), (24, 34))
        self.add_line('nose-right', (24, 34), (28, 34))
        self.add_line('mouth', (24, 34), (24, 42))
        self.add_contour('head', *('ears-1', 'ears-2', 'ears-3', 'ears-4', 'ears-5', 'cheek-right', 'cheek-left'), closed=True)
        self.relate('connect', *('nose-left', 'nose-right'))
        self.relate('connect', *('nose-left', 'mouth'))
        self.relate('connect', *('nose-right', 'mouth'))
        self.relate('connect', *('mouth', 'head'))
