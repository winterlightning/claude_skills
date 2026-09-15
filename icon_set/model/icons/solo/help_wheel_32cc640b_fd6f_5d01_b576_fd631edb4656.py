"""help-wheel: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32cc640b-fd6f-5d01-b576-fd631edb4656'
SOURCE_PATH = 'pictographic-primitives/interface-essential/help wheel_32cc640b-fd6f-5d01-b576-fd631edb4656.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class HelpWheel(Solo48):
    icon_id = 'help-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('help', 'wheel', 'interface-essential')

    def build(self):
        # Plan: CIRCLE; concentric rings and four reflected bridges ending exactly on both circles.
        # Reference: Geometric circles and exact radial contacts.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        circle('outer',24,24,20)
        circle('inner',24,24,10)
        for i,(sx,sy) in enumerate([(-1,-1),(1,-1),(1,1),(-1,1)]):
            self.add_line(f'bridge-{i}',(24+sx*6,24+sy*8),(24+sx*12,24+sy*16))
            self.relate('connect',f'bridge-{i}','outer')
            self.relate('connect',f'bridge-{i}','inner')
