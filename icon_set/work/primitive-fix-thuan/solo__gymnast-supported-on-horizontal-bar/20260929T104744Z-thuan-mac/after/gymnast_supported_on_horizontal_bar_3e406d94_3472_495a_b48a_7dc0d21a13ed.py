"""gymnastics acrobatic hanging person.
Symbol plan: VRECT_L centerline (8,4)-(40,44). Two posts and split bar share nodes at y24; circular head center24,10 r6; torso begins24,24 for exactly8 centerline /4 ink head gap. Narrowly separated legs retain a straight hanging pose.
Shared human_ref/full_body_ref.png for round head and simple limb strokes; supplied original for straight hanging posture and high support posts.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3e406d94-3472-495a-b48a-7dc0d21a13ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gymnast-supported-on-horizontal-bar/20260929T104744Z-thuan-mac/reference/gymnastics acrobatic hanging person_3e406d94-3472-495a-b48a-7dc0d21a13ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gymnast-supported-on-horizontal-bar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('gymnast', 'supported', 'on', 'horizontal', 'bar')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)


        circle('head',24,10,6)
        for n,x in [('left',8),('right',40)]:
            line(n+'-upper',(x,4),(x,24))
            line(n+'-lower',(x,24),(x,44))
            connect(n+'-upper',n+'-lower')
        line('bar-left',(8,24),(24,24));line('bar-right',(24,24),(40,24))
        for a,b in [('left-upper','bar-left'),('left-lower','bar-left'),('right-upper','bar-right'),('right-lower','bar-right'),('bar-left','bar-right')]:connect(a,b)
        line('torso',(24,24),(24,32));connect('torso','bar-left');connect('torso','bar-right')
        line('leg-left',(24,32),(20,44));line('leg-right',(24,32),(28,44))
        connect('torso','leg-left');connect('torso','leg-right');connect('leg-left','leg-right')
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')

