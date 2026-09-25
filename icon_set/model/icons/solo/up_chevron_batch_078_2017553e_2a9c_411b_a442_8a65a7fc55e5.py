from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2017553e-2a9c-411b-a442-8a65a7fc55e5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/up 4_2017553e-2a9c-411b-a442-8a65a7fc55e5.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/up 4_2017553e-2a9c-411b-a442-8a65a7fc55e5.svg'
# SOLO48 visible extremes (2, 8, 46, 40); centerline extremes (4, 10, 44, 38).
# Construction reference: chevron-up
# Plan: Two nested mirrored angles form the broad outlined chevron with short end walls.

class Batch078Icon(Solo48):
    icon_id = 'up-chevron-batch-078'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('upward', 'pointing', 'chevron')

    def build(self):

        self.add_polyline('chevron',(4,38),(4,26),(24,10),(44,26),(44,38),(24,26),closed=True)


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
