'Rattlesnake: smooth nested turns, an 8-unit body width and regularly separated rattle marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4648896-3720-5e11-b38e-0b0c450735c6'
SOURCE_PATH = 'pictographic-primitives/animals/reptile rattlesnake_d4648896-3720-5e11-b38e-0b0c450735c6.svg'
AUTHOR = 'gpt-6'


class Rattlesnake(Solo48):
    icon_id = 'rattlesnake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('rattlesnake', 'snake', 'rattle', 'reptile', 'slither', 'venom', 'desert', 'serpent')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('rattle-top', (6, 6), (6, 6))
        self.add_line('rattle-bottom', (6, 15), (6, 15))
        self.add_line('tail', (6, 26), (6, 32))
        self.add_arc('tail-turn', (6, 32), (22, 32), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('inner-neck', (22, 32), (22, 20))
        self.add_arc('inner-top', (22, 20), (32, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('inner-right', (32, 20), (32, 37))
        self.add_arc('head-tip', (32, 37), (42, 37), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('outer-right', (42, 37), (42, 20))
        self.add_arc('outer-top', (42, 20), (14, 20), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('outer-neck', (14, 20), (14, 32))
        self.add_contour('snake', *('tail', 'tail-turn', 'inner-neck', 'inner-top', 'inner-right', 'head-tip', 'outer-right', 'outer-top', 'outer-neck'), closed=False)
