"""Rejected rocking figure sat as a right-angle glyph attached to the base. Restore a curved seated back and bent forward arm, with a distinct rising rocker.
Symbol plan: human_ref/full_body_ref.png circular head, curved seated torso. Head bottom16 to torso24 gives exact4 ink gap.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd50e4120-77d7-422c-a424-5d54b2dccc50'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-figure-on-curved-rocker/20260929T112503Z-thuan-mac/reference/rocker_d50e4120-77d7-422c-a424-5d54b2dccc50.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'seated-figure-on-curved-rocker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'figure', 'on', 'curved', 'rocker')

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

        circle('head',19,11,5)
        path('torso',(19,24),[('C',(17,30),(19,26),(17,28)),('A',(21,34),4,4,False)])
        poly('leg',(21,34),(29,34),(36,40));join('torso','leg')
        poly('arm',(19,24),(25,26),(30,26));join('arm','torso')
        path('rocker',(6,32),[('C',(24,42),(9,39),(16,42)),('C',(36,40),(29,42),(33,42)),('C',(42,30),(40,38),(42,33))])
        join('leg','rocker')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
