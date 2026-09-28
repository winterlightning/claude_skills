"""Revision of person-above-three-circular-nodes. Restored three separated circular hierarchy nodes instead of filled dots, with a clear central person above the branching bar.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""A separate circular head sits above a domed bust connected to a branching line. Three circular nodes hang below it, evenly spaced along the lower horizontal connector.
Symbol plan: Person above a three-node hierarchy. Head radius 4 at (24,8), neck (24,20), exact 4 ink gap. Broad quarter-ellipse shoulders frame the vertical torso. Three compact circular nodes share radius 2 and 14-unit pitch; omit the bust baseline.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: network; human_ref/user.svg; human_ref/full_body_ref.png. Lucide original and atomic-debug renders inspected where named.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '270dd300-e8ad-4129-b17f-dbddcb024c7a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-above-three-circular-nodes/20260927T074149Z-thuan-mac-1/reference/human resources hierarchy_270dd300-e8ad-4129-b17f-dbddcb024c7a.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'person-above-three-circular-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'companies'
    categories = ('primitives', 'companies')
    aliases = ()
    keywords = ('person', 'above', 'three', 'circular', 'nodes')

    def build(self):
        def circle(name,cx,cy,r):
            self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        circle('head',24,10,4)
        self.add_line('torso',(24,22),(24,28))
        self.add_line('branch',(9,28),(39,28))
        self.relate('connect','torso','branch')
        for index,x in enumerate((9,24,39)):
            name=f'node-{index}'
            circle(name,x,39,3)
            self.add_line(name+'-stem',(x,28),(x,36))
            self.relate('connect',name+'-stem',name)
            self.relate('connect',name+'-stem','branch')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
