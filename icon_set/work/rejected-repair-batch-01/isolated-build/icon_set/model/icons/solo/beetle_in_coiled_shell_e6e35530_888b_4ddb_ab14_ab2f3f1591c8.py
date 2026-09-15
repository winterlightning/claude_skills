'Beetle in coiled shell v2. True twenty-unit shell radius; six legs spaced eight units apart around a compact beetle body, with short antennae.\nOriginal subject geometry is retained and refitted to the current native keyshape. Directional asymmetry is intentional. Construction review: original drawing; sprout or bug principles for the plant and beetle.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e6e35530-888b-4ddb-ab14-ab2f3f1591c8'
SOURCE_PATH = 'pictographic-primitives/animals/insect earth_e6e35530-888b-4ddb-ab14-ab2f3f1591c8.svg'
AUTHOR = 'gpt-6'

class BeetleInCoiledShell(Solo48):
    icon_id = 'beetle-in-coiled-shell'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('insect', 'beetle', 'shell', 'coil', 'spiral', 'cocoon', 'bug', 'nest')

    def build(self):
        self.add_arc('shell-top',(24, 4),(44, 24),radius_x=20,radius_y=20,sweep=True)
        self.add_arc('shell-bottom',(44, 24),(24, 44),radius_x=20,radius_y=20,sweep=True)
        self.add_arc('shell-left',(24, 44),(4, 24),radius_x=20,radius_y=20,sweep=True)
        self.add_contour('shell','shell-top','shell-bottom','shell-left',closed=False)
        self.add_polyline('body',(20, 16),(28, 16),(28, 24),(28, 32),(20, 32),(20, 24),closed=True)
        self.add_line('antenna-left',(20, 16),(20, 14))
        self.add_line('antenna-right',(28, 16),(28, 14))
        self.add_line('leg-left-top',(20, 16),(17, 16))
        self.add_line('leg-right-top',(28, 16),(31, 16))
        self.add_line('leg-left-mid',(20, 24),(14, 24))
        self.add_line('leg-right-mid',(28, 24),(34, 24))
        self.add_line('leg-left-bottom',(20, 32),(18, 32))
        self.add_line('leg-right-bottom',(28, 32),(30, 32))
        self.relate('connect','body','antenna-left')
        self.relate('connect','body','antenna-right')
        self.relate('connect','body','leg-left-top')
        self.relate('connect','body','leg-right-top')
        self.relate('connect','body','leg-left-mid')
        self.relate('connect','body','leg-right-mid')
        self.relate('connect','body','leg-left-bottom')
        self.relate('connect','body','leg-right-bottom')
        self.relate('connect','antenna-left','leg-left-top')
        self.relate('connect','antenna-right','leg-right-top')
