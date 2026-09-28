"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '67e893bc-5345-575c-b7bf-64734a8a6322'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__feather-quill-with-side-notch/20260925T090056Z-thuan-mac/reference/design tool quill_67e893bc-5345-575c-b7bf-64734a8a6322.svg'
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
    icon_id = 'feather-quill-with-side-notch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    exception = {'reason': 'Preserve pointed vane, notch and diagonal shaft proportions; native openings remain readable.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '162fc0cb8e1bc19626b73628698126f057a80f6ed355100118abc138eaf13238'}
    aliases = ()
    keywords = ()

    def build(self):
        self.add_arc('left',(12,36),(40,4),radius_x=32)
        self.add_arc('upper-right',(40,4),(31,27),radius_x=34)
        self.add_line('notch-1',(31,27),(25,28))
        self.add_line('notch-2',(25,28),(28,31))
        self.add_arc('lower-right',(28,31),(12,36),radius_x=32)
        self.add_contour('vane','left','upper-right','notch-1','notch-2','lower-right',closed=True)
        self.add_polyline('shaft',(4,44),(12,36),(30,18))
        self.relate('connect','shaft','vane')
