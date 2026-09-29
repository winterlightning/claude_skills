"""card-game-card-club: Rebuilt the club with three broad rounded lobes, mirrored side bowls and a centered stem; removed the small shoulder kinks.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide club original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '620fba34-559d-44dd-802b-138529d208d8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__card-game-card-club/20260928T164600Z-thuan-mac/reference/card game card club_620fba34-559d-44dd-802b-138529d208d8.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'card-game-card-club'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('card', 'game', 'card', 'club')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for i,(kind,end,*args) in enumerate(steps):
                eid=f'{name}-{i}';members.append(eid)
                if kind=='L':self.add_line(eid,here,end)
                elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        def poly(name,*pts):self.add_polyline(name,*pts,closed=pts[0]==pts[-1])
        def join(a,b):self.relate('connect',a,b)

        path('club',(24,4),[('C',(32,12),(29,4),(32,7)),('C',(30,19),(32,15),(31,17)),('C',(40,27),(36,17),(40,21)),('C',(32,35),(40,32),(37,35)),('C',(24,31),(29,35),(26,33)),('C',(16,35),(22,33),(19,35)),('C',(8,27),(11,35),(8,32)),('C',(18,19),(8,21),(12,17)),('C',(16,12),(17,17),(16,15)),('C',(24,4),(16,7),(19,4))],True)
        line('stem',(24,31),(24,44));join('stem','club')
