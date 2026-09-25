"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c810b3a0-ffc4-4002-871a-76f3db70b5fa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__foam-and-floating-bubbles/20260925T090056Z-thuan-mac/reference/foam_c810b3a0-ffc4-4002-871a-76f3db70b5fa.svg'
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
    icon_id = 'foam-and-floating-bubbles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve unequal floating bubbles and foam silhouette; compact bubble gaps remain visibly separated in both themes.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': 'e20a29e5082624342e83b9f0debd54fca9f0992a2b4f49af9443c0de79cc735f'}
    aliases = ()
    keywords = ()

    def build(self):
        circle(self,'bubble-large',16,14,7)
        circle(self,'bubble-small',32,6,4)
        self.add_line('base',(4,42),(35,42))
        self.add_arc('right',(35,42),(40,28),radius_x=10,sweep=False)
        self.add_arc('top-bubble',(40,28),(30,28),radius_x=6,large_arc=True,sweep=False)
        self.add_arc('middle',(30,28),(15,35),radius_x=9,sweep=False)
        self.add_arc('left',(15,35),(4,42),radius_x=10,sweep=False)
        self.add_contour('foam','base','right','top-bubble','middle','left',closed=True)
