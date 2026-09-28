'Airplane taking off.\nPlan: HRECT_L preserves the wide climbing silhouette. Widened wings and fuselage; raised tail is intentionally asymmetric.\nReference: plane-takeoff; Coherent fuselage, broad swept wings and round nose.\nChanges: No defining parts omitted; proportions broadened for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8fe19626-3dae-5f95-be02-4dbe10f65534'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_8fe19626-3dae-5f95-be02-4dbe10f65534.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'climbing-airplane-rounded-nose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('plane', '1')
    def build(self):
        self.path('plane',(4,16),[('L',(8,16)),('L',(12,22)),('L',(23,18)),('L',(12,8)),('L',(26,8)),('L',(33,18)),('L',(36,17)),('C',(44,22),(40,16),(44,19)),('C',(38,27),(44,25),(42,26)),('L',(32,28)),('L',(27,40)),('L',(17,40)),('L',(22,29)),('L',(12,32)),('C',(4,24),(8,33),(4,28)),('L',(4,16))],True)

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

PARENT_MODULE = 'icon_set/model/icons/solo/climbing_airplane_rounded_nose_8fe19626_3dae_5f95_be02_4dbe10f65534.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'b276d60d5308a3e3b35a8f27721128866939a81fea119ade7c8f2e63544aa057', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '8fe19626-3dae-5f95-be02-4dbe10f65534'}
