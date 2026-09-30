"""Current skier-like angular torso has a floating head to the right. Rebuild a leaning snowboarder with head aligned to upper torso and bent knees over a curved board.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/full_body_ref.png: head aligned to torso, bent round-ended limbs
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b8ecce3b-c3ce-5fe4-89dc-d203d8bbf4d9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-snowboarding-downhill-upload-52ddb7b225333f49/20260929T135610Z-thuan-mac/reference/person-snowboarding-downhill-upload-52ddb7b225333f49_b8ecce3b-c3ce-5fe4-89dc-d203d8bbf4d9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-snowboarding-downhill-upload-52ddb7b225333f49'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'snowboarding', 'downhill', 'upload', '52ddb7b225333f49')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        oval('head',32,10,4,4)
        poly('torso',(32,22),(32,26),(24,30))
        poly('front-leg',(24,30),(36,32),(32,40));join('front-leg','torso')
        poly('back-arm',(32,22),(22,22),(14,28));join('back-arm','torso')
        line('front-arm',(32,22),(40,26));join('front-arm','torso');join('front-arm','back-arm')
        poly('rear-leg',(24,30),(16,30),(12,38));join('rear-leg','torso');join('rear-leg','front-leg')
        path('board',(6,36),[('C',(32,42),(14,40),(24,42)),('C',(42,40),(37,42),(40,41))]);join('board','rear-leg');join('board','front-leg')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
