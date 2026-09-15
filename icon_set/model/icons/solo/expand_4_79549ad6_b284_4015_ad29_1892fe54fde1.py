'Expand: four equal reflected corner arrows with actual shared tips.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79549ad6-b284-4015-ad29-1892fe54fde1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand 4_79549ad6-b284-4015-ad29-1892fe54fde1.svg'
AUTHOR = 'gpt-6'

class Expand4(Solo48):
    icon_id = 'expand-4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self) -> None:
        # Reflect one complete corner arrow around the shared centre.
        for i,(sx,sy) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
            def p(x,y): return 24+sx*(x-24),24+sy*(y-24)
            self.add_polyline(f'head-{i}',p(14,6),p(6,6),p(6,14))
            self.add_line(f'shaft-{i}',p(6,6),p(17,17))
            self.relate('connect',f'head-{i}',f'shaft-{i}')
