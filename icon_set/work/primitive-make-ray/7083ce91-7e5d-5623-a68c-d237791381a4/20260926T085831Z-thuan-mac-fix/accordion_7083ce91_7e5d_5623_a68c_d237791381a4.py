"""Front-facing panels share a y axis; two broad bellows folds replace the fine pleats. Three keyboard bars share a repeat definition. Extremes (4,8)-(44,40)."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7083ce91-7e5d-5623-a68c-d237791381a4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__accordion/20260926T085631Z-thuan-mac/reference/accordian_7083ce91-7e5d-5623-a68c-d237791381a4.svg"
AUTHOR = "claude-opus-5-5"

class Accordion(Solo48):
    icon_id = 'accordion'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    categories = ("primitives", "music")
    aliases = ()
    keywords = ('accordion', 'instrument', 'bellows', 'keyboard', 'folk', 'music', 'squeezebox')

    def build(self):
        # Symbol plan (HRECT_L x4..44, y8..40).
        # Left keyboard panel: inner edge x12 from y8 to y40 with five short key
        # lines at y8,16,24,32,40 running left to x4 (pitch 8; the first and last
        # also close the panel). Bellows: two hexagon folds with an M top
        # (12,14)-(18,8)-(24,14)-(30,8)-(36,14), a mirrored W bottom and a centre
        # fold x24. Right panel: plain box x36..44.
        L = self.add_line
        join = lambda a, b: self.relate('connect', a, b)
        ys = (8, 14, 16, 24, 32, 34, 40)
        for a, b in zip(ys, ys[1:]):
            L(f'edge-{a}', (12, a), (12, b))
        for k, y in enumerate((8, 16, 24, 32, 40)):
            L(f'key-{k}', (12, y), (4, y))
        edges = [f'edge-{a}' for a in ys[:-1]]
        for a, b in zip(edges, edges[1:]):
            join(a, b)
        for k, y in enumerate((8, 16, 24, 32, 40)):
            for e in edges:
                if y in (int(e.split('-')[1]), ys[ys.index(int(e.split('-')[1])) + 1]):
                    join(f'key-{k}', e)
        L('r-top', (36, 8), (44, 8)); L('r-right', (44, 8), (44, 40)); L('r-bottom', (44, 40), (36, 40))
        L('r-l1', (36, 40), (36, 34)); L('r-l2', (36, 34), (36, 14)); L('r-l3', (36, 14), (36, 8))
        self.add_contour('right-panel', 'r-top', 'r-right', 'r-bottom', 'r-l1', 'r-l2', 'r-l3', closed=True)
        self.add_polyline('bellows-top', (12, 14), (18, 8), (24, 14), (30, 8), (36, 14))
        self.add_polyline('bellows-bottom', (12, 34), (18, 40), (24, 34), (30, 40), (36, 34))
        L('fold', (24, 14), (24, 34))
        join('bellows-top', 'edge-8'); join('bellows-top', 'edge-14')
        join('bellows-bottom', 'edge-32'); join('bellows-bottom', 'edge-34')
        for part in ('bellows-top', 'bellows-bottom'):
            join(part, 'right-panel'); join(part, 'fold')
