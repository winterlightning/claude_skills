"""Dropdown Menu with Selected Option; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ce7860f-b6e6-46e5-9b89-a6878b74d16b'
SOURCE_PATH = 'pictographic-primitives/websites/web form drop down menu form_8ce7860f-b6e6-46e5-9b89-a6878b74d16b.svg'
SOURCE_REFERENCES = ({'source_icon_id': '8ce7860f-b6e6-46e5-9b89-a6878b74d16b', 'source_path': 'pictographic-primitives/websites/web form drop down menu form_8ce7860f-b6e6-46e5-9b89-a6878b74d16b.svg'},)
AUTHOR = 'gpt-6'

class DropdownMenuSelectedOption(Solo48):
    icon_id = 'dropdown-menu-selected-option'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    categories = ("websites", "primitives")
    aliases = ()
    keywords = ('dropdown', 'menu', 'selected', 'check', 'form', 'options', 'interface')

    def build(self) -> None:
        # Centerline extremes (6,6)-(42,42), preserving the offset field and selected row.
        self.box('field',6,6,20,18,r=2,joins=((14,18),))
        self.add_polyline('panel',(18,6),(42,6),(42,42),(14,42),(14,18))
        self.relate('connect','field','panel')
        self.add_polyline('selected',(29,17),(31,20),(34,15))
        self.add_line('option',(23,33),(33,33))

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
