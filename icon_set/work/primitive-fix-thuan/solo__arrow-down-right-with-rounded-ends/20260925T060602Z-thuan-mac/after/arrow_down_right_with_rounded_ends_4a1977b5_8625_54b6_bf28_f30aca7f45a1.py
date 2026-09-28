"""Outlined diagonal arrow with eight-unit arms and rounded terminals."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4a1977b5-8625-54b6-bf28-f30aca7f45a1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-down-right-with-rounded-ends/20260925T060602Z-thuan-mac/reference/arrow thick corner bottom right_4a1977b5-8625-54b6-bf28-f30aca7f45a1.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'arrow-down-right-with-rounded-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('arrow thick corner bottom right',)

    def build(self):
        # Symbol plan: Outlined diagonal arrow with eight-unit arms and rounded terminals.
        # Construction reference: Lucide move-down-right; original supplied subject controls meaning.

        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('arrow',(7,14),[('A',(15,8),5,5,True),('L',(34,30)),('L',(34,10)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(10,34),4,4,True),('L',(22,34)),('L',(7,14))],True)
