"""Fresh reference repair. Construction reference: Lucide ruler.
Keyshape HRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7bda009e-9307-44d2-81d1-0e1d95fcd9f0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tape measure_7bda009e-9307-44d2-81d1-0e1d95fcd9f0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'retractable-measuring-tape-tool'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tape', 'measure')

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

        # Rounded-square housing owns the hub; extended tape shares the flat bottom.
        self.path('housing',(12,8),('L',(24,8)),('A',(32,16),8,8,True),('L',(32,30)),('L',(32,40)),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,16)),('A',(12,8),8,8,True),closed=True)
        self.circle('hub',18,22,5)
        self.path('tape',(32,30),('L',(44,30)),('L',(44,40)),('L',(32,40)))
        self.relate('connect','housing','tape')
