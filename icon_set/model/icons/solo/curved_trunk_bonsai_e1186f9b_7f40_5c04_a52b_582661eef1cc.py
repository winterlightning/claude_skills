'Bonsai: smooth broad canopy, one curved trunk and an 8-unit-deep balanced planter.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1186f9b-7f40-5c04-a52b-582661eef1cc'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bonsai_e1186f9b-7f40-5c04-a52b-582661eef1cc.svg'
AUTHOR = 'gpt-6'


class CurvedTrunkBonsai(Solo48):
    icon_id = 'curved-trunk-bonsai'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    aliases = ()
    keywords = ('bonsai', 'tree', 'plant', 'pot', 'foliage', 'garden', 'decor')

    def build(self):
        # Bonsai: smooth broad canopy, one curved trunk and an 8-unit-deep balanced planter.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('canopy-base',(6,24),(42,24))
        l('canopy-r',(42,24),(42,20))
        a('canopy-tr',(42,20),(34,12),8,sweep=False)
        a('crown',(34,12),(14,12),10,6,sweep=False)
        a('canopy-tl',(14,12),(6,20),8,sweep=False)
        l('canopy-l',(6,20),(6,24))
        self.add_contour('canopy','canopy-base','canopy-r','canopy-tr','crown','canopy-tl','canopy-l',closed=True)
        a('trunk-upper',(22,24),(28,30),6,sweep=False)
        a('trunk-lower',(28,30),(22,34),6,4,sweep=True)
        self.add_contour('trunk','trunk-upper','trunk-lower')
        p('pot',(6,34),(14,42),(34,42),(42,34),(6,34))
        link('connect','trunk','canopy')
        link('connect','trunk','pot')
