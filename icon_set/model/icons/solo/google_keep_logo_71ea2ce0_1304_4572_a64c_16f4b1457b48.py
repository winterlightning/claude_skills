"""An upright document with a folded top right corner holds a small light bulb with a separate base bar beneath it.

Plan: Folded page with a circular bulb, tapered neck and detached base.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: file-text: folded page; lightbulb: dome and shoulders.
Simplification: Interior fold seam omitted; dog-ear retained in the silhouette; socket reduced to one stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71ea2ce0-1304-4572-a64c-16f4b1457b48'
SOURCE_PATH = 'pictographic-primitives/logos/google keep logo_71ea2ce0-1304-4572-a64c-16f4b1457b48.svg'
AUTHOR = 'gpt-6'


class GoogleKeepLogo(Solo48):
    icon_id = 'google-keep-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-keep', 'google', 'notes', 'lightbulb', 'document', 'logo', 'brand')

    def build(self):
        self.add_polyline('page',(8,44),(8,4),(30,4),(40,14),(40,44),closed=True)
        self.add_arc('bulb-dome',(17,20),(31,20),radius_x=7)
        self.add_bezier('bulb-right',(31,20),((31,24),(27,24),(27,27)))
        self.add_line('bulb-neck',(27,27),(21,27))
        self.add_bezier('bulb-left',(21,27),((21,24),(17,24),(17,20)))
        self.add_contour('bulb','bulb-dome','bulb-right','bulb-neck','bulb-left',closed=True)
        self.add_line('base',(22,35),(26,35))
