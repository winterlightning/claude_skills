'T-rex head: a broad snout, coherent jaw and tangent crown curves; blocky identity retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '072fa441-e2e2-5dcb-8d2a-fb466edee694'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur trex_072fa441-e2e2-5dcb-8d2a-fb466edee694.svg'
AUTHOR = 'gpt-6'


class BlockyTrexHead(Solo48):
    icon_id = 'blocky-trex-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('trex', 'tyrannosaurus', 'dinosaur', 'head', 'teeth', 'geometric', 'prehistoric', 'jaw')

    def build(self):
        # T-rex head: a broad snout, coherent jaw and tangent crown curves; blocky identity retained.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('top',(14,8),(34,8))
        a('back',(34,8),(44,18),10)
        l('neck-a',(44,18),(44,40))
        l('neck-b',(44,40),(34,36))
        l('neck-c',(34,36),(26,32))
        l('neck-d',(26,32),(10,32))
        a('jaw',(10,32),(4,26),6)
        l('snout',(4,26),(4,18))
        a('forehead',(4,18),(14,8),10)
        self.add_contour('head','top','back','neck-a','neck-b','neck-c','neck-d','jaw','snout','forehead',closed=True)
        l('mouth',(4,24),(20,24))
        link('connect','head','mouth')
        self.add_dot('eye',(31,19))
