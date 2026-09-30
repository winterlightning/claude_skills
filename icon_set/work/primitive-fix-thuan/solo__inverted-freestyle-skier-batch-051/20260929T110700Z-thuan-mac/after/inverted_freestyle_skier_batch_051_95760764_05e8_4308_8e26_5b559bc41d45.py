'Lengthened the two skis, attached the bent legs explicitly and retained the upside-down head and extended pole arm.\nOriginal/current comparison: The rejected skis are tiny disconnected bars and read like a ladder beside the bent legs.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/full_body_ref.png: circular head and coherent limbs; inverted exact gap (38-4)-26=8 centerline/4 ink, aligned with actual upper torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '95760764-05e8-4308-8e26-5b559bc41d45'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inverted-freestyle-skier-batch-051/20260929T110700Z-thuan-mac/reference/free skiiing 1_95760764-05e8-4308-8e26-5b559bc41d45.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'inverted-freestyle-skier-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('inverted', 'freestyle', 'skier', 'batch', '051')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        circle('head',28,38,4)
        line('torso',(28,26),(28,22))
        poly('leg-one',(28,22),(20,12),(14,12),(6,12))
        poly('leg-two',(28,22),(20,24),(14,24))
        poly('ski-one',(6,6),(6,12),(6,30))
        poly('ski-two',(14,6),(14,12),(14,24),(14,30))
        poly('arm',(28,26),(42,22),(42,6))
        for n in ('leg-one','leg-two','arm'):join('torso',n)
        join('leg-one','leg-two');join('ski-one','leg-one');join('ski-two','leg-one');join('ski-two','leg-two')
        self.mark_human_figure('skier',head='head',torso='torso',torso_junction='start')
