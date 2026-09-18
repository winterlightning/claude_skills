from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1111a7d-0e17-480b-bd48-42a1ccc6d651'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/users_b1111a7d-0e17-480b-bd48-42a1ccc6d651.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/users_b1111a7d-0e17-480b-bd48-42a1ccc6d651.svg'
# SOLO48 visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
# Construction reference: users
# Plan: Two detached user busts use human_ref/user.svg. Head radius 4, center y10; lowest head centerline y14, shoulder top y22: exactly 8 centerline / 4 ink gap. Shoulder width 14 preserves broad bust proportions. Side-by-side arrangement replaces overlap.

class Batch078Icon(Solo48):
    icon_id = 'two-person-group-batch-078'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('two', 'people', 'user', 'group')

    def build(self):

        for i,x in enumerate((13,35)):
            n=f'person-{i}'
            self.circle(n+'-head',x,10,4)
            self.add_line(n+'-side-l',(x-7,42),(x-7,29))
            self.add_arc(n+'-shoulder-l',(x-7,29),(x,22),radius_x=7)
            self.add_arc(n+'-shoulder-r',(x,22),(x+7,29),radius_x=7)
            self.add_line(n+'-side-r',(x+7,29),(x+7,42))
            self.add_contour(n+'-body',n+'-side-l',n+'-shoulder-l',n+'-shoulder-r',n+'-side-r')


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
