'Material UI mark: deliberate straight diagonals and broad open folds without fitted wiggles.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bab5995-9993-44a4-941d-fd5906950e0d'
SOURCE_PATH = 'pictographic-primitives/logos/material ui logo_4bab5995-9993-44a4-941d-fd5906950e0d.svg'
AUTHOR = 'gpt-6'

class MaterialUiLogo(Solo48):
    icon_id = 'material-ui-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('material', 'ui', 'logo', 'logos')

    def build(self):
        # Material UI mark: deliberate straight diagonals and broad open folds without fitted wiggles.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('mark',(6,32),(6,8),(24,20),(42,6),(42,34),(24,42),(24,30),(14,24),(14,36),(6,32))
        l('inner',(24,30),(34,23))
        link('connect','inner','mark')
