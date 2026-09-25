"""long-legged-ostrich: Broad feathered body, long curved neck, small round head and two long angular legs; natural side-view asymmetry.
Lucide construction: bird; original and atomic-debug inspected.
Omissions: Internal feather marks and eye omitted.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3cbe2f8-4bac-4bb2-9024-155482b37261'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ostrich_e3cbe2f8-4bac-4bb2-9024-155482b37261.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'long-legged-ostrich'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('long', 'legged', 'ostrich')
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

        path('body',(6,29),[('C',(18,20),(9,23),(13,20)),('C',(30,25),(23,20),(27,22)),('C',(32,32),(33,28),(35,32)),('L',(26,32)),('L',(18,32)),('C',(12,30),(15,32),(14,29)),('L',(6,29))],True)
        path('neck',(30,25),[('C',(36,12),(39,25),(36,18))]);join('neck','body')
        oval('head',36,9,3,3);join('head','neck')
        line('beak',(39,9),(42,10));join('head','beak')
        poly('leg-left',(18,32),(16,42),(21,42));poly('leg-right',(26,32),(30,42),(35,42));join('leg-left','body');join('leg-right','body')
