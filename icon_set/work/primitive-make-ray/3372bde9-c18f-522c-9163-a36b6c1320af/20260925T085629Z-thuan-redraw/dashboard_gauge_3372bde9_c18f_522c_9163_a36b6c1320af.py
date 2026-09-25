"""Restore five scale marks and an open needle hub; smooth symmetric dial.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: gauge. Original source establishes full subject and arrangement.
Keyshape: HRECT_L; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3372bde9-c18f-522c-9163-a36b6c1320af'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dashboard-gauge/20260925T085629Z-thuan-mac/reference/gauge dashboard_3372bde9-c18f-522c-9163-a36b6c1320af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dashboard-gauge'
    keyshape = Keyshape.HRECT_L
    exception = {'reason': 'The exact four-unit visible hub-to-baseline gap is visually clear; retain the numerical curve-certification warning. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '515e3085ca3aea9c4572c684160f0ba886ac27aa3d7aa811dbaeea9a186b5dad'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dashboard', 'gauge')
    def build(self):

        self.path('dial',(8,40),[('C',(4,28),(5,36),(4,32)),('C',(10,14),(4,22),(6,18)),('C',(24,8),(14,10),(18,8)),('C',(38,14),(30,8),(34,10)),('C',(44,28),(42,18),(44,22)),('C',(40,40),(44,32),(43,36)),('L',(8,40))],True)
        for name,a,b in [('left',(4,28),(8,28)),('upper-left',(10,14),(13,17)),('top',(24,8),(24,12)),('upper-right',(38,14),(35,17)),('right',(44,28),(40,28))]:
            self.add_line(name,a,b);self.relate('connect',name,'dial')
        self.circle('hub',24,29,3)
        self.add_line('needle',(24,26),(28,21));self.relate('connect','needle','hub')


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

