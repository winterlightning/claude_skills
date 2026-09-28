"""Two price tags stacked: a front tag with its hole, and the edge of one behind.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: Lucide `tags`. The front tag lies on the 45-degree anti-diagonal, pointing top right as in the reference:
its square point at the top right (34,6), sides running left to (20,6)
and down to (34,20), long edges down the anti-diagonal to (6,20) and
(20,34), and a flat end between them; the eyelet is a dot at (26,14), 8+
from every edge. The tag behind shows only its point side and lower long
edge, 8 off the front tag's: down x=42 from (42,14) to (42,24), then along
x+y=66 to (24,42).
Revision: the rejected drawing overlapped the two tags into one blocky
outline; the front tag is now whole and the back tag is a separate
parallel edge, so two tags read.
Construction reference: Lucide `tags`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'da3a18cb-9766-5ab1-b651-eb447e6f30a2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__multiple-tags-2/20260926T160211Z-thuan-mac-1/reference/multiple tags 2_da3a18cb-9766-5ab1-b651-eb447e6f30a2.svg'
AUTHOR = "claude-opus-5-5"

POINT, TOP_END, SIDE_END = (34, 6), (20, 6), (34, 20)
RUN = 14                     # long edges run (-RUN, RUN) down the diagonal
EYELET = (26, 14)
BACK = ((42, 14), (42, 24), (24, 42))


class Drawing(Solo48):
    icon_id = 'multiple-tags-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('multiple tags 2', 'tags')
    keywords = ('tags', 'labels', 'price', 'sale', 'category', 'shopping', 'tag')

    def build(self):
        far_top = (TOP_END[0] - RUN, TOP_END[1] + RUN)
        far_side = (SIDE_END[0] - RUN, SIDE_END[1] + RUN)
        self.add_polyline('front', POINT, TOP_END, far_top, far_side, SIDE_END, closed=True)
        self.add_dot('eyelet', EYELET)
        self.add_polyline('back', *BACK)
