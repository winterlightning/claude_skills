# Review candidate; original preserved.
"""A sea turtle from above with an oval shell and four sweeping flippers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1adaf0a7-6662-4745-959f-fe860dd47485'
SOURCE_PATH = 'pictographic-primitives/animals/turtle_1adaf0a7-6662-4745-959f-fe860dd47485.svg'
AUTHOR = 'gpt-6'

class SeaTurtleVariant2(Solo48):
    icon_id = 'sea-turtle-v2'
    variant_of = 'sea-turtle'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('turtle', 'tortoise', 'sea turtle', 'shell', 'flippers', 'marine', 'ocean', 'reptile')

    def build(self) -> None:
        """Opening repair: Round head and broader mirrored front flippers replace thin lens-shaped pockets."""
        self.add_arc('shell-top-right', (24, 14), (34, 20), radius_x=10, radius_y=6)
        self.add_line('shell-right-upper', (34, 20), (34, 28))
        self.add_line('shell-right-lower', (34, 28), (34, 32))
        self.add_arc('shell-bottom-right', (34, 32), (24, 40), radius_x=10, radius_y=8)
        self.add_arc('shell-bottom-left', (24, 40), (14, 32), radius_x=10, radius_y=8)
        self.add_line('shell-left-lower', (14, 32), (14, 28))
        self.add_line('shell-left-upper', (14, 28), (14, 20))
        self.add_arc('shell-top-left', (14, 20), (24, 14), radius_x=10, radius_y=6)
        self.add_contour('shell', 'shell-top-right', 'shell-right-upper', 'shell-right-lower', 'shell-bottom-right', 'shell-bottom-left', 'shell-left-lower', 'shell-left-upper', 'shell-top-left', closed=True)
        self.add_line('shell-seam', (24, 14), (24, 40))
        self.relate('connect', 'shell', 'shell-seam')
        self.add_arc('head-left', (24, 14), (24, 6), radius_x=4, radius_y=4)
        self.add_arc('head-right', (24, 6), (24, 14), radius_x=4, radius_y=4)
        self.add_contour('head', 'head-left', 'head-right', closed=True)
        self.relate('connect', 'head', 'shell')
        self.relate('connect', 'head', 'shell-seam')
        for side, flip in (('left', False), ('right', True)):

            def p(x, y):
                return (48 - x, y) if flip else (x, y)
            self.add_arc(side + '-front-upper', p(14, 20), p(6, 28), radius_x=8, sweep=flip)
            self.add_line(side + '-front-lower', p(6, 28), p(14, 28))
            self.add_contour(side + '-front', side + '-front-upper', side + '-front-lower')
            self.relate('connect', side + '-front', 'shell')
            self.add_arc(side + '-rear', p(14, 32), p(12, 42), radius_x=12, sweep=flip)
            self.relate('connect', side + '-rear', 'shell')
