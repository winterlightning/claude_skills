"""Four diagonal windmill sails and tapered tower. VRECT_L extremes 8,4..40,44.
Rotor mirrors around (24,20); tower attaches at shared lower sail nodes.
Reduce broad sail panels to bold runs and omit tiny doorway to keep openings clear.
Source supplies diagonal rotor and taper; no exact useful Lucide match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='cc0660fc-686e-4d61-aef0-365ed9fa2270'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/mill_cc0660fc-686e-4d61-aef0-365ed9fa2270.svg'
AUTHOR='gpt-6-astra'
class Drawing(Solo48):
    icon_id='four-sail-windmill'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='architecture'
    aliases=('farm windmill',)
    keywords=('windmill','mill','sails','building','farm','wind')
    def build(self):
        hub=(24,20)
        for side,x in [('left',8),('right',40)]:
            self.add_line(f'upper-{side}',hub,(x,4))
            attach=((24+x)//2,28)
            self.add_line(f'lower-inner-{side}',hub,attach)
            self.add_line(f'lower-outer-{side}',attach,(x,36))
            self.relate('connect',f'lower-inner-{side}',f'lower-outer-{side}')
        self.add_polyline('tower',(16,28),(12,44),(36,44),(32,28))
        for side in ('left','right'):
            self.relate('connect','tower',f'lower-inner-{side}',f'lower-outer-{side}')
        names=['upper-left','upper-right','lower-inner-left','lower-inner-right']
        for i,a in enumerate(names):
            for b in names[i+1:]:self.relate('connect',a,b)
