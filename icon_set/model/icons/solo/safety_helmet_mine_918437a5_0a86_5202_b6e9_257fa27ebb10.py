'Mining helmet: symmetric crown with a centred circular lamp, attached by a simple bracket; remove the cramped nested strap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '918437a5-0a86-5202-b6e9-257fa27ebb10'
SOURCE_PATH = 'icons-json/construction/safety helmet mine_918437a5-0a86-5202-b6e9-257fa27ebb10.json'
AUTHOR = 'gpt-6'

class SafetyHelmetMine(Solo48):
    icon_id = 'safety-helmet-mine'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'mine', 'construction')

    def build(self) -> None:
        # The hard-hat crown and lamp bracket share the top centre.
        self.add_bezier('crown-left',(24,8),((14,8),(8,17),(8,29)))
        self.add_bezier('crown-right',(40,29),((40,17),(34,8),(24,8)))
        for j,(a,b) in enumerate(zip(((8,29),(4,33),(4,36),(24,40),(44,36),(44,33)),((4,33),(4,36),(24,40),(44,36),(44,33),(40,29)))):
            self.add_line(f'brim-{j}',a,b)
        self.add_contour('helmet','crown-left',*(f'brim-{j}' for j in range(6)),'crown-right',closed=True)
        self.add_line('bracket',(24,8),(24,18))
        self.add_arc('lamp-top',(19,23),(29,23),radius_x=5)
        self.add_arc('lamp-bottom',(29,23),(19,23),radius_x=5)
        self.add_contour('lamp','lamp-top','lamp-bottom',closed=True)
        self.relate('connect','helmet','bracket');self.relate('connect','bracket','lamp')
