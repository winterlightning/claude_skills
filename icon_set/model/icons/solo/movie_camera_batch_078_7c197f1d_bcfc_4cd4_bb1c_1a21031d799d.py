from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c197f1d-bcfc-4cd4-bb1c-1a21031d799d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/viddler logo_7c197f1d-bcfc-4cd4-bb1c-1a21031d799d.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/viddler logo_7c197f1d-bcfc-4cd4-bb1c-1a21031d799d.svg'
# SOLO48 visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
# Construction reference: video
# Plan: Two separate reel circles and left-facing flared lens identify a movie camera. Hubs omitted for clear reel openings; deliberate left-facing asymmetry.

class Batch078Icon(Solo48):
    icon_id = 'movie-camera-batch-078'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('vintage', 'movie', 'camera')

    def build(self):

        for i,x in enumerate((16,36)):
            self.circle(f'reel-{i}',x,12,6)
        self.add_polyline('body',(16,26),(42,26),(42,42),(16,42),(16,38),(6,42),(6,26),(16,30),(16,26))


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
