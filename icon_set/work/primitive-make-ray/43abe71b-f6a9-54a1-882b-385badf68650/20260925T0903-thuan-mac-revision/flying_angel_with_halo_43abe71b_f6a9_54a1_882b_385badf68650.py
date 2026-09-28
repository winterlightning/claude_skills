"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '43abe71b-f6a9-54a1-882b-385badf68650'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flying-angel-with-halo/20260925T090056Z-thuan-mac/reference/angel_43abe71b-f6a9-54a1-882b-385badf68650.svg'
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
    icon_id = 'flying-angel-with-halo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    exception = {'reason': 'Preserve reference-attached head/robe and wing junctions, asymmetric flight pose and open halo; this is not a detached stick figure.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': 'bb474848e919a07385a17cfd5f4b7c20fa1e3d0b04f915bb3a61dab83cfdc8a4'}
    aliases = ()
    keywords = ()

    def build(self):
        # Airborne asymmetric robe and wing preserve the original diagonal gesture.
        circle(self,'head',33,21,5)
        self.add_arc('halo-a',(23,6),(43,6),radius_x=10,radius_y=4)
        self.add_arc('halo-b',(43,6),(23,6),radius_x=10,radius_y=4)
        self.add_contour('halo','halo-a','halo-b',closed=True)
        self.add_arc('wing-upper',(4,10),(25,29),radius_x=43,sweep=False)
        self.add_arc('wing-bottom',(25,29),(4,10),radius_x=22)
        self.add_contour('wing','wing-upper','wing-bottom',closed=True)
        self.add_arc('robe-upper',(8,32),(30,28),radius_x=45,sweep=False)
        self.add_arc('robe-right',(30,28),(30,44),radius_x=35)
        self.add_arc('robe-bottom',(30,44),(8,32),radius_x=27)
        self.add_contour('robe','robe-upper','robe-right','robe-bottom',closed=True)
