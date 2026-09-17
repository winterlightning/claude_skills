from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca791817-3557-5e40-ac57-04c27dd3e3c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker_ca791817-3557-5e40-ac57-04c27dd3e3c9.svg'
AUTHOR = 'gpt-6'


class DiagonalEyedropperOverSampleTray(Solo48):
    icon_id = 'diagonal-eyedropper-over-sample-tray'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('eyedropper', 'pipette', 'sample', 'tray', 'color', 'liquid', 'tool', 'dropper')

    def build(self) -> None:
        # A diagonal capsule tapers into the open sample tray.
        self.add_bezier('cap',(34,8),((35,7),(36,6),(38,6)),((40,6),(42,8),(42,10)),((42,12),(41,13),(40,14)))
        points=[(40,14),(24,30),(16,32),(18,24),(34,8)]
        for n,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'body-{n}',a,b)
        self.add_contour('dropper','cap',*[f'body-{n}' for n in range(4)],closed=True)
        self.add_line('collar',(24,14),(34,24));self.relate('connect','collar','dropper')
        self.add_polyline('tray',(6,32),(6,42),(38,42),(38,32))
