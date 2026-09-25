"""Selection Field with Check; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37b8513e-3457-5655-923a-d4831e8257af'
SOURCE_PATH = 'pictographic-primitives/websites/web form drop down menu_37b8513e-3457-5655-923a-d4831e8257af.svg'
SOURCE_REFERENCES = ({'source_icon_id': '37b8513e-3457-5655-923a-d4831e8257af', 'source_path': 'pictographic-primitives/websites/web form drop down menu_37b8513e-3457-5655-923a-d4831e8257af.svg'},)
AUTHOR = 'gpt-6'

class SelectionFieldWithCheck(Solo48):
    icon_id = 'selection-field-with-check'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    aliases = ()
    keywords = ('field', 'form', 'selection', 'check', 'input', 'interface', 'control')

    def build(self) -> None:
        # Centerline extremes (6,8)-(42,40); the check compartment is widened for legibility.
        self.box('field',4,8,44,40,r=3,joins=((20,8),(20,40)))
        self.add_line('divider',(20,8),(20,40))
        self.relate('connect','divider','field')
        self.add_polyline('check',(29,24),(32,27),(35,21))

    def box(self, name, x0, y0, x1, y1, r=2, joins=()):
        # A shared corner radius and explicit attachment nodes own this rectangle.
        points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),
                (x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]
            if i%2:
                name_i=f'{name}-{i}';self.add_arc(name_i,p,q,radius_x=r);members.append(name_i)
            else:
                mid=[v for v in joins if v!=p and v!=q and
                     ((p[0]==q[0]==v[0] and min(p[1],q[1])<v[1]<max(p[1],q[1])) or
                      (p[1]==q[1]==v[1] and min(p[0],q[0])<v[0]<max(p[0],q[0])))]
                run=[p]+sorted(mid,key=lambda v:(v[0]-p[0])**2+(v[1]-p[1])**2)+[q]
                for j,(a,b) in enumerate(zip(run,run[1:])):
                    name_i=f'{name}-{i}-{j}';self.add_line(name_i,a,b);members.append(name_i)
        self.add_contour(name,*members,closed=True)
