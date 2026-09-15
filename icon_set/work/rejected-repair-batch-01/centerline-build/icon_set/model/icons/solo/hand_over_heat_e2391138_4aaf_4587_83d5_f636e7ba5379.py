"""A palm-down hand reaches over two rising heat waves. SQUARE extremes (6,6)-(42,42). Lucide hand-platter informs the folded thumb; waves-vertical informs the repeated smooth waves. Reduce each wave to one S bend. Preserve the reaching direction and two heat lines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'pictographic-primitives/symbol/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'
AUTHOR = 'gpt-6'


class HandOverHeat(Solo48):
    icon_id = 'hand-over-heat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('hand', 'heat', 'warm', 'hot', 'temperature', 'steam', 'burn', 'sensation')

    def build(self) -> None:
        self.add_polyline('upper-hand',(6,20),(20,8),(34,8))
        self.add_polyline('fingers',(6,20),(18,16),(26,16))
        self.relate('connect','upper-hand','fingers')
        self.add_line('thumb-side',(18,16),(18,20))
        self.add_arc('thumb-turn',(18,20),(22,24),radius_x=4,sweep=False)
        self.add_line('palm',(22,24),(30,24))
        self.add_line('wrist',(30,24),(42,6))
        self.add_contour('lower-hand','thumb-side','thumb-turn','palm','wrist')
        self.relate('connect','fingers','lower-hand')
        for i,x in enumerate((18,30)):
            self.add_arc(f'heat-{i}-a',(x,33),(x-2,35),radius_x=2,sweep=False)
            self.add_arc(f'heat-{i}-b',(x-2,35),(x,37),radius_x=2,sweep=False)
            self.add_arc(f'heat-{i}-c',(x,37),(x+2,39),radius_x=2)
            self.add_arc(f'heat-{i}-d',(x+2,39),(x,42),radius_x=2,radius_y=3)
            self.add_contour(f'heat-{i}',*(f'heat-{i}-'+part for part in 'abcd'))
