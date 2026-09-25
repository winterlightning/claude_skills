'Document with clock.\nPlan: SQUARE maximizes space for radius-10 clock inside the clipped page. Hands share one off-center junction.\nReference: file-clock; Circular clock and joined angular hands, kept enclosed as in the supplied source.\nChanges: No parts omitted; hands are necessarily very short (2 units each) and less legible at native size.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e7ce785e-158f-41d6-9e8b-dcba4879acac'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock file 1_e7ce785e-158f-41d6-9e8b-dcba4879acac.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'time-clock-file-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('time', 'clock', 'file', '1')
    def build(self):
        self.add_polyline('file',(6,6),(32,6),(42,16),(42,42),(6,42),closed=True)
        self.circle('clock',24,24,10)
        self.add_polyline('hands',(23,23),(23,25),(25,25))


    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; p=n+str(i)
            if i%2:self.add_arc(p,a,z,radius_x=rad)
            else:self.add_line(p,a,z)
            members.append(p)
        self.add_contour(n,*members,closed=True)

PARENT_MODULE = 'icon_set/model/icons/solo/time_clock_file_1_e7ce785e_158f_41d6_9e8b_dcba4879acac.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '1759ad2a469976443769bccadb25c5ac65461a0f5c250b5bef973060e4fa48d8', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'e7ce785e-158f-41d6-9e8b-dcba4879acac'}
