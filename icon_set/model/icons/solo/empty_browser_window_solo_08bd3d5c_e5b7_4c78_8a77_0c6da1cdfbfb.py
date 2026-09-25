"""Empty Browser Window; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08bd3d5c-e5b7-4c78-8a77-0c6da1cdfbfb'
SOURCE_PATH = 'pictographic-primitives/websites/ui webpage template_08bd3d5c-e5b7-4c78-8a77-0c6da1cdfbfb.svg'
SOURCE_REFERENCES = ({'source_icon_id': '08bd3d5c-e5b7-4c78-8a77-0c6da1cdfbfb', 'source_path': 'pictographic-primitives/websites/ui webpage template_08bd3d5c-e5b7-4c78-8a77-0c6da1cdfbfb.svg'}, {'source_icon_id': '8ee52bbe-ce7b-51d9-b180-b2b8c8d6a3b4', 'source_path': 'pictographic-primitives/websites/ui webpage template_8ee52bbe-ce7b-51d9-b180-b2b8c8d6a3b4.svg'}, {'source_icon_id': 'e0be1f74-3a16-4069-8206-6eaf00242275', 'source_path': 'pictographic-primitives/websites/ui webpage template_e0be1f74-3a16-4069-8206-6eaf00242275.svg'})
AUTHOR = 'gpt-6'

class EmptyBrowserWindowSolo(Solo48):
    icon_id = 'empty-browser-window-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    aliases = ()
    keywords = ('browser', 'window', 'empty', 'template', 'website', 'toolbar', 'interface')

    def build(self) -> None:
        # Centerline extremes (6,6)-(42,42). Header controls share a 9-unit step.
        self.box('browser',6,6,42,42,r=3,joins=((6,24),(42,24)))
        self.add_line('toolbar',(6,24),(42,24))
        self.relate('connect','toolbar','browser')
        for n in range(3): self.add_dot(f'control-{n}',(15+9*n,15))

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
