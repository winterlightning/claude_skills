"""A rounded square sticker peels at its lower-left corner; one smooth curl defines the folded flap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc796454-28a1-5074-b929-b1cd188ae179'
SOURCE_PATH = 'pictographic-primitives/tools/self adhesive_bc796454-28a1-5074-b929-b1cd188ae179.svg'
AUTHOR = 'gpt-6'

class PeelingSticker(Solo48):
    icon_id = 'peeling-sticker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('sticker', 'self adhesive', 'label', 'peel', 'adhesive', 'decal', 'note', 'tag')

    def build(self) -> None:
        self.add_line('top',(12,6),(36,6))
        self.add_arc('tr',(36,6),(42,12),radius_x=6)
        self.add_line('right',(42,12),(42,36))
        self.add_arc('br',(42,36),(36,42),radius_x=6)
        self.add_line('bottom',(36,42),(24,42))
        self.add_line('fold-diagonal',(24,42),(6,24))
        self.add_line('left',(6,24),(6,12))
        self.add_arc('tl',(6,12),(12,6),radius_x=6)
        self.add_contour('outline','top','tr','right','br','bottom','fold-diagonal','left','tl',closed=True)
        self.add_line('curl-top',(6,24),(18,24))
        self.add_arc('curl-corner',(18,24),(24,30),radius_x=6)
        self.add_line('curl-side',(24,30),(24,42))
        self.add_contour('curl','curl-top','curl-corner','curl-side')
        self.relate('connect','curl','outline')
