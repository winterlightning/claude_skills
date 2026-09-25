"""Rebuild a round bulb, softly tapering neck and short curved outlined stem.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: none. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0e2a3b90-793a-5161-aa41-5a7e08f9195c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-butternut-squash/20260925T085629Z-thuan-mac/reference/butternutsquash_0e2a3b90-793a-5161-aa41-5a7e08f9195c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-butternut-squash'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve natural diagonal gourd proportions and the open curved stem rather than stretching the organic silhouette to a rectangular envelope. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '5cbeab20c543ebbc0aaf4005006c95c19a20dff405cb310b9fee65bf26f5b8fb'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'butternut', 'squash')
    def build(self):

        self.path('squash',(28,12),[('C',(36,12),(30,9),(34,9)),('C',(36,22),(40,15),(39,19)),('C',(28,35),(32,27),(31,31)),('C',(18,42),(26,40),(23,42)),('C',(6,30),(11,42),(6,37)),('C',(13,20),(6,25),(9,22)),('C',(28,12),(19,17),(24,16))],True)
        self.path('stem',(32,4),[('C',(36,12),(41,2),(44,9))]);self.relate('connect','stem','squash')


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

