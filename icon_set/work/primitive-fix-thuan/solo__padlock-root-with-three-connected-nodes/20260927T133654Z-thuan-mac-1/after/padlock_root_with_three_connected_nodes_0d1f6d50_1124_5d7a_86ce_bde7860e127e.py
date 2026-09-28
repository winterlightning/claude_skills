"""Secure Hierarchy Diagram.

Plan: Lock root and three repeated round nodes; bounds (8,4)-(40,44). A horizontal branch rail separates the hierarchy from the lock.
Construction reference: Lucide network: repeated nodes and orthogonal branch; rounded shackle.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0d1f6d50-1124-5d7a-86ce-bde7860e127e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__padlock-root-with-three-connected-nodes/20260927T133654Z-thuan-mac-1/reference/lock hierarchy_0d1f6d50-1124-5d7a-86ce-bde7860e127e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'padlock-root-with-three-connected-nodes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('secure', 'hierarchy', 'diagram')

    def build(self):
        # Keep the lock above its three descendants. One orthogonal root and
        # one branch rail make the hierarchy visible without crossing the lock.
        path(self,'shackle',(20,16),('L',(20,8)),('A',4,4,True,(28,8)),('L',(28,16)))
        box(self,'lock',16,16,32,24,2,xs=(24,))
        line(self,'root',(24,24),(24,32))
        poly(self,'rail',(10,32),(24,32),(38,32))
        for i,x in enumerate((10,24,38)):
         line(self,f'branch-{i}',(x,32),(x,40))
         self.add_arc(f'node-{i}-right',(x,40),(x,44),radius_x=2)
         self.add_arc(f'node-{i}-left',(x,44),(x,40),radius_x=2)
         self.add_contour(f'node-{i}',f'node-{i}-right',f'node-{i}-left',closed=True)
        contacts(self)
