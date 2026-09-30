"""Rejected AIM runner looked mechanical, with a tiny head and angular torso. Enlarge head, smooth the raised forearm and lower torso, and retain the wide running stride.
Symbol plan: human_ref/full_body_ref.png: radius5 head, neck24, exact4 ink gap.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e67d265c-c409-4a6f-a8fd-58e1dec4e65f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__running-person-rounded-silhouette/20260929T112503Z-thuan-mac/reference/aim logo_e67d265c-c409-4a6f-a8fd-58e1dec4e65f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'running-person-rounded-silhouette'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('running', 'person', 'rounded', 'silhouette')

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

        circle('head',30,11,5)
        line('torso',(30,24),(30,26))
        path('lower-torso',(30,26),[('C',(24,32),(30,28),(27,30))]);join('torso','lower-torso')
        poly('back-arm',(30,24),(20,24),(12,30))
        path('front-arm',(30,24),[('L',(36,24)),('A',(42,18),6,6,False)])
        poly('rear-leg',(24,32),(16,40),(6,40));poly('front-leg',(24,32),(34,35),(34,42))
        join('torso','back-arm');join('torso','front-arm');join('lower-torso','rear-leg');join('lower-torso','front-leg')
        join('back-arm','front-arm');join('rear-leg','front-leg')
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
