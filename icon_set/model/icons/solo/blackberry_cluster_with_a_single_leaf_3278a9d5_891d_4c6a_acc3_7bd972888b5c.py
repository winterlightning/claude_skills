"""Blackberry with rounded outer drupelets, central fruit cell, lower paired lobes and one pointed leaf.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: grape: overlapping rounded regions; source governs elongated blackberry cluster
Omissions: Fine extra cell boundaries and tiny stem curl omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3278a9d5-891d-4c6a-acc3-7bd972888b5c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/blackberry_3278a9d5-891d-4c6a-acc3-7bd972888b5c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='blackberry-cluster-with-a-single-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('blackberry', 'cluster', 'with', 'a', 'single', 'leaf')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('berry',(24,14),[('C',(38,22),(30,12),(38,14)),('C',(35,34),(40,26),(40,31)),('C',(24,44),(35,40),(31,44)),('C',(13,34),(16,44),(12,40)),('C',(8,25),(8,33),(8,29)),('C',(24,14),(8,17),(15,12))],True)
        path('leaf',(24,14),[('C',(40,4),(24,6),(32,4)),('C',(24,14),(40,11),(32,14))],True);join('leaf','berry')
        path('center',(24,14),[('A',(30,22),6,8,True),('A',(24,30),6,8,True),('A',(18,22),6,8,True),('A',(24,14),6,8,True)],True);join('center','berry')
        path('left-seam',(8,25),[('C',(18,22),(12,30),(16,28))]);join('left-seam','berry');join('left-seam','center')
        path('right-seam',(38,22),[('C',(30,22),(38,30),(32,29))]);join('right-seam','berry');join('right-seam','center')
        path('lower-seam',(13,34),[('C',(24,30),(17,38),(22,36)),('C',(35,34),(26,36),(31,38))]);join('lower-seam','berry');join('lower-seam','center')
        line('bottom-seam',(24,30),(24,44));join('bottom-seam','center');join('bottom-seam','berry');join('bottom-seam','lower-seam')
