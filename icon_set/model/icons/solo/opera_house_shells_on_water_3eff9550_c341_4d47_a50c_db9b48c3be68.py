"""Stepping shell roofs over harbour waves; small cloud omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3eff9550-c341-4d47-a50c-db9b48c3be68'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/sydney opera house_3eff9550-c341-4d47-a50c-db9b48c3be68.svg'
AUTHOR = 'gpt-6'

class OperaHouseShellsOnWater(Solo48):
    icon_id = 'opera-house-shells-on-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('sydney opera house', 'australia', 'shells', 'sails', 'harbour', 'water', 'landmark', 'cloud')

    def build(self) -> None:
        # HRECT_L centerline extremes (2,8)-(46,40).
        self.add_line('base', (2, 30), (46, 30))
        self.add_line('left-front-1', (7, 30), (2, 19))
        self.add_arc('left-roof', (2, 19), (19, 24), radius_x=23, sweep=True)
        self.add_line('main-front', (19, 24), (15, 8))
        self.add_arc('main-roof', (15, 8), (32, 24), radius_x=24, sweep=True)
        self.add_arc('right-roof', (32, 24), (46, 20), radius_x=23, sweep=True)
        self.add_line('right-front', (46, 20), (41, 30))
        self.add_contour('shells', 'left-front-1', 'left-roof', 'main-front', 'main-roof', 'right-roof', 'right-front')
        self.relate('connect', 'shells', 'base')
        self.add_arc('wave-left', (2, 37), (24, 37), radius_x=11, radius_y=3, sweep=False)
        self.add_arc('wave-right', (24, 37), (46, 37), radius_x=11, radius_y=3, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right')
