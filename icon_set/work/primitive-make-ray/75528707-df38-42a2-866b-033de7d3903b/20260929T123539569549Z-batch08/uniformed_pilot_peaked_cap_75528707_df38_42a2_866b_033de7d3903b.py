"""The rejected pilot cap is a sharp pentagon and the uniform lacks its collar; restore a flatter rounded cap and collar cue. No written reviewer feedback.
Symbol plan: Shared human reference: circular jaw and touching shoulder construction. Cap follows source flattened crown; fine emblems and sleeve divisions omitted.
Keyshape VRECT_L, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='75528707-df38-42a2-866b-033de7d3903b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__uniformed-pilot-peaked-cap/20260929T121814Z-thuan-mac/reference/airman_75528707-df38-42a2-866b-033de7d3903b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='uniformed-pilot-peaked-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('uniformed', 'pilot', 'peaked', 'cap')
    human_construction='bust'

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

        self.path('cap',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(34,16)),('L',(14,16)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('face',(34,16),[('A',(14,16),10,10,True)]);self.relate('connect','face','cap')
        self.path('body',(8,44),[('L',(8,40)),('A',(12,32),10,10,True),('A',(18,30),10,10,True),('L',(30,30)),('A',(36,32),10,10,True),('A',(40,40),10,10,True),('L',(40,44))]);self.relate('connect','face','body')
        self.add_polyline('collar',(12,32),(24,40),(36,32));self.relate('connect','collar','body')
