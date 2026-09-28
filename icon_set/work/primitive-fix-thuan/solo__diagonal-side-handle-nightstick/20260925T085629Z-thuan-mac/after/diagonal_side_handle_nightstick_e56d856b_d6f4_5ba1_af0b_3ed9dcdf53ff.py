"""Restore the shallow diagonal baton and rounded outlined perpendicular side grip.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: none. Original source establishes full subject and arrangement.
Keyshape: VRECT_M; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e56d856b-d6f4-5ba1-af0b-3ed9dcdf53ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-side-handle-nightstick/20260925T085629Z-thuan-mac/reference/police nightstick_e56d856b-d6f4-5ba1-af0b-3ed9dcdf53ff.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-side-handle-nightstick'
    keyshape = Keyshape.VRECT_M
    exception = {'reason': 'Keep the reference shallow baton angle and small outlined side grip. Grip opening is visibly open at native size; organic cap extrema slightly differ from the rectangular guide. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'db3a940d73105a8bb38deba90fa10cfd6949a27bf045f43fee9bd3cd4006bb8f'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'side', 'handle', 'nightstick')
    def build(self):

        self.path('baton',(28,8),[('C',(34,4),(29,5),(31,4)),('C',(38,10),(37,4),(39,7)),('L',(29,39)),('C',(23,44),(28,42),(26,44)),('C',(19,38),(20,44),(18,41)),('L',(22,28)),('L',(24,22)),('L',(28,8))],True)
        self.path('grip',(24,22),[('L',(14,19)),('C',(12,25),(9,18),(8,24)),('L',(22,28))]);self.relate('connect','grip','baton')


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

