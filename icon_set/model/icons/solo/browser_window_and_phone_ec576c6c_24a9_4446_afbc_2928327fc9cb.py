"""Browser Window and Phone. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec576c6c-24a9-4446-afbc-2928327fc9cb'
SOURCE_PATH = 'pictographic-primitives/websites/responsive design image_ec576c6c-24a9-4446-afbc-2928327fc9cb.svg'
AUTHOR = 'gpt-6'

class BrowserWindowAndPhone(Solo48):
    icon_id = 'browser-window-and-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ()
    keywords = ('responsive', 'browser', 'phone', 'devices', 'window', 'mobile', 'web')

    def build(self):
        self.box('phone',30,6,42,28,r=2)
        self.add_polyline('window',(21,14),(9,14),(6,17),(6,39),(9,42),(37,42),(40,39),(40,37))
        self.add_line('toolbar',(6,23),(21,23))
        self.relate('connect','toolbar','window')

    def box(self, name, x0, y0, x1, y1, r=3):
        # One rounded rectangle definition; all corners share a radius.
        points = [(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),
                  (x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; part=f'{name}-{i}';members.append(part)
            if i%2: self.add_arc(part,p,q,radius_x=r)
            else: self.add_line(part,p,q)
        self.add_contour(name,*members,closed=True)
