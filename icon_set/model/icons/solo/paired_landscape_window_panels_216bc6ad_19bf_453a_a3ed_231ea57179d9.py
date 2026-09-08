from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '216bc6ad-19bf-453a-a3ed-231ea57179d9'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-05/windows_216bc6ad-19bf-453a-a3ed-231ea57179d9.svg'
AUTHOR = "gpt-6"


class PairedLandscapeWindowPanels(Solo48):
    icon_id = 'paired-landscape-window-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('paired', 'landscape', 'window', 'panels')

    def build(self):
        # Centerline extremes: (2, 2) to (46, 46).
        for name,l,r in [("left",2,20),("right",28,46)]:
            self.add_polyline(name+"-frame", (l,32), (l,2), (r,2), (r,25), (r,46), (l,46), (l,32))
            self.add_arc(name+"-hill", (l,32), (r,25), radius_x=24, sweep=True)
            self.relate("connect", name+"-hill", name+"-frame")
            self.add_line(name+"-cloud-base", (l,18), (l+6,18))
            self.add_arc(name+"-cloud-dome", (l+6,18), (r,18), radius_x=6)
            self.add_contour(name+"-cloud", name+"-cloud-base", name+"-cloud-dome")
            self.relate("connect", name+"-cloud", name+"-frame")
