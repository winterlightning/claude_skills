"""Rejected triangles are squat, line is too short and the curved arrow is a heavy hook. Restore two mirrored triangles across a horizontal divider and a smooth right-side downward arc.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: refresh-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '80d9152e-7c3d-4bfe-8c06-1a9d8b17db38'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__downward-reflection-diagram/20260928T165531Z-thuan-mac/reference/reflect down_80d9152e-7c3d-4bfe-8c06-1a9d8b17db38.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Keep the mirrored triangles large enough to remain triangles. Their tips have 1px clear ink gaps to the divider, visibly separated at native size in both themes. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '58c14bd4261c9dac4776a8618e33697cf9bcc4e137d7cf123d9b4808ad9a4243'}
    icon_id = 'downward-reflection-diagram'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('reflect', 'down')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        poly('upper',(4,8),(28,8),(16,19),closed=True)
        poly('lower',(4,40),(28,40),(16,29),closed=True)
        line('mirror-axis',(4,24),(29,24))
        path('rotation',(35,12),[('C',(44,24),(41,12),(44,18)),('C',(35,36),(44,30),(41,36))])
        poly('head',(36,29),(35,36),(42,36));join('rotation','head')


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

