'Underwater drone twin thrusters: independent spacing revision.\n\nRaise capsule body to leave eight units above both lower arm returns.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4756649f-fa81-4c81-bfa9-f4206356d978'
SOURCE_PATH = 'pictographic-primitives/war/underwater drone_4756649f-fa81-4c81-bfa9-f4206356d978.svg'
AUTHOR = 'gpt-6'

class UnderwaterDroneTwinThrusters(Solo48):
    icon_id = 'underwater-drone-twin-thrusters'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('underwater', 'drone', 'thruster', 'robot', 'submersible', 'marine')

    def build(self):
        self.add_polyline('water',(4, 8),(12, 11),(24, 8),(36, 11),(44, 8),closed=False)
        self.add_polyline('top',(9, 22),(12, 22),(36, 22),(39, 22),closed=False)
        self.add_arc('right',(39, 22),(39, 32),radius_x=5,radius_y=5,sweep=True)
        self.add_polyline('bottom',(39, 32),(32, 32),(16, 32),(9, 32),closed=False)
        self.add_arc('left',(9, 32),(9, 22),radius_x=5,radius_y=5,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'top']
        self.contours = [c for c in self.contours if c.contour_id != 'bottom']
        self.add_contour('body','top-1','top-2','top-3','right','bottom-1','bottom-2','bottom-3','left',closed=True)
        self.add_line('thruster-left',(12, 22),(12, 20))
        self.add_line('thruster-right',(36, 22),(36, 20))
        self.add_polyline('leg-left',(16, 32),(16, 40),(10, 40),closed=False)
        self.add_polyline('leg-right',(32, 32),(32, 40),(38, 40),closed=False)
        self.relate('connect','body','thruster-left')
        self.relate('connect','body','thruster-right')
        self.relate('connect','body','leg-left')
        self.relate('connect','body','leg-right')
