"""Burning barrel with tall uneven flame rising from its open top. VRECT_L fits the flame height and projecting rim. Shared rim nodes connect flame and barrel walls; hoop endpoints split the walls. Source provides banded drum and uneven flame tips; Lucide flame informs coherent curling curves. Small right flame tongue and extra closely spaced hoops omitted; one central band retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'df81c924-5e51-4958-ae59-789be142bbab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/mario 2_df81c924-5e51-4958-ae59-789be142bbab.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'burning-barrel-tall-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("video-games", "primitive", "primitives")
    aliases = ('Burning Barrel with Tall Flame',)
    keywords = ('burning', 'barrel', 'tall', 'flame')
    def build(self):
        self.add_bezier('flame',(12,24),((10,18),(14,10),(16,10)),((16,14),(18,16),(20,16)),((24,10),(24,8),(22,4)),((34,8),(38,16),(36,24)))
        points=[(8,24),(12,24),(36,24),(40,24)]
        for i in range(3):
            self.add_line('rim-'+str(i),points[i],points[i+1])
        self.add_contour('rim',*[f'rim-{i}' for i in range(3)])
        self.add_polyline('barrel',(12,24),(12,34),(12,44),(36,44),(36,34),(36,24))
        self.add_line('hoop',(12,34),(36,34))
        self.relate('connect','flame','rim','barrel')
        self.relate('connect','hoop','barrel')
