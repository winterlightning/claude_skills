from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d3723db-7bfa-4f0d-bb6b-3f7514e9cc87'
SOURCE_PATH = 'pictographic-primitives/transportation/rear fog lamp_3d3723db-7bfa-4f0d-bb6b-3f7514e9cc87.svg'
AUTHOR = 'gpt-6'

class RearFogLamp(Solo48):
    icon_id = 'rear-fog-lamp'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('rear fog lamp', 'fog light', 'lamp', 'car', 'dashboard', 'lighting', 'indicator', 'fog')

    def build(self):
        self.add_arc('lens',(20,8),(20,40),radius_x=16,sweep=False)
        self.add_line('lens-back',(20,40),(20,8))
        self.add_contour('lamp','lens','lens-back',closed=True)
        self.add_arc('fog-upper',(36,8),(34,20),radius_x=37,radius_y=37,sweep=False)
        self.add_line('fog-middle',(34,20),(34,28))
        self.add_arc('fog-lower',(34,28),(32,40),radius_x=37,radius_y=37,sweep=True)
        self.add_contour('fog','fog-upper','fog-middle','fog-lower')
        for y in (20,28):
            n=f'beam-{y}'
            self.add_polyline(n,(29,y),(34,y),(44,y))
            self.relate('connect',n,'fog')
