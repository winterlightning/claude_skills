"""Replace the pointed leaf silhouette with a smooth full oval and flowing diagonal seam.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: bean. Original source establishes full subject and arrangement.
Keyshape: VRECT_L; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0b19900b-2f50-4eb1-8024-c7cb4c3c1ae7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-oval-coffee-bean/20260925T085629Z-thuan-mac/reference/bean_0b19900b-2f50-4eb1-8024-c7cb4c3c1ae7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-oval-coffee-bean'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'oval', 'coffee', 'bean')
    def build(self):

        self.path('bean',(31,4),[('C',(40,16),(37,4),(40,9)),('C',(17,44),(40,30),(29,44)),('C',(8,32),(11,44),(8,39)),('C',(31,4),(8,18),(19,4))],True)
        self.path('seam',(31,4),[('C',(24,24),(29,11),(29,18)),('C',(17,44),(19,30),(19,37))]);self.relate('connect','seam','bean')


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

