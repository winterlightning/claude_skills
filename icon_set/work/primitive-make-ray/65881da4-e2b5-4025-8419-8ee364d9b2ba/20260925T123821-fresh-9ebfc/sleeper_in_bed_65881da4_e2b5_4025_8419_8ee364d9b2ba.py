'Sleeping head and rounded blanket above a two-rail bed with posts.'
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='65881da4-e2b5-4025-8419-8ee364d9b2ba'
SOURCE_PATH='pictographic-primitives/hotels/hotel bed_65881da4-e2b5-4025-8419-8ee364d9b2ba.svg'
AUTHOR='gpt-6'
PLAN='Sleeping head and rounded blanket above a two-rail bed with posts.'
CONSTRUCTION_REFERENCE='human_ref/full_body_ref.png: circular head; Lucide bed-single: separate mattress rail and posts.'
class Drawing(Solo48):
    icon_id='sleeper-in-bed'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('hotel', 'bed')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.circle('head',16,15,4)
        self.path('blanket',(28,15),[('L',(36,15)),('A',(44,23),8,8,True),('L',(44,28)),('L',(28,28)),('L',(28,15))],True)
        self.add_polyline('left-post',(4,8),(4,28),(4,36),(4,40))
        self.add_polyline('right-post',(44,23),(44,28),(44,36),(44,40))
        self.add_line('upper-rail',(4,28),(28,28));self.add_line('lower-rail',(4,36),(44,36))
        for a,b in [('left-post','upper-rail'),('left-post','lower-rail'),('right-post','lower-rail'),('right-post','blanket'),('upper-rail','blanket')]:self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='blanket-0',torso_junction='start')

# Keyshape: HRECT_L fits the horizontal sleeper, mattress band and bedposts.
# Visual review: Restored the blanket front edge and separate mattress band; head and blanket align horizontally.
OMISSIONS='No defining components omitted; smooth blanket volume and two mattress rails retained.'
HUMAN_REVIEW={'reference': 'icon_set/references/human_ref/full_body_ref.png', 'head_center': [16, 15], 'radius': 4, 'torso_junction': [28, 15], 'centerline_gap': 8, 'ink_gap': 4, 'proof': '28-(16+4)=8. Horizontal blanket top continues the resting head axis.'}
