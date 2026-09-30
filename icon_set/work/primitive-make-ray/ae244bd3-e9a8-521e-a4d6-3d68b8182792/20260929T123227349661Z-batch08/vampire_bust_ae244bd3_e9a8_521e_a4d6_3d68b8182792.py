"""The rejected vampire lacks its bow tie and has a generic round head; restore the bow tie and pointed ears with a smaller circular face. No written reviewer feedback.
Symbol plan: Shared human_ref/user.svg: circular face and broad shoulders. Pointed ears and fang stroke identify the vampire; small eyes and hairline omitted. Body touches jaw ink.
Keyshape VRECT_L, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ae244bd3-e9a8-521e-a4d6-3d68b8182792'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vampire-bust/20260929T121814Z-thuan-mac/reference/fantasy vampire_ae244bd3-e9a8-521e-a4d6-3d68b8182792.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vampire-bust'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('vampire', 'bust')

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

        self.path('head',(24,4),[('A',(34,14),10,10,True),('A',(30,22),10,10,True),('A',(24,24),10,10,True),('A',(18,22),10,10,True),('A',(14,14),10,10,True),('A',(24,4),10,10,True)],True)
        self.add_line('ear-left',(14,14),(8,10));self.relate('connect','ear-left','head')
        self.add_line('ear-right',(34,14),(40,10));self.relate('connect','ear-right','head')
        self.add_line('fang-left',(18,22),(18,26));self.add_line('fang-right',(30,22),(30,26));self.relate('connect','fang-left','head');self.relate('connect','fang-right','head')
        self.add_polyline('bow',(8,32),(24,38),(40,32),(40,44),(24,38),(8,44),closed=True)

