"""Police Officer with Helmet Badge.

Symbol plan: Domed police helmet with a small badge above a circular jaw and broad uniform shoulders with a central seam.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted. Badge reduced to a single bold mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '4bbaab36-8c19-44c4-b3ea-0dedb49bed05'
SOURCE_PATH = 'pictographic-primitives/avatars/police man_4bbaab36-8c19-44c4-b3ea-0dedb49bed05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'police-officer-with-helmet-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('police', 'officer', 'uniform', 'hat', 'person', 'portrait', 'security', 'law enforcement')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('helmet-left',(10,21),(24,4),14,17)
        arc('helmet-right',(24,4),(38,21),14,17)
        join('helmet','helmet-left','helmet-right')
        path('brim',(10,21),(12,21),(36,21),(38,21));connect('helmet','brim')
        arc('face',(36,21),(12,21),12);connect('face','brim');connect('face','helmet')
        self.add_dot('badge',(24,13))
        bottom=33

        top = bottom + HEAD_BODY_CENTERLINE_GAP
        line('body-left-side',(8,44),(8,42))
        arc('body-left-shoulder',(8,42),(18,top),10,42-top)
        join('body-left','body-left-side','body-left-shoulder')
        line('body-top',(18,top),(24,top))
        line('body-top-right',(24,top),(30,top))
        arc('body-right-shoulder',(30,top),(40,42),10,42-top)
        line('body-right-side',(40,42),(40,44))
        join('body-right','body-right-shoulder','body-right-side')
        connect('body-left','body-top');connect('body-top','body-top-right');connect('body-top-right','body-right')
        connect('face','body-top');connect('face','body-top-right')

        line('body-seam',(24,top),(24,44));connect('body-seam','body-top');connect('body-seam','body-top-right')
