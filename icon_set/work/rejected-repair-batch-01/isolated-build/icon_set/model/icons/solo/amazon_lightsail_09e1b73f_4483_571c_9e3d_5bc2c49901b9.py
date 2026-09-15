'Lightsail mark: preserve the curved asymmetric sail within its circular rim; replace fragmented conversion arcs with flowing curves.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09e1b73f-4483-571c-9e3d-5bc2c49901b9'
SOURCE_PATH = 'pictographic-primitives/programing/amazon lightsail_09e1b73f-4483-571c-9e3d-5bc2c49901b9.svg'
AUTHOR = 'gpt-6'

class AmazonLightsail(Solo48):
    icon_id = 'amazon-lightsail'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'lightsail', 'programing')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        # Preserve the asymmetric sail, using three coherent curved runs.
        self.add_bezier('sail-back',(26,13),((31,19),(31,29),(26,35)))
        self.add_bezier('sail-lower',(26,35),((25,29),(21,25),(16,24)))
        self.add_bezier('sail-upper',(16,24),((21,22),(25,18),(26,13)))
        self.add_contour('sail','sail-back','sail-lower','sail-upper',closed=True)
