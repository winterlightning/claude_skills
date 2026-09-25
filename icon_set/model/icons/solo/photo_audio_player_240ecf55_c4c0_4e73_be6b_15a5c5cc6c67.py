from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='240ecf55-c4c0-4e73-be6b-15a5c5cc6c67'
SOURCE_PATH='icon_set/work/todo-references/photo audio player_240ecf55-c4c0-4e73-be6b-15a5c5cc6c67.svg'
AUTHOR='gpt-6'
PLAN='An audio-player picture with a waveform above a playback track.'
OMISSIONS='Waveform amplitude reduced; tiny slider handle omitted to keep playback track clear.'
LUCIDE_REFERENCE='audio-lines'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='photo-audio-player'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'medias'
    categories = ('primitives', 'medias')
    aliases=()
    keywords=('photo', 'audio', 'player')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def handset(self):
        # One coherent side-profile receiver: round outer sweep and two ear pads.
        self.add_bezier('receiver',(9,6),((6,6),(6,12),(6,15)),((6,26),(22,42),(33,42)),((37,42),(42,40),(42,37)),((42,35),(36,30),(34,30)),((32,30),(30,34),(28,32)),((22,28),(19,25),(16,20)),((14,17),(19,15),(19,12)),((19,10),(12,6),(9,6)))

    def build(self):
        # An audio-player picture with a waveform above a playback track.

        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_polyline('wave',(14,18),(18,14),(23,18),(28,14),(34,18))
        self.add_line('division',(6,26),(42,26));self.relate('connect','division','frame')
        self.add_line('track',(15,34),(33,34))

