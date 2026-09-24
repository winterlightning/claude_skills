"""Blank circular face with broad curled cowboy brim and a smooth dipped crown, mirrored about x24.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: Shared human_ref/user.svg: circular head; source governs headwear. No useful Lucide cowboy match.
Omissions: No face details in source. Head-only subject has no head/body gap.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e7a439e2-504d-4cce-bf79-ba911a657a41'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face cowboy hat_e7a439e2-504d-4cce-bf79-ba911a657a41.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='blank-face-wearing-cowboy-hat'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('blank', 'face', 'wearing', 'cowboy', 'hat')
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

        # Circular jaw radius 16; the brim meets its endpoints at y26.
        self.add_arc('jaw',(8,26),(40,26),radius_x=16,sweep=False)
        path('brim',(6,16),[('C',(8,26),(6,21),(6,24)),('C',(40,26),(18,30),(30,30)),('C',(42,16),(42,24),(42,21))]);join('jaw','brim')
        path('crown',(12,20),[('L',(15,9)),('C',(18,6),(16,6),(17,6)),('C',(24,8),(20,6),(22,8)),('C',(30,6),(26,8),(28,6)),('C',(33,9),(31,6),(32,6)),('L',(36,20))])
        path('brim-top',(6,16),[('C',(12,20),(7,16),(9,19)),('C',(36,20),(20,24),(28,24)),('C',(42,16),(39,19),(41,16))]);join('brim-top','brim');join('brim-top','crown')
