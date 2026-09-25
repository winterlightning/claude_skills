"""spoon and fork: standalone batch 17 repair.
Retained the round plate, three-tined fork and diagonal outer handle visible in the supplied source. Squared the fork bowl and split it at the actual center-tine junction. Redrew the plate outline through the exact handle attachment.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'dd96595d-042a-465f-9681-d8c23c641754'
SOURCE_PATH = 'pictographic-primitives/other/spoon and fork_dd96595d-042a-465f-9681-d8c23c641754.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'utensils'

class AuthoredIcon(Solo48):
    icon_id = 'spoon-and-fork'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('spoon', 'and', 'fork')

    def build(self):
        self.add_bezier('plate-tr',(24,6),((34,6),(42,14),(42,24)))
        self.add_bezier('plate-br1',(42,24),((42,29),(40,34),(37,37)))
        self.add_bezier('plate-br2',(37,37),((34,40),(29,42),(24,42)))
        self.add_bezier('plate-bl',(24,42),((14,42),(6,34),(6,24)))
        self.add_bezier('plate-tl',(6,24),((6,14),(14,6),(24,6)))
        self.add_contour('plate','plate-tr','plate-br1','plate-br2','plate-bl','plate-tl',closed=True)
        self.add_line('tine-left',(16,19),(16,24));self.add_line('bowl-1',(16,24),(16,28));self.add_line('bowl-2',(16,28),(24,28));self.add_line('bowl-3',(24,28),(32,28));self.add_line('bowl-4',(32,28),(32,24))
        self.add_line('tine-right',(32,24),(32,19));self.add_contour('fork','tine-left','bowl-1','bowl-2','bowl-3','bowl-4','tine-right')
        self.add_line('center-tine',(24,19),(24,28));self.add_line('handle',(24,28),(24,33))
        self.relate('connect','center-tine','fork');self.relate('connect','handle','fork');self.relate('connect','center-tine','handle')
        self.add_line('outer-handle',(37,37),(42,42));self.relate('connect','outer-handle','plate')

