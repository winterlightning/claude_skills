from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82863c23-af6c-45c9-84a6-d427521a1cf2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/perspective grid_82863c23-af6c-45c9-84a6-d427521a1cf2.svg'
AUTHOR = 'gpt-6'


class PerspectiveGridWithCurvedSideLines(Solo48):
    icon_id = 'perspective-grid-with-curved-side-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('grid', 'perspective', 'mesh', 'warp', 'curve', 'distortion', 'design', 'geometry')

    def build(self) -> None:
        # Mirror the curved side meridians around x=24; repeat horizontal divisions.
        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        for y in (18,30):
            self.add_line(f'row-{y}',(6,y),(42,y));self.relate('connect',f'row-{y}','frame')
        self.add_line('center',(24,6),(24,42))
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier(side,(24+sign*10,6),((24+sign*8,18),(24+sign*8,30),(24+sign*10,42)))
        for name in ('left','center','right'):
            self.relate('connect',name,'frame')
            for y in (18,30):self.relate('connect',name,f'row-{y}')
