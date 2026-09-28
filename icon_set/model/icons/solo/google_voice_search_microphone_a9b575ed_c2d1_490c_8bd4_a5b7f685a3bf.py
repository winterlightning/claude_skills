"""An upright capsule microphone sits in a U-shaped cradle that curves beneath it, with a short stand dropping to the bottom.

Plan: Capsule radius 7 inside U-cradle radius 16; stand shares its bottom node.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: mic: capsule, U-cradle, shared stand attachment.
Simplification: Outlined stand becomes a single stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9b575ed-c2d1-490c-8bd4-a5b7f685a3bf'
SOURCE_PATH = 'pictographic-primitives/logos/google microphone voice search logo_a9b575ed-c2d1-490c-8bd4-a5b7f685a3bf.svg'
AUTHOR = 'gpt-6'


class GoogleVoiceSearchMicrophone(Solo48):
    icon_id = 'google-voice-search-microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('microphone', 'voice-search', 'google', 'mic', 'logo', 'brand', 'speech')

    def build(self):
        self.add_arc('cap-top',(17,11),(31,11),radius_x=7)
        self.add_line('cap-right',(31,11),(31,19))
        self.add_arc('cap-bottom',(31,19),(17,19),radius_x=7)
        self.add_line('cap-left',(17,19),(17,11))
        self.add_contour('capsule','cap-top','cap-right','cap-bottom','cap-left',closed=True)
        self.add_arc('cradle-a',(40,20),(24,36),radius_x=16)
        self.add_arc('cradle-b',(24,36),(8,20),radius_x=16)
        self.add_contour('cradle','cradle-a','cradle-b')
        self.add_line('stand',(24,36),(24,44))
        self.relate('connect','cradle','stand')
