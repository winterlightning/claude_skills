"""Bird Hunter. Upper-body hunter aims left beneath a bird silhouette; omit doubled gun and arm outlines, keep raised wings.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3025dd06-abf8-561c-a34e-645334e08f61'
SOURCE_PATH = 'pictographic-primitives/recreation/hunting_3025dd06-abf8-561c-a34e-645334e08f61.svg'
AUTHOR = 'gpt-6'


class BirdHunter(Solo48):
    icon_id = 'bird-hunter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('bird', 'hunter')

    def build(self) -> None:
        self.add_arc('head-top', (32, 22), (38, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (38, 22), (32, 22), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso-1', (31, 42), (31, 34))
        self.add_line('torso-2', (31, 34), (37, 33))
        self.add_line('torso-3', (37, 33), (42, 37))
        self.add_line('torso-4', (42, 37), (42, 42))
        self.add_contour('torso', 'torso-1', 'torso-2', 'torso-3', 'torso-4', closed=False)
        self.add_line('arms-1', (31, 34), (23, 37))
        self.add_line('arms-2', (23, 37), (17, 29))
        self.add_contour('arms', 'arms-1', 'arms-2', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_line('gun-1', (6, 23), (17, 29))
        self.add_line('gun-2', (17, 29), (26, 34))
        self.add_contour('gun', 'gun-1', 'gun-2', closed=False)
        self.relate("connect", 'gun', 'arms')
        self.add_line('bird-1', (6, 6), (13, 12))
        self.add_line('bird-2', (13, 12), (20, 6))
        self.add_contour('bird', 'bird-1', 'bird-2', closed=False)
