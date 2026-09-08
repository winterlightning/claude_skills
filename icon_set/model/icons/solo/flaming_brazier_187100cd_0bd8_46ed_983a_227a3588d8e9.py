"""A curling flame rising above a bowl on splayed legs. VRECT_XL extremes (5,2)-(43,46). Lucide flame informs the asymmetric hook; omit the inner flame and redundant legs."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '187100cd-0bd8-46ed-983a-227a3588d8e9'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/greek fire_187100cd-0bd8-46ed-983a-227a3588d8e9.svg'


class FlamingBrazier(Solo48):
    icon_id = 'flaming-brazier'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('brazier', 'fire', 'flame', 'greek', 'olympic', 'torch', 'ritual', 'ancient')

    def build(self) -> None:
        self.add_arc('flame-left',(15,19),(18,11),radius_x=13)
        self.add_arc('flame-notch',(18,11),(24,9),radius_x=4,sweep=False)
        self.add_arc('flame-hook',(24,9),(26,2),radius_x=10,sweep=False)
        self.add_arc('flame-right',(26,2),(33,19),radius_x=22)
        self.add_contour('flame','flame-left','flame-notch','flame-hook','flame-right')
        self.add_line('rim',(5,26),(43,26))
        self.add_arc('bowl-right',(43,26),(35,35),radius_x=19)
        self.add_arc('bowl-bottom',(35,35),(13,35),radius_x=19)
        self.add_arc('bowl-left',(13,35),(5,26),radius_x=19)
        self.add_contour('bowl','rim','bowl-right','bowl-bottom','bowl-left',closed=True)
        self.add_line('leg-left',(13,35),(10,46))
        self.add_line('leg-right',(35,35),(38,46))
        self.relate('connect','bowl','leg-left')
        self.relate('connect','bowl','leg-right')
