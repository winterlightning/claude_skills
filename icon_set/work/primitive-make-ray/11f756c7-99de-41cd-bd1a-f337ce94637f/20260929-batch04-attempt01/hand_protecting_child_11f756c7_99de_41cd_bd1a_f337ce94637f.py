"""The protecting hand is a pointed shovel shape, and the child is an unmarked ring. Restore a softly rounded palm and child hair cue beneath it.
Plan: VRECT_L; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand-helping for palm curves; human circular head with a small attached hair lock.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '11f756c7-99de-41cd-bd1a-f337ce94637f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-protecting-child/20260929T105027Z-thuan-mac/reference/kids care 1_11f756c7-99de-41cd-bd1a-f337ce94637f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-protecting-child'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'protecting', 'child')

    def build(self):

        def path(n,start,*commands,closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                k=f'{n}-{j}';kind,end,*args=cmd
                if kind=='L': self.add_line(k,here,end)
                elif kind=='A': self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def bez(n,a,*parts):self.add_bezier(n,a,*parts)
        def arc(n,a,b,r,ry=None,s=True):self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(a,b):self.relate('connect',a,b)
        def rect(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        path('hand',(40,4),('L',(27,4)),('C',(12,10),(21,5),(15,9)),('A',(12,18),4,4,False),('C',(25,17),(17,18),(21,19)),('L',(32,12)),('L',(40,12)))
        circle('child',24,35,9)
        bez('hair',(24,26),((26,28),(24,30),(21,30)));join('hair','child')
