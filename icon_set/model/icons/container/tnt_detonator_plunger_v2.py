# Variant of tnt-detonator-plunger; parent file remains unchanged.
'Tnt detonator plunger: independent spacing revision.\n\nEight-unit wire/box and wire-loop spacing; preserve T plunger and curling wire.\nNative container family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class TntDetonatorPlungerVariant2(Container64):
    icon_id = 'tnt-detonator-plunger-v2'
    variant_of = 'tnt-detonator-plunger'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ()
    keywords = ('tnt', 'detonator', 'plunger')

    def build(self) -> None:
        self.add_line('box-top', (5, 20), (37, 20))
        self.add_arc('box-ne', (37, 20), (40, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-right', (40, 23), (40, 59))
        self.add_arc('box-se', (40, 59), (37, 62), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-bottom', (37, 62), (5, 62))
        self.add_arc('box-sw', (5, 62), (2, 59), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-left', (2, 59), (2, 23))
        self.add_arc('box-nw', (2, 23), (5, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('box', 'box-top', 'box-ne', 'box-right', 'box-se', 'box-bottom', 'box-sw', 'box-left', 'box-nw', closed=True)
        self.add_line('plunger', (21, 2), (21, 20))
        self.add_line('handle', (9, 2), (33, 2))
        self.relate('connect', 'handle', 'plunger')
        self.relate('connect', 'plunger', 'box')
        self.add_line('wire-out', (40, 52), (44, 52))
        self.add_arc('wire-up', (44, 52), (48, 48), radius_x=4, radius_y=4, sweep=False)
        self.add_line('wire-rise', (48, 48), (48, 38))
        self.add_arc('wire-crest', (48, 38), (56, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('wire-fall', (56, 38), (56, 58))
        self.add_arc('wire-foot', (56, 58), (60, 62), radius_x=4, radius_y=4, sweep=False)
        self.add_line('wire-end', (60, 62), (62, 62))
        self.add_contour('wire', 'wire-out', 'wire-up', 'wire-rise', 'wire-crest', 'wire-fall', 'wire-foot', 'wire-end', closed=False)
        self.relate('connect', 'wire', 'box')

SOURCE_ICON_ID = None

SOURCE_PATH = None
