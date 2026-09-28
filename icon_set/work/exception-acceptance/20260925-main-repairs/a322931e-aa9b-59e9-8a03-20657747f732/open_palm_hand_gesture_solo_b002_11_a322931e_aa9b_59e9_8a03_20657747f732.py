'Upturned offering hand with rounded thumb above palm and long fingers pointing right. Centerline4,10 to44,38.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a322931e-aa9b-59e9-8a03-20657747f732'
SOURCE_PATH = 'pictographic-primitives/business/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCE = 'Lucide hand-helping: rounded thumb returning into palm and long finger edge.'
OMISSIONS = 'Finger divisions omitted as in source.'

def path(s,n,p,cs,closed=False):
    ids=[]
    for j,c in enumerate(cs):
        eid=f'{n}-{j}';q=c[-1]
        if c[0]=='L':s.add_line(eid,p,q)
        elif c[0]=='A':s.add_arc(eid,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
        elif c[0]=='C':s.add_bezier(eid,p,(c[1],c[2],q))
        ids.append(eid);p=q
    s.add_contour(n,*ids,closed=closed)
def circle(s,n,x,y,r):
    path(s,n,(x-r,y),[('A',r,r,True,(x+r,y)),('A',r,r,True,(x-r,y))],True)

class Drawing(Solo48):
    icon_id = 'open-palm-hand-gesture-solo-b002-11'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('begging', 'hand', 'ask')
    def build(self):
        # Continuous palm contour; thumb meets the finger at a shared endpoint without overlap.
        path(self,'hand',(4,34),[('L',(4,16)),('C',(10,14),(13,10),(18,10)),('C',(23,10),(27,12),(27,17)),('A',7,7,True,(20,24)),('L',(14,22))])
        path(self,'fingers',(27,17),[('L',(35,12)),('C',(40,9),(44,12),(44,17)),('C',(44,21),(42,24),(39,26)),('L',(27,35)),('C',(24,38),(21,38),(19,38)),('L',(4,34))])
        self.relate('connect','hand','fingers')


# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '8f1f863c84d4c082a05d3011fad8281d4f6d86ac612a53e71b7e4983048e58fe', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'a322931e-aa9b-59e9-8a03-20657747f732'}
