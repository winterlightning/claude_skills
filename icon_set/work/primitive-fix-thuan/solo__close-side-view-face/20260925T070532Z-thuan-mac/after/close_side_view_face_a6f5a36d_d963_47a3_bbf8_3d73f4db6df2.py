"""Flowing nose, readable lips and natural chin with larger clear ear opening.
Plan: coherent named contours and repeated dimensions. VRECT_L natural subject envelope.
Construction reference: human_ref/user.svg supports smooth anatomy; no exact Lucide facial-profile match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a6f5a36d-d963-47a3-bbf8-3d73f4db6df2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__close-side-view-face/20260925T070532Z-thuan-mac/reference/cheek_a6f5a36d-d963-47a3-bbf8-3d73f4db6df2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'close-side-view-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('cheek',)

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('face',(17,4),[('C',(8,20),(17,11),(8,16)),('C',(13,23),(8,23),(11,23)),('C',(12,29),(12,25),(11,27)),('C',(14,32),(12,31),(14,31)),('L',(14,35)),('C',(21,40),(14,40),(17,40)),('C',(27,39),(23,40),(25,40)),('C',(37,32),(33,37),(37,36))])
        path('ear',(30,13),[('C',(40,14),(30,5),(40,5)),('C',(33,23),(40,20),(37,23))])
        path('neck',(27,39),[('C',(31,44),(29,40),(30,42))])
        join('neck','face')
