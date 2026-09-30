"""The rejected offering hand curls almost vertically; restore the reference horizontal palm, forearm and softly raised fingertips. No written reviewer feedback.
Reoriented the palm horizontally and opened the space between the thumb and outer fingers.
Construction: Lucide hand-helping original and atomic-debug; source horizontal offering gesture.
Omissions: Fine skin creases omitted.
Keyshape: HRECT_M. Horizontal offering hand; centerline extremes (4,10)-(44,38).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='28ebd0ec-a7a1-4063-b621-7c3eb8b9fd1a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__upturned-offering-hand/20260929T121814Z-thuan-mac/reference/give hand_28ebd0ec-a7a1-4063-b621-7c3eb8b9fd1a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='upturned-offering-hand'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('upturned', 'offering', 'hand')

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

        self.path('palm',(4,18),[('C',(17,12),(10,18),(11,12)),('C',(28,18),(22,12),(23,18)),('L',(31,18)),('L',(38,12)),('C',(42,10),(40,10),(41,10)),('C',(44,14),(44,10),(44,12)),('C',(42,24),(44,18),(44,22)),('L',(33,34)),('C',(22,38),(29,38),(25,38)),('C',(4,32),(15,38),(10,30))])
        self.path('thumb',(18,26),[('L',(24,26)),('C',(31,18),(28,26),(31,22))]);self.relate('connect','thumb','palm')
