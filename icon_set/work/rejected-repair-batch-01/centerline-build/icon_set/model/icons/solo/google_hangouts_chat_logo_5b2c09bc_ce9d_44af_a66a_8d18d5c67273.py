"""A round speech bubble with a short tail at the bottom centre holds an @ symbol.

Plan: Radial bubble with directional tail; inner radius 2 counter and outer radius 11 curl.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: at-sign: circular counter and connected curl; message-circle: bubble.
Simplification: Counter uses the existing 4-unit-diameter circular-hole exception; lower curl shortened for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b2c09bc-ce9d-44af-a66a-8d18d5c67273'
SOURCE_PATH = 'pictographic-primitives/logos/google hangouts chat logo_5b2c09bc-ce9d-44af-a66a-8d18d5c67273.svg'
AUTHOR = 'gpt-6'


class GoogleHangoutsChatLogo(Solo48):
    icon_id = 'google-hangouts-chat-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-chat', 'hangouts', 'google', 'chat', 'at-sign', 'logo', 'brand')

    def build(self):
        # Circular envelope has room for two nested curves; tail occupies lower-right.
        self.add_arc('bubble-top',(4,24),(44,24),radius_x=20)
        self.add_bezier('bubble-right',(44,24),((44,34),(32,40),(24,44)))
        self.add_line('tail',(24,44),(24,40))
        self.add_line('lower-left',(24,40),(12,40))
        self.add_arc('bubble-left',(12,40),(4,24),radius_x=20)
        self.add_contour('bubble','bubble-top','bubble-right','tail','lower-left','bubble-left',closed=True)
        self.add_arc('at-inner-top',(22,24),(26,24),radius_x=2)
        self.add_arc('at-inner-bottom',(26,24),(22,24),radius_x=2)
        self.add_contour('at-inner','at-inner-top','at-inner-bottom',closed=True)
        self.add_bezier('at-return',(26,24),((26,31),(35,31),(35,24)))
        self.add_arc('at-outer',(35,24),(13,24),radius_x=11,sweep=False)
        self.add_bezier('at-end',(13,24),((13,27),(14,30),(15,31)))
        self.add_contour('at-curl','at-return','at-outer','at-end')
        self.relate('connect','at-inner','at-curl')
