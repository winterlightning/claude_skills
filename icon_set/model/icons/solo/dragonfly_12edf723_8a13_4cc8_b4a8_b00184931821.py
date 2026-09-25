"""Restore a larger oval head, four slender smooth wings and a long tail; derive wings by reflection.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: none. Original source establishes full subject and arrangement.
Keyshape: VRECT_L; preserve natural source proportions where a documented exception is needed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '12edf723-8a13-4cc8-b4a8-b00184931821'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dragonfly/20260925T085629Z-thuan-mac/reference/dragonfly_12edf723-8a13-4cc8-b4a8-b00184931821.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dragonfly-solo'
    keyshape = Keyshape.VRECT_L
    exception = {'reason': 'Preserve four tapered wings, large oval head and long tail. Natural wing-tip narrowing and head-to-wing spacing remain visually distinct at native size. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '2f1701b213a77eb0bf015a31eb61c425c2d4f82cab749d402b24c52992cbc74d'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dragonfly',)
    def build(self):

        self.path('head',(24,4),[('A',(24,12),6,4,True),('A',(24,4),6,4,True)],True)
        self.add_polyline('body',(24,12),(24,22),(24,28),(24,44));self.relate('connect','body','head')
        for name,sign in [('left',-1),('right',1)]:
            p=lambda x,y:(24+sign*x,y)
            self.path(name+'-upper',(24,22),[('C',p(12,16),p(4,17),p(8,16)),('C',p(16,20),p(16,16),p(16,18)),('C',(24,22),p(16,24),p(8,24))],True)
            self.path(name+'-lower',(24,22),[('C',p(12,30),p(4,26),p(9,27)),('C',p(12,36),p(16,33),p(16,36)),('C',(24,28),p(6,36),p(2,33)),('L',(24,22))],True)
            self.relate('connect','body',name+'-upper');self.relate('connect','body',name+'-lower');self.relate('connect',name+'-upper',name+'-lower')
        self.relate('connect','left-upper','right-upper');self.relate('connect','left-lower','right-lower');self.relate('connect','left-upper','right-lower');self.relate('connect','right-upper','left-lower')


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

