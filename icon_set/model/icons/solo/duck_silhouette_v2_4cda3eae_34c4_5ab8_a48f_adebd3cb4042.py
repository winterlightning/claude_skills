# Variant of duck-silhouette; parent file remains unchanged.
'Duck with a broad bill and visible eye. HRECT_L (2,8)-(46,40) retains its swimming silhouette. Lucide bird informed the rounded head and clear eye; triangular bill replaced. Deliberate right-facing asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cda3eae-34c4-5ab8-a48f-adebd3cb4042'
SOURCE_PATH = 'pictographic-primitives/animals/chick_4cda3eae-34c4-5ab8-a48f-adebd3cb4042.svg'
AUTHOR = 'gpt-6'

class DuckSilhouetteVariant2(Solo48):
    icon_id = 'duck-silhouette-v2'
    variant_of = 'duck-silhouette'
    variant_label = 'Clearer duck bill and eye'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('duck', 'bird', 'rubber duck', 'toy', 'bath', 'silhouette', 'poultry', 'minimal')

    def build(self) -> None:
        self.add_arc('head-back', (22, 18), (32, 8), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('crown', (32, 8), (40, 16), radius_x=8, radius_y=8, sweep=True)
        self.add_line('bill-1', (40, 16), (46, 16))
        self.add_line('bill-2', (46, 16), (46, 24))
        self.add_line('bill-bottom', (46,24), (40,24))
        self.add_dot('eye',(32,17))
        self.add_line('breast', (40, 24), (40, 26))
        self.add_arc('belly-right', (40, 26), (26, 40), radius_x=14, radius_y=14, sweep=True)
        self.add_line('belly', (26, 40), (18, 40))
        self.add_arc('belly-left', (18, 40), (2, 24), radius_x=16, radius_y=16, sweep=True)
        self.add_line('tail', (2, 24), (7, 20))
        self.add_arc('scoop', (7, 20), (14, 27), radius_x=7, radius_y=7, sweep=False)
        self.add_line('back', (14, 27), (19, 27))
        self.add_arc('neck', (19, 27), (22, 24), radius_x=3, radius_y=3, sweep=False)
        self.add_line('neck-rise', (22, 24), (22, 18))
        self.add_contour('outline', 'head-back', 'crown', 'bill-1', 'bill-2', 'bill-bottom', 'breast', 'belly-right', 'belly', 'belly-left', 'tail', 'scoop', 'back', 'neck', 'neck-rise', closed=True)
