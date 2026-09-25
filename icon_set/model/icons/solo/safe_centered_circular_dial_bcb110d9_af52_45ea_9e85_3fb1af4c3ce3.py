"""Secure Bank Safe Vault.
Plan: Rounded safe cabinet on short feet with centered circular dial. Extrema (6,6)-(42,42).
Reference: Lucide vault: rounded cabinet and prominent centered lock mechanism.
Reduction: Inset door border and tiny central hub omitted; prominent circular dial retains vault identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcb110d9-af52-45ea-9e85-3fb1af4c3ce3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/saving safe_bcb110d9-af52-45ea-9e85-3fb1af4c3ce3.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'safe-centered-circular-dial'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ()
    keywords = ('secure', 'bank', 'safe', 'vault')

    def build(self):

        self.add_line('cabinet-top',(10,6),(38,6))
        self.add_arc('cabinet-tr',(38,6),(42,10),radius_x=4)
        self.add_line('cabinet-right',(42,10),(42,34))
        self.add_arc('cabinet-br',(42,34),(38,38),radius_x=4)
        self.add_line('cabinet-base',(38,38),(10,38))
        self.add_arc('cabinet-bl',(10,38),(6,34),radius_x=4)
        self.add_line('cabinet-left',(6,34),(6,10))
        self.add_arc('cabinet-tl',(6,10),(10,6),radius_x=4)
        self.add_contour('cabinet',*[f'cabinet-{s}' for s in ('top','tr','right','br','base','bl','left','tl')],closed=True)

        self.add_arc('dial-a',(24,15),(24,29),radius_x=7)
        self.add_arc('dial-b',(24,29),(24,15),radius_x=7)
        self.add_contour('dial','dial-a','dial-b',closed=True)

        for i,x in enumerate((10,38)):
            self.add_line(f'foot-{i}',(x,38),(x,42));self.relate('connect','cabinet',f'foot-{i}')
