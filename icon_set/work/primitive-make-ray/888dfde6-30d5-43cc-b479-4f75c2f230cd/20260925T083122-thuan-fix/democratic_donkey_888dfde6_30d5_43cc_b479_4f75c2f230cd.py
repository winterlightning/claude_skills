"""Round the donkey muzzle and rump, preserve its upright ear and two clear legs.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: HRECT_L for the subject's natural orientation.
Construction: Lucide rabbit supports smooth animal silhouette; preserve the supplied donkey logo posture.
Reduction: No facial marks or hidden legs added; source silhouette retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '888dfde6-30d5-43cc-b479-4f75c2f230cd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__democratic-donkey/20260925T083122Z-thuan-mac/reference/election democrat_888dfde6-30d5-43cc-b479-4f75c2f230cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'democratic-donkey'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('election', 'democrat')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('donkey',(4,21),[('C',(10,14),(4,19),(8,17)),('L',(10,8)),('C',(17,14),(14,9),(16,10)),('C',(22,18),(19,16),(20,18)),('L',(34,18)),('C',(40,25),(38,18),(40,20)),('L',(40,40)),('L',(32,40)),('L',(31,29)),('L',(23,29)),('L',(22,40)),('L',(14,40)),('L',(14,25)),('L',(10,22)),('C',(4,21),(7,26),(4,25))],True)
        path('tail',(40,25),[('C',(44,32),(42,27),(43,30))]);join('tail','donkey')
