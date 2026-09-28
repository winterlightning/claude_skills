"""Revision of the claimed reference after comparing original and rejected drawing."""
"""Circular network extent with three internal nodes and triangular links. Nodes reduced to round junction marks to keep open triangular face. Radius20 about24,24.
Lucide construction reference: network.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3b2a855e-6ab2-51bc-8612-b388126ed3ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__global-network-nodes-solo-b017/20260927T142529Z-thuan-mac-1/reference/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/networks/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
AUTHOR = "gpt-6"
class BatchIcon(Solo48):
    icon_id='global-network-nodes-solo-b017'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "networks"
    categories = ("primitives", "networks")
    aliases=()
    keywords=('global', 'network', 'nodes')
    def build(self):
        # Three open node circles and clear connecting links follow the source.
        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r)); members=[]
            for i in range(4):
                m=n+str(i); self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r); members.append(m)
            self.add_contour(n,*members,closed=True)
        circle('extent',24,24,20)
        circle('node-left',16,24,3)
        circle('node-top',28,16,3)
        circle('node-bottom',28,30,3)
        self.add_line('link-upper',(19,24),(25,16))
        self.add_line('link-lower',(19,24),(25,30))
        self.add_line('link-right',(28,19),(28,27))
        for a,b,c in (('link-upper','node-left','node-top'),('link-lower','node-left','node-bottom'),('link-right','node-top','node-bottom')):
            self.relate('connect',a,b); self.relate('connect',a,c)
