"""Fresh SOLO48 revision of burning-crashed-aircraft from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '81f5c526-61a1-4426-afae-2fec80a31cb2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__burning-crashed-aircraft/20260927T071330Z-thuan-mac-1/reference/plane crashed_81f5c526-61a1-4426-afae-2fec80a31cb2.svg'
AUTHOR = 'gpt-6'

class BurningCrashedAircraft(Solo48):
    icon_id = 'burning-crashed-aircraft'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('aircraft', 'crash', 'fire', 'smoke', 'flame', 'wreck')

    def build(self) -> None:

        # Broken left wing and narrow flaming fuselage, source facing down-right.
        poly(self,'aircraft',(8,26),(19,31),(18,18),(27,23),(29,34),
             (40,34),(40,44),(26,44),(8,36),closed=True)
        self.add_bezier('flame',(27,23),((30,16),(26,13),(30,6)),
                        ((34,11),(40,16),(38,23)),((36,28),(38,31),(38,34)))
        line(self,'smoke',(12,4),(10,13))
        contacts(self)
