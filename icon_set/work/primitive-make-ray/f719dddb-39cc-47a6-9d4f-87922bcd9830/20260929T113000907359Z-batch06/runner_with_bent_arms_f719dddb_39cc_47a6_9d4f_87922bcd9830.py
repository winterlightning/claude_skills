"""Rejected runner had an undersized head and stiff flat shoulders. Enlarge head, curve the torso through the hip and give both arms a clear elbow while retaining opposed legs.
Symbol plan: human_ref/full_body_ref.png: radius5 head, torso at24, exact4 ink gap; curved upper torso has vertical neck tangent.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f719dddb-39cc-47a6-9d4f-87922bcd9830'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__runner-with-bent-arms/20260929T112503Z-thuan-mac/reference/caper_f719dddb-39cc-47a6-9d4f-87922bcd9830.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'runner-with-bent-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('runner', 'with', 'bent', 'arms')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        circle('head',28,11,5)
        path('torso',(28,24),[('C',(22,32),(28,27),(24,30))])
        poly('rear-arm',(28,24),(17,20),(10,27));poly('front-arm',(28,24),(34,30),(42,27))
        poly('rear-leg',(22,32),(15,40),(6,40));poly('front-leg',(22,32),(32,36),(29,42))
        for a in ['rear-arm','front-arm','rear-leg','front-leg']:join('torso',a)
        join('rear-arm','front-arm');join('rear-leg','front-leg')
        self.mark_human_figure('runner',head='head',torso='torso-0',torso_junction='start')
