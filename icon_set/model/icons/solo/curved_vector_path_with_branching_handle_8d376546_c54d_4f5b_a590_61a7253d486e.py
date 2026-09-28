from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d376546-c54d-4f5b-a590-61a7253d486e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors path corner_8d376546-c54d-4f5b-a590-61a7253d486e.svg'
AUTHOR = 'gpt-6'


class CurvedVectorPathWithBranchingHandle(Solo48):
    icon_id = 'curved-vector-path-with-branching-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('vector', 'curve', 'path', 'nodes', 'handles', 'branch', 'editing', 'bezier')

    def build(self) -> None:
        # Circular endpoints, continuous rising path, and a rightward branch.
        for name,x,y in [('lower',10,38),('upper',38,10)]:
            self.add_arc(name+'-a',(x-4,y),(x+4,y),radius_x=4)
            self.add_arc(name+'-b',(x+4,y),(x-4,y),radius_x=4)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        self.add_bezier('path-low',(10,34),((10,30),(18,32),(18,26)))
        self.add_bezier('path-high',(18,26),((18,18),(24,12),(34,10)))
        self.add_contour('path','path-low','path-high')
        self.relate('connect','path','lower');self.relate('connect','path','upper')
        self.add_bezier('branch',(18,26),((26,24),(30,24),(42,24)))
        self.relate('connect','branch','path')
