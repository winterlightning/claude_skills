'Stapler: straight parallel lid edges and a broad base; equal spacing preserves the open lever.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '769934a7-f4c1-53a0-94f4-8cabcbf5384b'
SOURCE_PATH = 'icons-json/office/stapler_769934a7-f4c1-53a0-94f4-8cabcbf5384b.json'
AUTHOR = 'gpt-6'

class Stapler(Solo48):
    icon_id = 'stapler'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('stapler', 'office')

    def build(self):
        # Stapler: straight broad lid and open base joined at the rear hinge without a trapped sliver.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('base',(4,32),(4,40),(36,40),(40,36))
        p('lid',(10,8),(44,28),(40,36),(6,16),(10,8))
        link('connect','base','lid')
