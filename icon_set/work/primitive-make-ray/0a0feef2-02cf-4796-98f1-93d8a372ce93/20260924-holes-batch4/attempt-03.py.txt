"""ui webpage bug: repaired SOLO48 composition.
Plan: Bilateral leg pairs and a continuous window frame.
Keyshape: SQUARE balances browser chrome and bug content.
Reduction: Bug crossbar removed inside the body; all six external legs remain. Two tiny browser chrome ticks omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0a0feef2-02cf-4796-98f1-93d8a372ce93'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage bug_0a0feef2-02cf-4796-98f1-93d8a372ce93.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'bug, monitor'

class Drawing(Solo48):
    icon_id = 'ui-webpage-bug'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ui', 'webpage', 'bug')

    def browser(self):
        self.add_line('top', (10, 6), (38, 6))
        self.add_arc('tr', (38, 6), (42, 10), radius_x=4)
        self.add_line('right-upper', (42, 10), (42, 14))
        self.add_line('right-lower', (42, 14), (42, 38))
        self.add_arc('br', (42, 38), (38, 42), radius_x=4)
        self.add_line('bottom', (38, 42), (10, 42))
        self.add_arc('bl', (10, 42), (6, 38), radius_x=4)
        self.add_line('left-lower', (6, 38), (6, 14))
        self.add_line('left-upper', (6, 14), (6, 10))
        self.add_arc('tl', (6, 10), (10, 6), radius_x=4)
        self.add_contour('browser', 'top', 'tr', 'right-upper', 'right-lower', 'br', 'bottom', 'bl', 'left-lower', 'left-upper', 'tl', closed=True)
        self.add_line('chrome', (6, 14), (42, 14))
        self.relate('connect', 'chrome', 'left-upper', 'left-lower', 'right-upper', 'right-lower')

    def build(self):
        self.browser()
        points = [(19, 28), (21, 24), (27, 24), (29, 28), (27, 32), (21, 32)]
        names = []
        for (i, p) in enumerate(points):
            n = f'body-{i}'
            self.add_arc(n, p, points[(i + 1) % 6], radius_x=5)
            names.append(n)
        self.add_contour('bug-body', *names, closed=True)
        for (name, start, end) in [('tl', (21, 24), (18, 22)), ('tr', (27, 24), (30, 22)), ('bl', (21, 32), (18, 33)), ('br', (27, 32), (30, 33))]:
            self.add_line('leg-' + name, start, end)
            self.relate('connect', 'leg-' + name, 'bug-body')
        self.add_line('leg-middle-left', (16, 28), (19, 28))
        self.add_line('leg-middle-right', (29, 28), (32, 28))
        self.relate('connect', 'leg-middle-left', 'bug-body')
        self.relate('connect', 'leg-middle-right', 'bug-body')
