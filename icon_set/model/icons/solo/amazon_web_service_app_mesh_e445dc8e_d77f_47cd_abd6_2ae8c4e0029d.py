"""amazon-web-service-app-mesh: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e445dc8e-d77f-47cd-abd6-2ae8c4e0029d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service app mesh_e445dc8e-d77f-47cd-abd6-2ae8c4e0029d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AmazonWebServiceAppMesh(Solo48):
    icon_id = 'amazon-web-service-app-mesh'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'app', 'mesh', '_uncategorized_02')

    def build(self):
        # Plan: SQUARE; symmetric links terminate on node circles; remove the tiny top-link arc.
        # Reference: Geometric node circles and shared contacts; no exact Lucide brand match.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        circle('hub',24,27,5)
        for name,cx,cy in [('top',24,9),('left',9,39),('right',39,39)]:circle(name,cx,cy,3)
        self.add_line('top-link',(24,12),(24,22))
        # Integer 3-4-5 contact points on the hub; smooth curves land on outer-node apices.
        self.add_bezier('left-link',(20,30),((16,33),(12,34),(9,36)))
        self.add_bezier('right-link',(28,30),((32,33),(36,34),(39,36)))
        for name in ['top','left','right']:
            self.relate('connect',name+'-link',name)
            self.relate('connect',name+'-link','hub')
