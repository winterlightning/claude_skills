"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2ba4638e-ff88-5a77-b904-061a960fe212'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fiber-access/20260925T090056Z-thuan-mac/reference/fiber access_2ba4638e-ff88-5a77-b904-061a960fe212.svg'
AUTHOR = "gpt-6"

def circle(self,name,x,y,r):
    self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
    self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)

def leaf(self,name,a,b,r):
    self.add_arc(name+'-a',a,b,radius_x=r)
    self.add_arc(name+'-b',b,a,radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)

class Revision(Solo48):
    icon_id = 'fiber-access'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'networks'
    exception = {'reason': 'Retain the defining tangent coil connections; internal-spacing advisory describes these intentional connections.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '300c0629e91e25cf5461a8556c1844d34b2930c0a8cfca98c3f1ef62b77e4855'}
    aliases = ()
    keywords = ()

    def build(self):
        for i,y in enumerate((14,34)):
            circle(self,f'coil-{i}',20,y,6)
            self.add_line(f'in-{i}',(4,y-6 if i==0 else y+6),(20,y-6 if i==0 else y+6))
            self.add_line(f'out-{i}',(26,y),(44,y))
            self.add_polyline(f'arrow-{i}',(39,y-5),(44,y),(39,y+5))
            self.relate('connect',f'coil-{i}',f'in-{i}')
            self.relate('connect',f'coil-{i}',f'out-{i}')
            self.relate('connect',f'out-{i}',f'arrow-{i}')
