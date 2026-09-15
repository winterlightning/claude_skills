'Projecting cap: circular pivot and centered projection within the open frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b681a1fd-f413-5651-8984-b19bea2f0e24'
SOURCE_PATH = 'pictographic-primitives/construction/projecting cap_b681a1fd-f413-5651-8984-b19bea2f0e24.svg'
AUTHOR = 'gpt-6'

class ProjectingCap(Solo48):
    icon_id = 'projecting-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('projecting', 'cap', 'construction')

    def build(self) -> None:
        self.add_polyline('frame',(44,8),(4,8),(4,40),(44,40))

        self.add_arc('pivot-top', (13,24), (21,24), radius_x=4, radius_y=4)
        self.add_arc('pivot-bottom', (21,24), (13,24), radius_x=4, radius_y=4)
        self.add_contour('pivot', 'pivot-top', 'pivot-bottom', closed=True)
        self.add_line('projection',(21,24),(44,24))
        self.relate('connect','projection','pivot')
