"""Pumpkin.

Plan: Mirrored pumpkin lobes around axis24 and bent stem; centerlines (6,6)-(42,42).
Construction: Source lobed pumpkin; no useful exact Lucide pumpkin.
Reduction: Retained central seam, omitted secondary lobe seams to preserve spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7a3a8b0a-72cc-50fc-8d70-d02028b9db8a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pumpkin/20260927T153803Z-thuan-mac-1/reference/pumpkin_7a3a8b0a-72cc-50fc-8d70-d02028b9db8a.svg'
AUTHOR = "gpt-6"


class IconPumpkin(Solo48):
    icon_id = 'pumpkin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('pumpkin',)

    def build(self):
        # Three broad lobes converge at the stem and at the base.
        self.add_bezier('outer-left',(24,13),((15,7),(6,14),(6,27)))
        self.add_bezier('outer-lower-left',(6,27),((6,39),(14,42),(24,42)))
        self.add_bezier('outer-lower-right',(24,42),((34,42),(42,39),(42,27)))
        self.add_bezier('outer-right',(42,27),((42,14),(33,7),(24,13)))
        self.add_contour('pumpkin','outer-left','outer-lower-left','outer-lower-right','outer-right',closed=True)
        self.add_line('seam',(24,13),(24,42))
        self.relate('connect','seam','pumpkin')
        self.add_bezier('stem',(24,13),((24,8),(26,6),(30,6)))
        self.relate('connect','stem','pumpkin')
