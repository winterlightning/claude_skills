from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfc8d394-09c5-5059-9251-0449ae250baa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/picker_cfc8d394-09c5-5059-9251-0449ae250baa.svg'
AUTHOR = 'gpt-6'


class UprightEyedropperWithTwoGraduations(Solo48):
    icon_id = 'upright-eyedropper-with-two-graduations'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('eyedropper', 'dropper', 'pipette', 'liquid', 'color', 'graduations', 'tool', 'sampler')

    def build(self) -> None:
        # Shared x=24 axis; bulb, collar, graduated barrel and narrowed tip.
        self.add_line('cap-left',(16,16),(16,12))
        self.add_arc('cap-arch',(16,12),(32,12),radius_x=8)
        self.add_line('cap-right',(32,12),(32,16))
        self.add_contour('cap','cap-left','cap-arch','cap-right')
        self.add_polyline('body',(16,16),(16,24),(16,32),(20,36),(20,44),(28,44),(28,36),(32,32),(32,16),closed=True)
        self.relate('connect','cap','body')
        for side,a,b in [('left',(10,16),(16,16)),('right',(32,16),(38,16))]:
            name='collar-'+side
            self.add_line(name,a,b)
            self.relate('connect',name,'cap');self.relate('connect',name,'body')
        for y in (24,32):
            name=f'graduation-{y}'
            self.add_line(name,(16,y),(22,y));self.relate('connect',name,'body')
