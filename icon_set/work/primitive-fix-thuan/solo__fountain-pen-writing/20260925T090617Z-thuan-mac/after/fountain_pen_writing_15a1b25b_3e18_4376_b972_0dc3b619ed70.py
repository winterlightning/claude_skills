"""Restore the curved fountain nib and smooth writing flourish while keeping a clean rounded barrel.
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: pen-line, pen-tool. Original reference establishes full subject and arrangement.
Keyshape SQUARE; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='15a1b25b-3e18-4376-b972-0dc3b619ed70'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fountain-pen-writing/20260925T090617Z-thuan-mac/reference/pen write_15a1b25b-3e18-4376-b972-0dc3b619ed70.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='fountain-pen-writing'
    keyshape=Keyshape.SQUARE
    exception = {'reason': 'Retain the broad writing flourish and naturally angled barrel and nib instead of stretching them to the square envelope. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'b0d091a005be268a8d73b8084f42001d2edf57a4cdcbfe4ea95bc04218d2d9c0'}
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('fountain', 'pen', 'writing')
    def build(self):

        self.path('barrel',(22,26),[('L',(27,17)),('L',(32,8)),('C',(36,5),(33,6),(34,5)),('C',(40,9),(39,5),(40,6)),('C',(39,13),(40,10),(40,11)),('L',(34,22)),('L',(29,31)),('L',(22,26))],True)
        self.path('nib',(22,26),[('C',(18,40),(18,30),(18,34)),('C',(29,31),(27,36),(30,34)),('L',(22,26))],True)
        self.relate('connect','barrel','nib')
        self.path('writing',(4,42),[('C',(18,40),(10,36),(12,45))]);self.relate('connect','writing','nib')


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


