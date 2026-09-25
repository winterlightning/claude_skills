"""dill: A gently leaning herb stem owns four alternating, smoothly swept branch attachments; natural asymmetry retained.
Lucide construction: sprout; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ed3fa5b-9e28-4066-bff3-a2cb767df09d'
SOURCE_PATH = 'pictographic-primitives/food/dill_4ed3fa5b-9e28-4066-bff3-a2cb767df09d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'dill'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('dill',)
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('stem',(24,44),[('C',(24,34),(24,40),(24,37)),('C',(25,24),(24,30),(24,27)),('C',(28,14),(26,20),(27,17)),('C',(33,4),(29,10),(31,7))])
        path('left-low',(24,34),[('C',(12,27),(17,34),(13,31))]);join('left-low','stem')
        path('right-low',(24,34),[('C',(40,24),(33,34),(39,30))]);join('right-low','stem');join('left-low','right-low')
        path('left-high',(25,24),[('C',(8,12),(16,24),(9,18))]);join('left-high','stem')
        path('right-high',(28,14),[('C',(40,7),(35,14),(39,10))]);join('right-high','stem')
