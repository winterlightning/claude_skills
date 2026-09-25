"""Arrow Up with Dashed Tail.

Plan: VRECT centerlines (8,4)-(40,44); mirror a broad arrowhead and 12-unit shaft; one pair of dashes separated by 8.
Construction references: Lucide arrow-big-up: continuous broad arrowhead and parallel shaft.
Reduction: Reduced each tail to one dash and regularized the source’s uneven dash lengths; both source UUIDs retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '042844f7-9e69-44c7-91bb-6be3830d4b9b'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dash up_042844f7-9e69-44c7-91bb-6be3830d4b9b.svg'
SOURCE_ICON_IDS = ('042844f7-9e69-44c7-91bb-6be3830d4b9b', '5443e1f9-f37f-4884-b268-88955bf863e3')
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow dash up_042844f7-9e69-44c7-91bb-6be3830d4b9b.svg', 'pictographic-primitives/arrows/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg')
AUTHOR = 'gpt-6'


class ArrowUpWithDashedTail(Solo48):
    icon_id = 'arrow-up-with-dashed-tail'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'up', 'with', 'dashed', 'tail')

    def build(self) -> None:
        axis, shaft_half = 24, 6
        left, right = axis-shaft_half, axis+shaft_half
        self.add_polyline("head-and-shaft",(left,32),(left,20),(8,20),(axis,4),(40,20),(right,20),(right,32))
        for side,x in [("left",left),("right",right)]:
            self.add_line(f"dash-{side}",(x,40),(x,44))
