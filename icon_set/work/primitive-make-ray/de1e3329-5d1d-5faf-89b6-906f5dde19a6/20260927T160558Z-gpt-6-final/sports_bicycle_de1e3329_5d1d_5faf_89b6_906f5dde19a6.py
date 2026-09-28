'Sports bicycle: independent spacing revision.\n\nUse the reviewed open frame and equal wheels; remove internal seat tube.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: bike: round wheels and economical frame strokes. Local Lucide originals and atomic-debug renders were inspected.\n'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'de1e3329-5d1d-5faf-89b6-906f5dde19a6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sports-bicycle/20260927T155415Z-thuan-mac-1/reference/bicycle sports_de1e3329-5d1d-5faf-89b6-906f5dde19a6.svg'
SOURCE_REFERENCES = (('de1e3329-5d1d-5faf-89b6-906f5dde19a6', 'pictographic-primitives/transportation/bicycle sports_de1e3329-5d1d-5faf-89b6-906f5dde19a6.svg'),)
AUTHOR = 'gpt-6'

class SportsBicycle(Solo48):
    icon_id = 'sports-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('bicycle', 'bike', 'sports', 'racing', 'road bike', 'cycling', 'drop handlebar', 'pedal')

    def build(self):
        # Matched wheels anchor an open diamond road-bike frame.
        self.add_arc('rear-a', (13, 28), (13, 42), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('rear-b', (13, 42), (13, 28), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('rear-wheel', 'rear-a', 'rear-b', closed=True)
        self.add_arc('front-a', (35, 28), (35, 42), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('front-b', (35, 42), (35, 28), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('front-wheel', 'front-a', 'front-b', closed=True)
        self.add_polyline('frame', (13, 28), (20, 16), (31, 16), (24, 28), (13, 28))
        self.add_line('seat-tube', (20, 16), (24, 28))
        self.add_line('fork', (31, 16), (35, 28))
        self.add_line('seat-post', (20, 16), (19, 8))
        self.add_line('saddle', (15, 8), (24, 8))
        self.add_polyline('handlebar', (31, 16), (32, 6), (40, 6))
        for a,b in [('frame','rear-wheel'),('frame','seat-tube'),('frame','fork'),('fork','front-wheel'),('frame','seat-post'),('seat-post','saddle'),('frame','handlebar')]:
            self.relate('connect', a, b)
