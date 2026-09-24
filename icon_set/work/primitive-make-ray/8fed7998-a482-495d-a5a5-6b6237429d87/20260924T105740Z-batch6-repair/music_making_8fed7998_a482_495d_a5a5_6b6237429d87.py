"""music making: standalone SOLO48 repair.
Plan: Person at left gestures toward paired notes at right.
Keyshape: SQUARE; shared dimensions and nodes own repeated elements.
Reduction: Shifted the figure left and spaced the notes; outlined torso reduced to coherent strokes.
Lucide originals and atomic-debug construction reference: music.
human_ref/full_body_ref.png: head center (14,12), radius 6, torso starts (14,26); 26-(12+6)=8 centerline units and 4 ink units. Torso and head share x=14; figure flag recorded.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8fed7998-a482-495d-a5a5-6b6237429d87'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/music making_8fed7998-a482-495d-a5a5-6b6237429d87.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='music-making'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('music', 'making')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.circle('head',14,12,6)
        self.add_line('torso',(14,26),(14,42))
        self.add_bezier('left-shoulder',(6,42),((6,30),(6,26),(14,26)))
        self.add_polyline('arm',(14,26),(26,34),(42,34))
        self.relate('connect','torso','left-shoulder');self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.circle('note-left',28,20,2);self.circle('note-right',40,20,2)
        self.add_polyline('beam',(30,20),(30,8),(42,6),(42,20))
        self.relate('connect','beam','note-left');self.relate('connect','beam','note-right')

