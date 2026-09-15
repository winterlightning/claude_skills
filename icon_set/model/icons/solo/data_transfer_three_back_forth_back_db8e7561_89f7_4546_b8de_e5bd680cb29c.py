'Three transfer arrows: equal row spacing and equal arrowhead heights keep the alternating directions clear.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db8e7561-89f7-4546-b8de-e5bd680cb29c'
SOURCE_PATH = 'pictographic-primitives/networks/data transfer three back forth back_db8e7561-89f7-4546-b8de-e5bd680cb29c.svg'
AUTHOR = 'gpt-6'

class DataTransferThreeBackForthBack(Solo48):
    icon_id = 'data-transfer-three-back-forth-back'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('data', 'transfer', 'three', 'back', 'forth', 'networks')

    def build(self) -> None:
        for i,y in enumerate((12,24,36)):
            if i==1:
                self.add_line('shaft-mid',(12,y),(44,y))
                self.add_polyline('head-mid',(16,y-4),(12,y),(16,y+4))
                self.relate('connect','shaft-mid','head-mid')
            else:
                self.add_line(f'shaft-{i}',(4,y),(38,y))
                self.add_polyline(f'head-{i}',(34,y-4),(38,y),(34,y+4))
                self.relate('connect',f'shaft-{i}',f'head-{i}')
