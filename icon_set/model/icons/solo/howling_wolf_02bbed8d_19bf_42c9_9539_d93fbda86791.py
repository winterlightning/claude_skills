"""Widen the ear group and deepen its central notch; bring the back of the neck into the enlarged head. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02bbed8d-19bf-42c9-9539-d93fbda86791'
SOURCE_PATH = 'pictographic-primitives/animals/wolf body howl_02bbed8d-19bf-42c9-9539-d93fbda86791.svg'
AUTHOR = 'gpt-6'

class HowlingWolf(Solo48):
    icon_id = 'howling-wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('wolf', 'howl', 'standing', 'moon', 'wild', 'canine', 'night', 'wilderness')

    def build(self):
        """Symbol plan: Widen the ear group and deepen its central notch; bring the back of the neck into the enlarged head. Reference: Lucide dog and cat: clear ear silhouettes; deliberate howling profile."""
        self.add_polyline('muzzle', (26, 14), (26, 6), (34, 12), (42, 6), (42, 24), closed=False)
        self.add_line('chest', (42, 24), (40, 32))
        self.add_polyline('front', (40, 32), (40, 42), (32, 42), (32, 32), closed=False)
        self.add_line('belly', (32, 32), (24, 32))
        self.add_polyline('rear', (24, 32), (24, 42), (16, 42), (16, 32), closed=False)
        self.add_arc('haunch', (16, 32), (24, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('shoulder', (24, 24), (26, 14), radius_x=10, radius_y=10, sweep=False)
        self.contours = [c for c in self.contours if c.contour_id != 'muzzle']
        self.contours = [c for c in self.contours if c.contour_id != 'front']
        self.contours = [c for c in self.contours if c.contour_id != 'rear']
        self.add_contour('body', 'muzzle-1', 'muzzle-2', 'muzzle-3', 'muzzle-4', 'chest', 'front-1', 'front-2', 'front-3', 'belly', 'rear-1', 'rear-2', 'rear-3', 'haunch', 'shoulder', closed=True)
        self.add_line('tail', (16, 32), (6, 42))
        self.relate('connect', 'body', 'tail')
