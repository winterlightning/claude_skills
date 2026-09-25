'MediaConnect: a regular isometric cube inside two clean outer bracket strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e19348b9-bdcd-4de4-84e3-e69ce4b9d8b8'
SOURCE_PATH = 'pictographic-primitives/apps/elemental mediaconnect_e19348b9-bdcd-4de4-84e3-e69ce4b9d8b8.svg'
AUTHOR = 'gpt-6'

class ElementalMediaconnect(Solo48):
    icon_id = 'elemental-mediaconnect'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('elemental', 'mediaconnect', 'apps')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('cube-1', (24, 14), (34, 20))
        self.add_line('cube-2', (34, 20), (34, 30))
        self.add_line('cube-3', (34, 30), (24, 36))
        self.add_line('cube-4', (24, 36), (14, 30))
        self.add_line('cube-5', (14, 30), (14, 20))
        self.add_line('cube-6', (14, 20), (24, 14))
        self.add_line('edges-1', (14, 20), (24, 26))
        self.add_line('edges-2', (24, 26), (34, 20))
        self.add_line('vertical', (24, 26), (24, 36))
        self.add_line('outer-left-1', (12, 40), (6, 36))
        self.add_line('outer-left-2', (6, 36), (6, 14))
        self.add_line('outer-left-3', (6, 14), (18, 6))
        self.add_line('outer-right-1', (42, 14), (42, 36))
        self.add_line('outer-right-2', (42, 36), (30, 42))
        self.add_contour('cube', *('cube-1', 'cube-2', 'cube-3', 'cube-4', 'cube-5', 'cube-6'), closed=False)
        self.add_contour('edges', *('edges-1', 'edges-2'), closed=False)
        self.add_contour('outer-left', *('outer-left-1', 'outer-left-2', 'outer-left-3'), closed=False)
        self.add_contour('outer-right', *('outer-right-1', 'outer-right-2'), closed=False)
        self.relate('connect', *('cube', 'edges'))
        self.relate('connect', *('cube', 'vertical'))
        self.relate('connect', *('edges', 'vertical'))
