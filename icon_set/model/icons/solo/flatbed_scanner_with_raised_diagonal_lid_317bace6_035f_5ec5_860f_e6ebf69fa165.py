"""Flatbed Scanner With Open Lid.

Symbol plan: Low scanner body, two short feet and hinged rising lid. Single-stroke lid replaces narrow double outline. Lucide printer informs rounded machine body; deliberate lid asymmetry.
Keyshape HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '317bace6-035f-5ec5-860f-e6ebf69fa165'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/scanner_317bace6-035f-5ec5-860f-e6ebf69fa165.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'flatbed-scanner-with-raised-diagonal-lid'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('flatbed', 'scanner', 'with', 'open', 'lid')

    def build(self):
        self.run('top',(8,28),(40,28))
        self.add_arc('right',(40,28),(40,36),radius_x=4)
        self.run('bottom',(40,36),(36,36),(12,36),(8,36))
        self.add_arc('left',(8,36),(8,28),radius_x=4)
        self.add_contour('body','top-1','right','bottom-1','bottom-2','bottom-3','left',closed=True)
        self.add_line('lid',(8,28),(40,8));self.relate('connect','lid','body')
        for i,x in enumerate((12,36)):
            self.add_line(f'foot-{i}',(x,36),(x,40));self.relate('connect',f'foot-{i}','body')

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f"{name}-{i}",a,b)
