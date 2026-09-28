from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "280da1a2-f9bb-4c4f-8a82-4da931ec7064"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tag-yuan/20260926T163748Z-thuan-mac/reference/tag yuan_280da1a2-f9bb-4c4f-8a82-4da931ec7064.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id="tag-yuan"
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="commerce"
    aliases=()
    keywords=("price tag","yuan","renminbi","currency")
    def build(self):
        # The reference's clipped price-tag corner and centered yuan mark.
        self.add_polyline("tag-outline",(6,16),(16,6),(42,6),(42,38),(38,42),(10,42),(6,38),(6,16),closed=True)
        self.add_polyline("yuan-fork",(19,16),(24,25),(29,16))
        self.add_line("yuan-stem",(24,25),(24,33))
        self.add_polyline("yuan-bar-upper",(18,25),(24,25),(30,25))
        self.add_polyline("yuan-bar-lower",(18,33),(24,33),(30,33))
        self.relate("connect","yuan-fork","yuan-stem")
        self.relate("connect","yuan-fork","yuan-bar-upper")
        self.relate("connect","yuan-stem","yuan-bar-upper")
        self.relate("connect","yuan-stem","yuan-bar-lower")
