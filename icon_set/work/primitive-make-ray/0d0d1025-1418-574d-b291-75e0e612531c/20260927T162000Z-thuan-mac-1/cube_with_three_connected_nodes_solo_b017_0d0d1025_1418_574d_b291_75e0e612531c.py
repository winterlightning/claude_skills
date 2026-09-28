"""Isometric cube with three round terminal nodes attached above and at lower corners. Centerline6,6–42,42.
Lucide construction reference: box; network.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0d0d1025-1418-574d-b291-75e0e612531c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cube-with-three-connected-nodes-solo-b017/20260927T160114Z-thuan-mac-1/reference/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
AUTHOR="gpt-6"
class BatchIcon(Solo48):
    icon_id='cube-with-three-connected-nodes-solo-b017'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=('cube', 'with', 'three', 'connected', 'nodes')
    def build(self):
        # The three terminal rings surround one legible three-face isometric cube.
        def ring(name,x,y,r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        self.add_polyline('cube',(16,20),(24,16),(32,20),(32,29),(24,34),(16,29),closed=True)
        self.add_polyline('faces',(16,20),(24,25),(32,20))
        self.add_line('edge',(24,25),(24,34))
        self.relate('connect','cube','faces')
        self.relate('connect','cube','edge')
        self.relate('connect','faces','edge')
        ring('top',24,12,4)
        ring('left',8,36,4)
        ring('right',40,36,4)
        for name,a,b in [('top',(24,16),(24,16)),('left',(16,29),(12,36)),('right',(32,29),(36,36))]:
            if a!=b:
                self.add_line(name+'-link',a,b)
                self.relate('connect',name+'-link','cube')
                self.relate('connect',name+'-link',name)
            else:
                self.relate('connect','cube',name)
