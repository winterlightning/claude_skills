"""Fresh reference repair. Construction reference: No useful Lucide hanger match; supplied reference.
Keyshape HRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b8261937-d8d8-4ee2-83fd-5404997b0511'
SOURCE_PATH = 'pictographic-primitives/other/hanger_b8261937-d8d8-4ee2-83fd-5404997b0511.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'clothes-hanger'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hanger',)

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):

        # Symmetric triangular shoulders, smoothly rounded ends and a separate short hook stem.
        self.path('frame',(24,24),('L',(42,34)),('C',(44,37),(43,35),(44,36)),('C',(40,40),(44,39),(42,40)),('L',(8,40)),('C',(4,37),(6,40),(4,39)),('C',(6,34),(4,36),(5,35)),('L',(24,24)),closed=True)
        self.path('hook',(18,14),('A',(24,8),6,6,True),('A',(30,14),6,6,True),('A',(24,20),6,6,True),('L',(24,24)))
        self.relate('connect','hook','frame')

    icon_id = 'clothes-hanger'
    category = 'objects'
    aliases = ()
    keywords = ('clothes', 'hanger')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
