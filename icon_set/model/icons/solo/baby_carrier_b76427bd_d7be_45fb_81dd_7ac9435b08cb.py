from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b76427bd-d7be-45fb-81dd-7ac9435b08cb'
SOURCE_PATH = 'pictographic-primitives/babies/gear baby strap on holder_b76427bd-d7be-45fb-81dd-7ac9435b08cb.svg'
AUTHOR = 'gpt-6'

class BabyCarrier(Solo48):
    icon_id = 'baby-carrier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('carrier', 'sling', 'baby', 'harness', 'papoose', 'straps', 'infant', 'gear')

    # Designed to centerline extremes (6, 6)–(42, 42).
    def build(self):
        # Baby carrier: symmetric straps, smooth waist curves and an 8-unit belt band.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('left-strap',(10,18),(10,6),(18,6),(18,16))
        p('right-strap',(30,16),(30,6),(38,6),(38,18))
        a('top',(10,18),(38,18),22,8,sweep=True)
        a('right-waist',(38,18),(34,34),30,30,sweep=False)
        l('bottom',(34,34),(14,34))
        a('left-waist',(14,34),(10,18),30,30,sweep=False)
        self.add_contour('carrier','top','right-waist','bottom','left-waist',closed=True)
        p('belt',(14,34),(6,34),(6,42),(42,42),(42,34),(34,34))
        for part in ('left-strap','right-strap','belt'):
            link('connect',part,'carrier')
