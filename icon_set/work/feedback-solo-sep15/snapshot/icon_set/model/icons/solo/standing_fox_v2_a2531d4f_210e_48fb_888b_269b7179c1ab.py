"""Simplify the fox head to a pointed ear and one clear triangular muzzle; remove the small forehead and jaw curves. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2531d4f-210e-48fb-888b-269b7179c1ab'
SOURCE_PATH = 'pictographic-primitives/animals/fox body_a2531d4f-210e-48fb-888b-269b7179c1ab.svg'
AUTHOR = 'gpt-6'

class StandingFoxVariant2(Solo48):
    icon_id = 'standing-fox-v2'
    variant_of = 'standing-fox'
    variant_label = 'Simplify the fox head to a pointed ear and one clear triangular muzzle; remove the small forehead and jaw curves.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('standing', 'fox')

    def build(self) -> None:
        """Symbol plan: Simplify the fox head to a pointed ear and one clear triangular muzzle; remove the small forehead and jaw curves. Reference: Lucide cat: economical pointed ears and muzzle."""
        self.add_arc('tail-outer-top', (6, 17), (14, 6), radius_x=12, radius_y=15, sweep=True)
        self.add_bezier('tail-inner', (14, 6), ((20, 13), (19, 22), (12, 26)))
        self.add_bezier('tail-outer-low', (6, 32), *(((6, 27.35898385), (6, 21.64101615), (6, 17)),))
        self.add_contour('tail', 'tail-outer-low', 'tail-outer-top', 'tail-inner')
        self.add_arc('hip-top', (12, 26), (16, 24), radius_x=4, radius_y=2, sweep=True)
        self.add_line('back', (16, 24), (26, 24))
        self.add_arc('chest', (34, 32), (32, 38), radius_x=6, radius_y=6, sweep=False)
        self.add_line('foreleg', (32, 38), (32, 42))
        self.add_line('hind', (6, 32), (6, 40))
        self.add_line('rear-foot', (6, 40), (6, 42))
        self.add_contour('rear', 'hind', 'rear-foot')
        self.relate('connect', 'rear', 'tail')
        self.add_arc('haunch', (18, 30), (10, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_line('hip-low', (10, 38), (6, 40))
        self.add_contour('thigh', 'haunch', 'hip-low')
        self.add_line('belly', (10, 38), (32, 38))
        self.relate('connect', 'thigh', 'belly')
        self.relate('connect', 'rear', 'thigh')
        self.add_polyline('head-new', (26, 24), (32, 6), (36, 18), (42, 24), (34, 32))
        self.contours=[c for c in self.contours if c.contour_id!='head-new']
        self.add_contour('upper', 'hip-top', 'back', 'head-new-1', 'head-new-2', 'head-new-3', 'head-new-4', 'chest', 'foreleg')
        self.relate('connect', 'upper', 'tail')
        self.relate('connect', 'upper', 'belly')
