"""Diagonal pliers with two substantial splayed handles and pointed jaws; pivot dot and fine jaw notch omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c2add48e-0255-4362-8d2f-928582da2c95'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cushioned-handle-pliers/20260926T182517Z-thuan-mac-1/reference/pliers_c2add48e-0255-4362-8d2f-928582da2c95.svg'
AUTHOR = 'gpt-6'

class CushionedHandlePliers(Solo48):
    icon_id = 'cushioned-handle-pliers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('pliers', 'cutters', 'grip', 'jaws', 'handles', 'hardware', 'repair', 'tool')

    def build(self) -> None:
        self.add_polyline('jaw',(6,6),(18,6),(26,14),(24,22),(16,24),(8,16),(6,6))
        self.add_line('upper-a',(26,14),(40,22))
        self.add_bezier('upper-round-1',(40,22),((41,22),(42,25),(42,27)))
        self.add_bezier('upper-round-2',(42,27),((42,30),(41,33),(38,34)))
        self.add_line('upper-b',(38,34),(24,22))
        self.add_contour('upper-handle','upper-a','upper-round-1','upper-round-2','upper-b')
        self.add_line('lower-a',(16,24),(22,40))
        self.add_bezier('lower-round-1',(22,40),((23,41),(25,42),(27,42)))
        self.add_bezier('lower-round-2',(27,42),((29,42),(31,40),(32,38)))
        self.add_line('lower-b',(32,38),(24,22))
        self.add_contour('lower-handle','lower-a','lower-round-1','lower-round-2','lower-b')
        self.relate('connect','upper-handle','jaw')
        self.relate('connect','lower-handle','jaw')
        self.relate('connect','upper-handle','lower-handle')
