'Sailboat: straight balanced sails and a shallow single hull, keeping the mast upright.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '319e2aa3-098e-5a2f-a08e-fb155dc163cb'
SOURCE_PATH = 'pictographic-primitives/transportation/bark_319e2aa3-098e-5a2f-a08e-fb155dc163cb.svg'
AUTHOR = 'gpt-6'

class Bark(Solo48):
    icon_id = 'bark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('bark', 'transportation')

    def build(self):
        # Sailboat: balanced triangular sails, an upright mast and an 8-unit-deep hull.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('sails',(24,6),(8,26),(40,26),(24,6))
        l('mast',(24,6),(24,34))
        p('hull',(6,34),(12,42),(36,42),(42,34),(6,34))
        link('connect','mast','sails')
        link('connect','mast','hull')
