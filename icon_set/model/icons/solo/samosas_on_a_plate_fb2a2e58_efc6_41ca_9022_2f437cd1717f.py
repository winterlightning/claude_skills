"""Fresh reference repair. Construction reference: No useful Lucide samosa match; supplied reference.
Keyshape HRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fb2a2e58-efc6-41ca-9022-2f437cd1717f'
SOURCE_PATH = 'pictographic-primitives/other/samosa_fb2a2e58-efc6-41ca-9022-2f437cd1717f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'samosas-on-a-plate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('samosa',)

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
        # Two overlapping triangular pastries; an oval rim remains visible around their bases.
        self.add_polyline('front',(12,30),(16,20),(20,10),(26,20),(32,30),closed=True)
        self.add_polyline('rear',(26,20),(33,8),(40,20),closed=True)
        self.path('plate',(16,20),('C',(4,30),(4,20),(4,26)),('C',(24,40),(4,36),(14,40)),('C',(44,30),(34,40),(44,36)),('C',(40,20),(44,26),(42,22)))
        self.relate('connect','front','rear');self.relate('connect','front','plate');self.relate('connect','rear','plate')

    icon_id = 'samosas-on-a-plate'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('samosas', 'on', 'a', 'plate')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
