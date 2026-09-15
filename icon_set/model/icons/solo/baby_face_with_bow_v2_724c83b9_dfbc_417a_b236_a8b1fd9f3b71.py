"""Remove both ears. A continuous rounded cheek and jaw outline connects directly to the original bow, retaining the eyes and smile.
Reference: Existing baby face with bow; shared rounded human face vocabulary
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '724c83b9-dfbc-417a-b236-a8b1fd9f3b71'
SOURCE_PATH = 'pictographic-primitives/babies/baby girl_724c83b9-dfbc-417a-b236-a8b1fd9f3b71.svg'
AUTHOR = 'gpt-6'

class BabyFaceWithBowVariant2(Solo48):
    icon_id = 'baby-face-with-bow-v2'
    variant_of = 'baby-face-with-bow'
    variant_label = 'Revised after specific drawing feedback, 16 September'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'face', 'with', 'bow')

    def build(self):
        # Symbol plan: Remove both ears. A continuous rounded cheek and jaw outline connects directly to the original bow, retaining the eyes and smile.

        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('face',(10,20),[('A',(6,24),4,4,False),('A',(42,24),18,18,False),('A',(38,20),4,4,False)])
        poly('bow-left',(24,13),(10,6),(10,20),closed=True);poly('bow-right',(24,13),(38,6),(38,20),closed=True)
        join('bow-left','bow-right');join('bow-left','face');join('bow-right','face')
        dot('eye-left',(17,26));dot('eye-right',(31,26))
        self.add_arc('smile',(21,33),(27,33),radius_x=4,radius_y=2,sweep=False)
