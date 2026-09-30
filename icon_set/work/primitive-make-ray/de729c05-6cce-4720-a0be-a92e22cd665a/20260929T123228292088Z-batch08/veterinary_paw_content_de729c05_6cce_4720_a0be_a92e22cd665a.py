"""The rejected paw toes are dots and the medical cross nearly disappears; restore outlined toes and a larger cross. No written reviewer feedback.
Enlarged the medical cross and central toe opening, with a taller paw pad.
Construction: Lucide paw-print original and atomic-debug; source three-toe pad and medical cross.
Omissions: Side toe rings use the existing small-circle exception and read as round marks at native size.
Keyshape: VRECT_L. Vertical composition; centerline extremes (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='de729c05-6cce-4720-a0be-a92e22cd665a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__veterinary-paw-content/20260929T121814Z-thuan-mac/reference/paw print with a cross_de729c05-6cce-4720-a0be-a92e22cd665a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='veterinary-paw-content'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('veterinary', 'paw', 'content')

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

        for i,(x,y) in enumerate(((24,7),(10,13),(38,13))):self.circle(f'toe-{i}',x,y,3 if i==0 else 2)
        self.path('pad',(14,44),[('A',(8,38),6,6,True),('C',(24,20),(8,30),(14,20)),('C',(40,38),(34,20),(40,30)),('A',(34,44),6,6,True),('L',(14,44))],True)
        self.add_polyline('cross-h',(21,32),(24,32),(27,32));self.add_polyline('cross-v',(24,29),(24,32),(24,35));self.relate('connect','cross-h','cross-v')

