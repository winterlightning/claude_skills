"""Restore a tapered nozzle and smoothly rounded bulb, keeping a clear projecting collar.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: pipette. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'af6d5270-c438-58b6-a281-5ef3d5292d3d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-eyedropper-with-long-collar/20260925T085629Z-thuan-mac/reference/color picker_af6d5270-c438-58b6-a281-5ef3d5292d3d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-eyedropper-with-long-collar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'eyedropper', 'with', 'long', 'collar')
    def build(self):

        self.path('outline',(6,42),[('L',(10,36)),('C',(12,29),(9,33),(10,31)),('L',(28,13)),('L',(33,8)),('C',(36,6),(34,7),(35,6)),('C',(42,12),(39,6),(42,9)),('C',(40,15),(42,13),(41,14)),('L',(35,20)),('L',(19,36)),('C',(12,38),(17,38),(15,39)),('L',(6,42))],True)
        self.add_polyline('collar',(24,9),(28,13),(35,20),(39,24));self.relate('connect','collar','outline')


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

