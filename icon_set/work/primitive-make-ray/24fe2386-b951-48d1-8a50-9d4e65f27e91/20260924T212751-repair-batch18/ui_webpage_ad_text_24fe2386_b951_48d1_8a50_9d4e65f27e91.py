"""A browser page displaying uppercase AD.
Symbol plan and construction: app-window: a header strip with shared side-wall joins; supplied source owns the letters.
Keyshape: SQUARE balances the full browser and two letters after wider and taller trials.
Omissions: Small header dashes removed; A rounded; AD and full frame retained.
Review: Blocked: letters remain too close to the browser side walls and A/D curved-pair clearance requires review. Six candidates saved; no visual approval."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='24fe2386-b951-48d1-8a50-9d4e65f27e91'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage ad text_24fe2386-b951-48d1-8a50-9d4e65f27e91.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='ui-webpage-ad-text'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('ui', 'webpage', 'ad', 'text')






    def build(self):
        self.add_polyline('browser',(6,14),(6,6),(42,6),(42,14),(42,42),(6,42),closed=True)
        self.add_line('chrome',(6,14),(42,14));self.relate('connect','browser','chrome')
        self.add_polyline('a-left',(12,32),(12,30),(12,24))
        self.add_arc('a-cap',(12,24),(20,24),radius_x=4)
        self.add_polyline('a-right',(20,24),(20,30),(20,32))
        self.add_line('a-bar',(12,30),(20,30))
        for n in ['a-left','a-right']:
            self.relate('connect',n,'a-cap');self.relate('connect',n,'a-bar')
        self.add_line('d-stem',(28,20),(28,32))
        self.add_arc('d-bowl',(28,20),(28,32),radius_x=8,radius_y=6)
        self.relate('connect','d-stem','d-bowl')
