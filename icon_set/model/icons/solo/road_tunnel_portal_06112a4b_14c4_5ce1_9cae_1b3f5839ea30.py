from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06112a4b-14c4-5ce1-9cae-1b3f5839ea30'
SOURCE_PATH = 'pictographic-primitives/transportation/road tunnel_06112a4b-14c4-5ce1-9cae-1b3f5839ea30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '06112a4b-14c4-5ce1-9cae-1b3f5839ea30', 'source_path': 'pictographic-primitives/transportation/road tunnel_06112a4b-14c4-5ce1-9cae-1b3f5839ea30.svg'}]

class RoadTunnelPortal(Solo48):
    icon_id = 'road-tunnel-portal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('tunnel', 'road tunnel', 'portal', 'arch', 'road', 'underpass', 'highway', 'infrastructure')

    def build(self):
        self.add_line('outer-left',(4,40),(4,28))
        self.add_arc('outer-arch',(4,28),(44,28),radius_x=20,sweep=True)
        self.add_line('outer-right',(44,28),(44,40))
        self.add_contour('outer','outer-left','outer-arch','outer-right')
        self.add_line('inner-left',(15,29),(15,28))
        self.add_arc('inner-arch',(15,28),(33,28),radius_x=9,sweep=True)
        self.add_line('inner-right',(33,28),(33,29))
        self.add_contour('inner','inner-left','inner-arch','inner-right')
        self.add_line('threshold',(15,29),(33,29))
        self.add_line('road-left',(4,40),(15,29))
        self.add_line('road-right',(33,29),(44,40))
        for a,b in (('outer','road-left'),('road-left','inner'),('inner','threshold'),('inner','road-right'),('road-right','outer')):self.relate('connect',a,b)
