"""World Globe Symbol — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9745aa8-65c0-43a9-b672-82f9308c27af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/globe 1_f9745aa8-65c0-43a9-b672-82f9308c27af.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'world-globe-symbol-batch-033'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('world-globe-symbol',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Globe with blank center latitude band and one simplified meridian per pole; shared symmetric nodes; radius20.

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

        pts=[(24,4),(40,12),(44,24),(40,36),(24,44),(8,36),(4,24),(8,12)]
        for i,p in enumerate(pts):self.add_arc(f'outer-{i}',p,pts[(i+1)%8],radius_x=20)
        self.add_contour('outline',*[f'outer-{i}' for i in range(8)],closed=True)
        for j,y in enumerate((12,36)):
            self.add_polyline(f'latitude-{j}',(8,y),(24,y),(40,y))
            self.relate('connect','outline',f'latitude-{j}')
        # A single central polar meridian replaces the four crowded wedges.
        # Retain the broad empty equatorial band and true shared polar nodes.
        for name,start,end,latitude in [('north',(24,4),(24,12),'latitude-0'),('south',(24,36),(24,44),'latitude-1')]:
            self.add_line(name,start,end)
            self.relate('connect','outline',name)
            self.relate('connect',latitude,name)
