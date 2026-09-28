from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66813d78-0e72-4003-9931-01ed34939450'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad_66813d78-0e72-4003-9931-01ed34939450.svg'
AUTHOR = 'gpt-6'

class RailwayTrack(Solo48):
    icon_id = 'railway-track'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('railway', 'track', 'rail', 'railroad', 'sleepers', 'train', 'line', 'tracks')

    def build(self):
        for x,side in ((16,'left'),(32,'right')):
            self.add_polyline(side+'-rail',(x,4),(x,12),(x,24),(x,36),(x,44))
        for y in (12,24,36):
            n=f'sleeper-{y}'
            self.add_polyline(n,(8,y),(16,y),(32,y),(40,y))
            self.relate('connect',n,'left-rail')
            self.relate('connect',n,'right-rail')
