'Bathrobe: symmetric sleeve widths, a clear belt and deliberately straight overlapping lapels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b96d753e-96ad-5e09-8189-08d080845f4b'
SOURCE_PATH = 'pictographic-primitives/spas/bathroom robe female_b96d753e-96ad-5e09-8189-08d080845f4b.svg'
AUTHOR = 'gpt-6'

class BathroomRobeFemale(Solo48):
    icon_id = 'bathroom-robe-female'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    categories = ('primitives', 'spas')
    aliases = ()
    keywords = ('bathroom', 'robe', 'female', 'spas')

    def build(self):
        # Bathrobe: symmetric sleeve widths, a clear belt and deliberately straight overlapping lapels.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('robe',(14,6),(6,30),(14,34),(14,42),(34,42),(34,34),(42,30),(34,6),(14,6))
        p('lapel',(14,6),(24,26),(24,42))
        l('collar',(34,6),(22,22))
        link('connect','robe','lapel')
        link('connect','robe','collar')
        link('connect','lapel','collar')
        l('belt',(14,26),(34,26))
        link('connect','belt','lapel')
        l('sleeve-left',(14,18),(14,34))
        l('sleeve-right',(34,18),(34,34))
        for part in ('sleeve-left','sleeve-right'):
            link('connect',part,'robe')
            link('connect',part,'belt')
