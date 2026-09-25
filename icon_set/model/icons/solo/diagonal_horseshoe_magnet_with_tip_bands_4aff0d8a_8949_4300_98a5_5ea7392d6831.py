from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aff0d8a-8949-4300-98a5-5ea7392d6831'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/magnet_4aff0d8a-8949-4300-98a5-5ea7392d6831.svg'
AUTHOR = 'gpt-6'


class DiagonalHorseshoeMagnetWithTipBands(Solo48):
    icon_id = 'diagonal-horseshoe-magnet-with-tip-bands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('magnet', 'horseshoe', 'poles', 'magnetic', 'tool', 'attraction', 'physics', 'metal')

    def build(self) -> None:
        # Concentric U bends use integer 3:4:5 offsets; paired pole bands share depth.
        self.add_line('outer-arm-a',(24,6),(12,15))
        self.add_arc('outer-bend',(12,15),(30,39),radius_x=15,sweep=False)
        self.add_line('outer-arm-b',(30,39),(42,30))
        self.add_line('tip-b',(42,30),(36,22))
        self.add_line('inner-arm-b',(36,22),(24,31))
        self.add_arc('inner-bend',(24,31),(18,23),radius_x=5,sweep=True)
        self.add_line('inner-arm-a',(18,23),(30,14))
        self.add_line('tip-a',(30,14),(24,6))
        self.add_contour('magnet','outer-arm-a','outer-bend','outer-arm-b','tip-b','inner-arm-b','inner-bend','inner-arm-a','tip-a',closed=True)
        for name,a,b in [('band-a',(16,12),(22,20)),('band-b',(34,36),(28,28))]:
            self.add_line(name,a,b);self.relate('connect',name,'magnet')
