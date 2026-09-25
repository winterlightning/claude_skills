"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '59e5c54e-47c7-45fc-becf-a493bbebd830'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__five-rounded-flower-petals/20260925T090056Z-thuan-mac/reference/onam 2_59e5c54e-47c7-45fc-becf-a493bbebd830.svg'
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
    icon_id = 'five-rounded-flower-petals'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve the five-lobe natural envelope and connected radial seams rather than forcing a square silhouette.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '39d8e4c74669caa186025d112ee12a76b271258a0604122107aefd0686ae4fd2'}
    aliases = ()
    keywords = ()

    def build(self):
        # Five distinct round lobes with mirrored left/right pairs.
        self.add_arc('top',(16,16),(32,16),radius_x=8)
        self.add_arc('right',(32,16),(36,28),radius_x=7,large_arc=True)
        self.add_arc('bottom-right',(36,28),(24,36),radius_x=8,large_arc=True)
        self.add_arc('bottom-left',(24,36),(12,28),radius_x=8,large_arc=True)
        self.add_arc('left',(12,28),(16,16),radius_x=7,large_arc=True)
        self.add_contour('petals','top','right','bottom-right','bottom-left','left',closed=True)
        circle(self,'center',24,24,5)
        for i,(a,b) in enumerate([((16,16),(21,20)),((32,16),(27,20)),((36,28),(28,27)),((24,36),(24,29)),((12,28),(20,27))]):
            self.add_line(f'seam-{i}',a,b)
