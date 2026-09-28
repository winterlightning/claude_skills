"""Restore curved crescent horns and a clear hooked arrow tail around a balanced heart.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: heart. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1e5fb62e-d39c-58a2-9bd4-d0f7063bf952'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__devilish-heart/20260925T085629Z-thuan-mac/reference/succubus sigil_1e5fb62e-d39c-58a2-9bd4-d0f7063bf952.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'devilish-heart'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the legible hooked arrow tail and curved horns. The tail extends two units beyond the square envelope and has locally reduced arrow clearance. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'd4ea41c5fa33bdde7ce77822c5c496a15bed6dd070e2a228bb3d7c06bf91fb9d'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('devilish', 'heart')
    def build(self):

        self.path('heart',(21,19),[('C',(12,16),(18,15),(15,14)),('C',(7,23),(8,17),(7,19)),('C',(21,35),(7,28),(15,32)),('C',(30,28),(25,32),(28,30)),('C',(35,23),(33,26),(35,25)),('C',(30,16),(35,19),(34,17)),('C',(21,19),(27,14),(24,15))],True)
        self.path('horn-left',(12,16),[('C',(6,6),(7,16),(6,10))]);self.relate('connect','horn-left','heart')
        self.path('horn-right',(30,16),[('C',(36,6),(35,16),(36,10))]);self.relate('connect','horn-right','heart')
        self.path('tail',(30,28),[('L',(36,28)),('A',(42,34),6,6,True),('A',(36,40),6,6,True),('L',(25,40))]);self.relate('connect','tail','heart')
        self.add_polyline('arrow',(30,36),(25,40),(30,44));self.relate('connect','arrow','tail')


    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

