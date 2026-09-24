"""A browser page displaying a short-sleeved shirt.
Symbol plan and construction: app-window and shirt: shared browser header nodes, matched shoulders, sleeves and body.
Keyshape: VRECT_L gives the garment more vertical room; a flatter passing candidate was visually rejected.
Omissions: Tiny header dashes and scooped neckline removed; shoulder slopes, sleeves and body retained.
Review: Approved: upright garment proportions and equal sleeve steps read at native size in both themes. The neck detail is deliberately omitted rather than squeezed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='6fd53a7d-aab1-479b-9e12-e2f8acddcfb2'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage t shirt_6fd53a7d-aab1-479b-9e12-e2f8acddcfb2.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='ui-webpage-t-shirt'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('ui', 'webpage', 't', 'shirt')






    def build(self):
        self.add_polyline('browser',(8,12),(8,4),(40,4),(40,12),(40,44),(8,44),closed=True)
        self.add_line('chrome',(8,12),(40,12));self.relate('connect','browser','chrome')
        self.add_polyline('shirt',(21,21),(27,21),(31,25),(31,29),(28,29),(28,35),(20,35),(20,29),(17,29),(17,25),closed=True)
