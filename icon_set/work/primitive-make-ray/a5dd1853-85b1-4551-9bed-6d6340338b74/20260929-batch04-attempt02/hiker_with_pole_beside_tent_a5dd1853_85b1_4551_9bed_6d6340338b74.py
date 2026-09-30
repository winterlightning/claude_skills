"""The rejected hiker has a floating tiny head and an incomplete narrow tent; its lowered arm is missing. Restore a larger aligned head, natural arm/pole grip and a triangular tent.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Shared human full_body_ref.png: aligned round head, curved arm, exact 4u ink neck gap; source triangular tent.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a5dd1853-85b1-4551-9bed-6d6340338b74'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiker-with-pole-beside-tent/20260929T105027Z-thuan-mac/reference/camping trekking 2_a5dd1853-85b1-4551-9bed-6d6340338b74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hiker-with-pole-beside-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hiker', 'with', 'pole', 'beside', 'tent')

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
        circle('head',12,11,5)
        line('torso',(12,24),(12,33));self.mark_human_figure('hiker',head='head',torso='torso',torso_junction='start')
        poly('legs',(6,42),(12,33),(18,42));join('legs','torso')
        bez('arm',(12,24),((15,24),(15,28),(20,28)))
        line('grip',(20,28),(24,28));join('arm','grip');join('arm','torso')
        poly('pole',(24,24),(24,28),(24,42));join('pole','grip')
        poly('tent',(32,42),(42,42),(37,23),(32,42),closed=True)
        bez('lower-arm',(12,24),((8,24),(6,24),(6,26)));join('lower-arm','torso');join('lower-arm','arm')
