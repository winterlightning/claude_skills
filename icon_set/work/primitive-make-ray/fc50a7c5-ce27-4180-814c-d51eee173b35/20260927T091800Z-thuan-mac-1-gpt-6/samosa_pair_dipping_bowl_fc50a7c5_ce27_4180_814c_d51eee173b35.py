"""Samosas with Dipping Bowl."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fc50a7c5-ce27-4180-814c-d51eee173b35'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__samosa-pair-dipping-bowl/20260927T091411Z-thuan-mac-1/reference/salmosa_fc50a7c5-ce27-4180-814c-d51eee173b35.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'samosa-pair-dipping-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('samosa', 'pair', 'dipping', 'bowl')

    # Revision plan: Back and front samosas retain the staggered source layout; the dipping bowl gains a curved lip and rounded body. Asymmetry is intentional. No useful Lucide food match.
    # Revision plan: Back and front samosas retain the staggered source layout; the dipping bowl gains a curved lip and rounded body. Asymmetry is intentional. No useful Lucide food match.
    # Revision plan: Back and front samosas retain the staggered source layout; the dipping bowl gains a curved lip and rounded body. Asymmetry is intentional. No useful Lucide food match.
    # Revision plan: Back and front samosas retain the staggered source layout; the dipping bowl gains a curved lip and rounded body. Asymmetry is intentional. No useful Lucide food match.
    # Revision plan: Back and front samosas retain the staggered source layout; the dipping bowl gains a curved lip and rounded body. Asymmetry is intentional. No useful Lucide food match.
    def build(self):
        # Two diagonally staggered pastry outlines and a true open sauce cup.
        self.add_polyline('back-pastry', (6, 24), (16, 6), (24, 24), closed=True)
        self.add_polyline('front-pastry', (26, 42), (34, 24), (42, 42), closed=True)
        self.add_arc('bowl-rim', (6, 36), (18, 36), radius_x=6, radius_y=3, sweep=True)
        self.add_arc('bowl-body', (18, 36), (6, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('bowl', 'bowl-rim', 'bowl-body', closed=True)
