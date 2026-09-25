"""looped-swan: A curved-neck swan with a long low hull and curled wing; continuous neck and body curves replace short kinks.
Lucide construction: bird; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd24dfd19-25bb-41c4-b523-eaaa8900e241'
SOURCE_PATH = 'pictographic-primitives/animals/swan_d24dfd19-25bb-41c4-b523-eaaa8900e241.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-swan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('looped', 'swan')
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

        path('outline',(24,16),[('C',(33,6),(24,10),(28,6)),('C',(42,16),(39,6),(42,10)),('L',(34,16)),('C',(38,27),(31,20),(34,23)),('C',(42,34),(40,29),(42,31)),('C',(24,42),(42,40),(32,42)),('C',(6,32),(14,42),(6,38)),('C',(15,24),(6,28),(10,24)),('C',(24,26),(19,24),(22,25)),('C',(24,16),(25,23),(24,20))],True)
        path('wing',(24,26),[('C',(16,32),(27,30),(22,32))]);join('wing','outline')
