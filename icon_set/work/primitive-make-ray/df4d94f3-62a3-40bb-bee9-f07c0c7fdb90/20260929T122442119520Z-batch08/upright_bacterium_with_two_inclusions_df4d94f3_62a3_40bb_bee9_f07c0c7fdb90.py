"""The rejected bacterium is upright with rail-like projections; restore the reference diagonal capsule and radial protrusions. No written reviewer feedback.
Restored the diagonal capsule and four radial projections, preserving both inclusions.
Construction: No useful exact local Lucide match; source diagonal capsule construction.
Omissions: Inclusion rings reduced to two dots; four clear projections replace the fine perimeter series.
Keyshape: SQUARE. Balanced overall composition; centerline extremes (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='df4d94f3-62a3-40bb-bee9-f07c0c7fdb90'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__upright-bacterium-with-two-inclusions/20260929T121814Z-thuan-mac/reference/bacterium_df4d94f3-62a3-40bb-bee9-f07c0c7fdb90.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='upright-bacterium-with-two-inclusions'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('upright', 'bacterium', 'with', 'two', 'inclusions')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.path('cell',(13,21),[('L',(21,13)),('A',(35,27),10,10,True),('L',(27,35)),('A',(13,21),10,10,True)],True)
        for i,(a,b) in enumerate([((13,21),(6,16)),((21,13),(16,6)),((35,27),(42,32)),((27,35),(32,42))]):
            self.add_line(f'projection-{i}',a,b);self.relate('connect',f'projection-{i}','cell')
        self.add_dot('inclusion-a',(20,28));self.add_dot('inclusion-b',(28,20))
