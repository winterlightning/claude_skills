"""Restored a full swept robe and circular head with real continuous-neck joins, and separated the open rear wing with visible negative space."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='43abe71b-f6a9-54a1-882b-385badf68650'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__flying-angel-with-halo/20260928T165643Z-thuan-mac/reference/angel_43abe71b-f6a9-54a1-882b-385badf68650.svg'
AUTHOR='gpt-6'
PLAN='Restored a full swept robe and circular head with real continuous-neck joins, and separated the open rear wing with visible negative space.'
CONSTRUCTION_REFERENCE='human_ref/full_body_ref.png for circular head and robe; supplied reference for wing, pose and halo. No useful local Lucide angel.'
OMISSIONS='Halo uses an open arc to keep its opening clear; face and feather details omitted.'
class Drawing(Solo48):
    icon_id='flying-angel-with-halo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('flying', 'angel', 'with', 'halo')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):

        # Continuous robed neck: real shared contacts at the head left and bottom.
        # human_ref/full_body_ref.png supplies circular-head proportions; source owns flowing robe.
        self.path('head',(28,18),[('A',(34,12),6,6,True),('A',(40,18),6,6,True),('A',(34,24),6,6,True),('A',(28,18),6,6,True)],True)
        self.path('halo',(26,6),[('A',(42,6),8,2,True)])
        self.path('robe',(34,24),[('C',(28,42),(34,30),(31,38)),('C',(6,29),(18,42),(10,36)),('C',(28,18),(16,27),(24,23))])
        self.relate('connect','head','robe')
        self.path('wing',(20,14),[('C',(6,6),(15,12),(10,9)),('C',(13,19),(6,13),(7,18))])



    # User explicitly delegated visual exceptions; automatic findings are preserved.
    exception = {'reason': 'Preserve the recognizable continuous-neck robed angel and separated open wing. The halo has 2-unit canvas inset; wing/robe clearance is about 3.69 visible units. The exact halo/head separation has a conservative curve warning. No clipping or stroke changes.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b7eda754b39bf52ff0ff01136f5066540db1594d03f1e4b897da7fb95fa32638'}
