"""A radiation trefoil with three outlined blades and center dot. CIRCLE centerline radius20, ink radius22. Lucide radiation informs annular sectors and the isolated center. Integer 3-4-5 radial points preserve coherent radii; upper blades mirror each other and the lower blade centers on the vertical axis."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c73451e-64e9-4a9b-855d-6d5ab86c3167'
SOURCE_PATH = 'pictographic-primitives/symbol/nuclear energy_2c73451e-64e9-4a9b-855d-6d5ab86c3167.svg'
AUTHOR = 'gpt-6'


class RadiationTrefoil(Solo48):
    icon_id = 'radiation-trefoil'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('radiation', 'nuclear', 'energy', 'radioactive', 'hazard', 'trefoil', 'warning', 'atomic')

    def build(self) -> None:
        self.add_arc('right-outer',(36,8),(44,24),radius_x=20)
        self.add_line('right-low',(44,24),(34,24))
        self.add_arc('right-inner',(34,24),(30,16),radius_x=10,sweep=False)
        self.add_line('right-high',(30,16),(36,8))
        self.add_contour('right','right-outer','right-low','right-inner','right-high',closed=True)
        self.add_arc('left-outer',(4,24),(12,8),radius_x=20)
        self.add_line('left-high',(12,8),(18,16))
        self.add_arc('left-inner',(18,16),(14,24),radius_x=10,sweep=False)
        self.add_line('left-low',(14,24),(4,24))
        self.add_contour('left','left-outer','left-high','left-inner','left-low',closed=True)
        self.add_arc('bottom-outer',(36,40),(12,40),radius_x=20)
        self.add_line('bottom-left',(12,40),(18,32))
        self.add_arc('bottom-inner',(18,32),(30,32),radius_x=10,sweep=False)
        self.add_line('bottom-right',(30,32),(36,40))
        self.add_contour('bottom','bottom-outer','bottom-left','bottom-inner','bottom-right',closed=True)
        self.add_dot('center',(24,24))
