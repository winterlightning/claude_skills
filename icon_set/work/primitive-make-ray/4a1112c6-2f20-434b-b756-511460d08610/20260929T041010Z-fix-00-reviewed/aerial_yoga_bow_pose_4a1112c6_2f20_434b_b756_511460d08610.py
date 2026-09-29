"""Rejected bent strokes no longer show the hanging fabric or recognizable reclined bow pose. Restore triangular suspension and a coherent folded body."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='4a1112c6-2f20-434b-b756-511460d08610'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__aerial-yoga-bow-pose/20260929T041010Z-thuan-mac/reference/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg'
AUTHOR='gpt-6'
PLAN='Rejected bent strokes no longer show the hanging fabric or recognizable reclined bow pose. Restore triangular suspension and a coherent folded body.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='aerial-yoga-bow-pose'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('head',38,37,4)
        self.add_bezier('torso',(26,37),((22,37),(28,32),(26,28)),((23,23),(6,22),(6,31)))
        self.path('bent-leg',(6,31),[('L',(6,37)),('A',(14,37),4,4,False),('L',(18,25))])
        self.path('sling',(18,25),[('L',(22,6)),('L',(28,27)),('C',(16,32),(29,33),(21,32))])
        self.relate('connect','torso','bent-leg');self.relate('connect','torso','sling');self.relate('connect','bent-leg','sling')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

# Human reference: icon_set/references/human_ref/full_body_ref.png.
# Detached circular head: nearest neck point is radius + 8 from center, leaving exactly 4 px ink clearance.
# Head (38,37), r4; neck (26,37); upper torso extends left.

Drawing.exception = {'reason': 'Preserve the suspended bow pose and tapered aerial fabric. The exact 4 px head-to-torso gap is analytic; the checker retains its curve warning. A 1 px envelope underfill and compact fabric/body spacing preserve the original pose.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': 'bd4a3bfa2a4241093aff767c03f1973ab4401288275aa83ed52b5adc244ccb47'}
