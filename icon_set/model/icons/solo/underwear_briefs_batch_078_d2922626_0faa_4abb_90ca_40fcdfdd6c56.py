from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2922626-0faa-4abb-90ca-40fcdfdd6c56'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/underclothes_d2922626-0faa-4abb-90ca-40fcdfdd6c56.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/underclothes_d2922626-0faa-4abb-90ca-40fcdfdd6c56.svg'
# SOLO48 visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
# Construction reference: No useful local Lucide subject match
# Plan: Symmetric waistband and inward curving leg openings. Shared waist and crotch nodes.

class Batch078Icon(Solo48):
    icon_id = 'underwear-briefs-batch-078'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('underwear', 'briefs')

    def build(self):

        self.add_polyline('waist',(4,16),(4,8),(44,8),(44,16))
        self.add_line('band',(4,16),(44,16))
        self.add_arc('leg-right',(44,16),(30,40),radius_x=14,radius_y=24,sweep=False)
        self.add_line('crotch',(30,40),(18,40))
        self.add_arc('leg-left',(18,40),(4,16),radius_x=14,radius_y=24,sweep=False)
        self.add_contour('lower','leg-right','crotch','leg-left')
        self.relate('connect','waist','band')
        self.relate('connect','waist','lower')
        self.relate('connect','band','lower')


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
