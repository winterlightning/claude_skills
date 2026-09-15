'Overlapping comments: straight balanced bubbles and clear tails with ample panel separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87416b28-9cd9-4d1f-9509-2f57b7c73823'
SOURCE_PATH = 'pictographic-primitives/state/double comment box_87416b28-9cd9-4d1f-9509-2f57b7c73823.svg'
AUTHOR = 'gpt-6'

class DoubleCommentBox(Solo48):
    icon_id = 'double-comment-box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('double', 'comment', 'box', 'state')

    def build(self):
        # Overlapping comments: clean visible bubble outlines, with 8-unit panel separation and readable tails.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('front',(18,6),(42,6),(42,28),(36,28),(36,36),(28,28),(18,28),(18,6))
        p('back',(18,18),(6,18),(6,36),(16,36),(24,42),(24,28))
        link('connect','front','back')
