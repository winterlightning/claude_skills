"""Restore the central flower disk, four equal rounded petals, two pointed leaves and a short visible stem below the leaf junction.
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: flower-2. Original reference establishes full subject and arrangement.
Keyshape VRECT_L; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bc50f80c-32d1-4463-8d50-0760d877bb3f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__four-petal-stemmed-flower/20260925T090617Z-thuan-mac/reference/bloom_bc50f80c-32d1-4463-8d50-0760d877bb3f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='four-petal-stemmed-flower'
    keyshape=Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('four', 'petal', 'stemmed', 'flower')
    def build(self):

        self.path('bloom',(18,10),[('A',(30,10),6,6,True),('A',(30,22),6,6,True),('A',(24,28),6,6,True),('A',(18,22),6,6,True),('A',(18,10),6,6,True)],True)
        self.circle('disk',24,16,3)
        self.add_polyline('stem',(24,28),(24,42),(24,44));self.relate('connect','stem','bloom')
        for name,sign in [('left',-1),('right',1)]:
            p=lambda x,y:(24+sign*x,y)
            self.path(name+'-leaf',(24,42),[('C',p(16,32),p(10,42),p(16,39)),('C',(24,42),p(7,32),p(2,36))],True)
            self.relate('connect',name+'-leaf','stem')
        self.relate('connect','left-leaf','right-leaf')


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


