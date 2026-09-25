'A concentric ring supports an upright cross on its crown. Unified astrology symbol, not a modifier badge. VRECT_M fits outer radius14 centered at(24,30) and cross reaching y4. Lucide circle-plus supplies cardinal arc construction. Shared x24 axis, two closed rings and explicitly split cross junction; reference ring thickness normalized to stroke4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '37f2e936-d45d-4082-8529-a8e9d9f944d5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/astrology earth_37f2e936-d45d-4082-8529-a8e9d9f944d5.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'ring-topped-by-a-cross'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Earth Astrology Symbol']
    keywords = ['ring', 'cross', 'astrology', 'circle', 'symbol', 'celestial', 'axis']
    def build(self):
        for name,r in [('outer',14),('inner',4)]:
            self.add_arc(name+'-a',(24,30-r),(24,30+r),radius_x=r)
            self.add_arc(name+'-b',(24,30+r),(24,30-r),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        self.add_line('cross-top',(24,4),(24,8))
        self.add_line('cross-stem',(24,8),(24,16))
        self.add_line('cross-left',(14,8),(24,8))
        self.add_line('cross-right',(24,8),(34,8))
        self.relate('connect','cross-top','cross-stem','cross-left','cross-right')
        self.relate('connect','cross-stem','outer')
