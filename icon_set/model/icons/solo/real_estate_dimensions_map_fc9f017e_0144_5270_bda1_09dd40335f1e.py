'Folded map: three balanced panels with straight folds; the cramped interior dimension notch is omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc9f017e-0144-5270-bda1-09dd40335f1e'
SOURCE_PATH = 'icons-json/maps/real estate dimensions map_fc9f017e-0144-5270-bda1-09dd40335f1e.json'
AUTHOR = 'gpt-6'

class RealEstateDimensionsMap(Solo48):
    icon_id = 'real-estate-dimensions-map'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('real', 'estate', 'dimensions', 'map', 'maps')

    def build(self):
        # Folded map: three balanced panels with straight folds; the cramped interior dimension notch is omitted.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('map',(4,8),(17,14),(31,8),(44,14),(44,40),(31,34),(17,40),(4,34),(4,8))
        l('fold-left',(17,14),(17,40))
        l('fold-right',(31,8),(31,34))
        link('connect','fold-left','map')
        link('connect','fold-right','map')
