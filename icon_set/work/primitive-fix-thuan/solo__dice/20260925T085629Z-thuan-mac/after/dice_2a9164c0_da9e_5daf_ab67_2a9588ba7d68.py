"""Use consistent six-unit corner radii and enlarge the outlined central pip so it reads as a circle.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: dice-1. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2a9164c0-da9e-5daf-ab67-2a9588ba7d68'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dice/20260925T085629Z-thuan-mac/reference/dice_2a9164c0-da9e-5daf-ab67-2a9588ba7d68.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dice',)
    def build(self):

        self.box('die',6,6,42,42,6)
        self.circle('pip',24,24,4)


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

