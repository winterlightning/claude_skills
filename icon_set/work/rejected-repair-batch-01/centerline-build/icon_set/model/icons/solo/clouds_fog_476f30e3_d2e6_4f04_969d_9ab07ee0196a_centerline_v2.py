"""Replace the flattened rear cloud with a fuller crown and remove its redundant zero-length return; use two balanced fog strokes instead of one long heavy underline.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '476f30e3-d2e6-4f04-969d-9ab07ee0196a'
SOURCE_PATH = 'pictographic-primitives/weather/cloud mist_476f30e3-d2e6-4f04-969d-9ab07ee0196a.svg'
AUTHOR = 'gpt-6'

class CloudsFog(Solo48):
    icon_id = 'clouds-fog-centerline-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('cloud', 'fog', 'mist', 'overcast', 'weather', 'atmosphere')

    def build(self) -> None:
        self.add_arc('front-left', (12, 28), (12, 18), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('front-crown-left', (12, 18), (20, 12), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('front-crown-right', (20, 12), (28, 18), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('front-right', (28, 18), (28, 28), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('front-base', (28, 28), (12, 28))
        self.add_contour('front', 'front-left', 'front-crown-left', 'front-crown-right', 'front-right', 'front-base', closed=True)
        self.add_arc('back-top', (20, 12), (36, 12), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('back-side', (36, 12), (36, 24), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_line('back-return', (36, 24), (36, 24))
        self.add_contour('back', 'back-top', 'back-side', 'back-return', closed=False)
        self.add_line('mist-left', (6, 40), (20, 40))
        self.add_line('mist-right', (28, 40), (42, 40))
        self.relate('connect', 'front', 'back')
    variant_of = 'clouds-fog'
    variant_label = 'Batch 01 centerline repair'
