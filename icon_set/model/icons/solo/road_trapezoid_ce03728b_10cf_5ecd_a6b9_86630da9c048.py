from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce03728b-10cf-5ecd-a6b9-86630da9c048'
SOURCE_PATH = 'pictographic-primitives/transportation/road straight_ce03728b-10cf-5ecd-a6b9-86630da9c048.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': 'ce03728b-10cf-5ecd-a6b9-86630da9c048', 'source_path': 'pictographic-primitives/transportation/road straight_ce03728b-10cf-5ecd-a6b9-86630da9c048.svg'}]

class RoadTrapezoid(Solo48):
    icon_id = 'road-trapezoid'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('road', 'straight road', 'highway', 'lane', 'street', 'perspective', 'route', 'driving')

    def build(self):
        self.add_polyline('road',(14,4),(24,4),(34,4),(40,44),(24,44),(8,44),closed=True)
        self.add_line('upper-dash',(24,4),(24,12))
        self.add_line('middle-dash',(24,22),(24,26))
        self.add_line('lower-dash',(24,36),(24,44))
        self.relate('connect','road','upper-dash')
        self.relate('connect','road','lower-dash')
