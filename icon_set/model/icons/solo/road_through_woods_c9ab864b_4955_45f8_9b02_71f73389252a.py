from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9ab864b-4955-45f8-9b02-71f73389252a'
SOURCE_PATH = 'pictographic-primitives/transportation/road woods_c9ab864b-4955-45f8-9b02-71f73389252a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': 'c9ab864b-4955-45f8-9b02-71f73389252a', 'source_path': 'pictographic-primitives/transportation/road woods_c9ab864b-4955-45f8-9b02-71f73389252a.svg'}]

class RoadThroughWoods(Solo48):
    icon_id = 'road-through-woods'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('road', 'forest', 'woods', 'scenic route', 'tree', 'curve', 'countryside', 'drive')

    def build(self):
        self.add_polyline('pine',(6,16),(11,6),(16,16),(11,16),closed=True)
        self.add_line('trunk',(11,16),(11,20))
        self.relate('connect','pine','trunk')
        self.add_arc('road-edge',(6,42),(42,14),radius_x=46,radius_y=46,sweep=True)
        self.add_arc('road-dash-low',(18,42),(22,34),radius_x=38,radius_y=38,sweep=True)
        self.add_arc('road-dash-high',(31,27),(42,23),radius_x=38,radius_y=38,sweep=True)
