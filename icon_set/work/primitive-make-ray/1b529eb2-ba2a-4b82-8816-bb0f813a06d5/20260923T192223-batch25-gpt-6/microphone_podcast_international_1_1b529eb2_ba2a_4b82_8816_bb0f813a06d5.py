"""A globe above a microphone represents international podcasting.
Construction reference: mic and globe.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1b529eb2-ba2a-4b82-8816-bb0f813a06d5'
SOURCE_PATH = 'icon_set/work/todo-references/microphone podcast international 1_1b529eb2-ba2a-4b82-8816-bb0f813a06d5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'microphone-podcast-international-1'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('microphone', 'podcast', 'international', '1')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: upper globe with two meridians, lower capsule microphone and U support.
        self.add_arc('globe-top',(8,20),(40,20),radius_x=16)
        self.add_bezier('globe-left',(10,28),((8,25),(8,22),(8,20)))
        self.add_bezier('globe-right',(40,20),((40,22),(40,25),(38,28)))
        self.add_contour('globe','globe-left','globe-top','globe-right')
        self.add_line('equator',(8,20),(40,20))
        self.add_bezier('meridian-left',(18,5),((15,9),(15,14),(15,20)))
        self.add_bezier('meridian-right',(30,5),((33,9),(33,14),(33,20)))
        self.rect('microphone',20,24,8,12,r=4)
        self.add_polyline('stand',(24,40),(24,44),(32,44))
        self.add_line('base-left',(16,44),(24,44))
        self.relate('connect','stand','base-left')
        self.add_line('support-left',(12,30),(12,32))
        self.add_arc('support-bowl',(12,32),(36,32),radius_x=12,radius_y=8,sweep=False)
        self.add_line('support-right',(36,32),(36,30))
        self.add_contour('support','support-left','support-bowl','support-right')
        self.relate('connect','support','stand')
