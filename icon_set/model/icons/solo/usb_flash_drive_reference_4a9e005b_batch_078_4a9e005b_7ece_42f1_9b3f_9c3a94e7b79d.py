from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a9e005b-7ece-42f1-9b3f-9c3a94e7b79d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/usb drive_4a9e005b-7ece-42f1-9b3f-9c3a94e7b79d.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/usb drive_4a9e005b-7ece-42f1-9b3f-9c3a94e7b79d.svg'
# SOLO48 visible extremes (8, 2, 40, 46); centerline extremes (10, 4, 38, 44).
# Construction reference: No useful local Lucide subject match
# Plan: Upright USB flash drive retains both connector contacts. Small upper corner radii and broad bottom arcs distinguish the body from the connector.

class Batch078Icon(Solo48):
    icon_id = 'usb-flash-drive-reference-4a9e005b-batch-078'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('usb', 'flash', 'drive')

    def build(self):
        self.add_line('top',(12,22),(36,22))
        self.add_arc('top-right',(36,22),(38,24),radius_x=2)
        self.add_line('right',(38,24),(38,36))
        self.add_arc('bottom-right',(38,36),(30,44),radius_x=8)
        self.add_line('bottom',(30,44),(18,44))
        self.add_arc('bottom-left',(18,44),(10,36),radius_x=8)
        self.add_line('left',(10,36),(10,24))
        self.add_arc('top-left',(10,24),(12,22),radius_x=2)
        self.add_contour('body','top','top-right','right','bottom-right','bottom','bottom-left','left','top-left',closed=True)
        self.add_polyline('connector',(12,22),(12,4),(36,4),(36,22))
        self.relate('connect','connector','body')
        for i,x in enumerate((20,28)):
            self.add_line(f'contact-{i}',(x,12),(x,14))

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rect(self, name, l, t, r, b, radius=4):
        k=radius
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        for j in range(8):
            a,z=pts[j],pts[(j+1)%8]
            if j%2: self.add_arc(name+str(j),a,z,radius_x=k)
            else: self.add_line(name+str(j),a,z)
        self.add_contour(name,*(name+str(j) for j in range(8)),closed=True)
