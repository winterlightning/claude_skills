"""World Globe Planet Symbol — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8bd55324-ebc3-4c07-87e6-347f46d0dae7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/globe_8bd55324-ebc3-4c07-87e6-347f46d0dae7.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'world-globe-planet-symbol-batch-033'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('world-globe-planet-symbol',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Circular globe with equator and oval meridian; shared poles and equatorial nodes; radius20.

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x0,y0,x1,y1,r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8];eid=f'{name}-{i}';ids.append(eid)
                if i%2:self.add_arc(eid,p,q,radius_x=r)
                else:self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        pts=[(24,4),(44,24),(24,44),(4,24)]
        for i,p in enumerate(pts):self.add_arc(f'outer-{i}',p,pts[(i+1)%4],radius_x=20)
        self.add_contour('outline',*[f'outer-{i}' for i in range(4)],closed=True)
        pts2=[(24,4),(34,24),(24,44),(14,24)]
        for i,p in enumerate(pts2):self.add_arc(f'meridian-{i}',p,pts2[(i+1)%4],radius_x=10,radius_y=20)
        self.add_contour('meridian',*[f'meridian-{i}' for i in range(4)],closed=True)
        self.add_polyline('equator',(4,24),(14,24),(34,24),(44,24))
        self.relate('connect','outline','meridian');self.relate('connect','outline','equator');self.relate('connect','meridian','equator')
