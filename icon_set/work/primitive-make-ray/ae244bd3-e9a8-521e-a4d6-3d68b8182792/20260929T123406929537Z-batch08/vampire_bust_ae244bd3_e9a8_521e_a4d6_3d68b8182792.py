"""The rejected vampire lacks its bow tie and has a generic round head; restore the bow tie and pointed ears with a smaller circular face. No written reviewer feedback.
Restored an outlined bow tie below the circular fanged face and pointed ears.
Construction: Shared human_ref/user.svg circular head; source pointed ears, fangs and bow tie. Bow tie is an accessory; shoulders are omitted.
Omissions: Shoulder outline, fine eyes and hairline omitted so the bow tie and fangs survive at 48 px.
Keyshape: VRECT_L. Vertical composition; centerline extremes (8,4)-(40,44).
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

        self.circle('head',24,17,13)
        self.add_line('ear-left',(11,17),(8,10));self.relate('connect','ear-left','head')
        self.add_line('ear-right',(37,17),(40,10));self.relate('connect','ear-right','head')
        self.add_polyline('fangs',(20,19),(20,17),(28,17),(28,19))
        self.add_polyline('bow',(8,36),(24,40),(40,36),(40,44),(24,40),(8,44),closed=True)

