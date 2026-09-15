'Cracked house: straight roof and walls, widened doorway and a deliberate fracture.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2dd0d16e-d067-5be6-9ccf-bb8095c51fc8'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/poverty housing_2dd0d16e-d067-5be6-9ccf-bb8095c51fc8.svg'
AUTHOR = 'gpt-6'


class CrackedHouseWithChimney(Solo48):
    icon_id = 'cracked-house-with-chimney'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('house', 'home', 'damage', 'crack', 'poverty', 'housing', 'shelter', 'chimney', 'repair')

    def build(self):
        # Cracked house: straight roof and walls, widened doorway and a deliberate fracture.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('house',(6,42),(6,22),(24,6),(42,22),(42,42),(6,42))
        p('chimney',(32,13),(32,6),(42,6),(42,22))
        link('connect','house','chimney')
        p('crack',(16,13),(20,23),(28,23),(32,30))
        link('connect','crack','house')
        p('door',(16,42),(16,34),(26,34),(26,42))
        link('connect','door','house')
