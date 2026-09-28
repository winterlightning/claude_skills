'Prison Cell Bars.\n\nSymbol plan: Five evenly spaced prison bars connect two horizontal rails. Thick rail outlines reduce to single strokes.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8e9e2f83-517f-469a-92b2-445c602e2f0f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__prison-bar-barrier/20260927T170540Z-thuan-mac-1/reference/jail_8e9e2f83-517f-469a-92b2-445c602e2f0f.svg'
AUTHOR = "gpt-6"

class PrisonBarBarrier(Solo48):
    icon_id = 'prison-bar-barrier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('prison', 'bar', 'barrier')

    def build(self):
        # Open sides and five evenly spaced bars match the source's barrier.
        self.add_line('top-rail', (6,6), (42,6))
        self.add_line('bottom-rail', (6,42), (42,42))
        for index, x in enumerate((8,16,24,32,40)):
            name = f'bar-{index}'
            self.add_line(name, (x,6), (x,42))
            self.relate('connect', name, 'top-rail')
            self.relate('connect', name, 'bottom-rail')
