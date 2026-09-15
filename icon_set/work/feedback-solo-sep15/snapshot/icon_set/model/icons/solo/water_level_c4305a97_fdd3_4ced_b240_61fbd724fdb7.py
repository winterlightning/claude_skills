"""water-level: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4305a97-fdd3-4ced-b240-61fbd724fdb7'
SOURCE_PATH = 'pictographic-primitives/weather/water level_c4305a97-fdd3-4ced-b240-61fbd724fdb7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WaterLevel(Solo48):
    icon_id = 'water-level'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('water', 'level', 'weather')

    def build(self):
        # Plan: HRECT_L; repeated matching water scallops and identical base corners.
        # Reference: Geometric repeated wave construction.
        self.add_line('left',(4,8),(4,35))
        self.add_arc('left-bottom',(4,35),(9,40),radius_x=5,sweep=False)
        self.add_line('bottom',(9,40),(39,40))
        self.add_arc('right-bottom',(39,40),(44,35),radius_x=5,sweep=False)
        self.add_line('right',(44,35),(44,8))
        self.add_contour('vessel','left','left-bottom','bottom','right-bottom','right')
        for row,y in enumerate((14,25)):
            points=(4,17,31,44)
            for i,(a,b) in enumerate(zip(points,points[1:])):
                self.add_bezier(f'wave-{row}-{i}',(a,y),(((a+b)/2-2,y+5),((a+b)/2+2,y+5),(b,y)))
            self.add_contour(f'water-{row}',*(f'wave-{row}-{i}' for i in range(3)))
            self.relate('connect',f'water-{row}','vessel')
