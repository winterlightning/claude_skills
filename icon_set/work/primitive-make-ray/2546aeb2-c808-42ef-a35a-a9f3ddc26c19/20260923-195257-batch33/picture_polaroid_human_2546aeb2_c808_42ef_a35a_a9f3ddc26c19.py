from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='2546aeb2-c808-42ef-a35a-a9f3ddc26c19'
SOURCE_PATH='icon_set/work/todo-references/picture polaroid human_2546aeb2-c808-42ef-a35a-a9f3ddc26c19.svg'
AUTHOR='gpt-6'
PLAN='A portrait Polaroid in front of a tilted second print.'
OMISSIONS='Bust uses a circular detached head and broad shoulder arc; blank caption retained.'
LUCIDE_REFERENCE='user'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
class Drawing(Solo48):
    icon_id='picture-polaroid-human'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('picture', 'polaroid', 'human')

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
        # A portrait Polaroid in front of a tilted second print.

        self.box('front',6,6,28,36,3)
        self.add_polyline('rear',(34,13),(42,16),(37,42));self.relate('connect','rear','front')
        self.circle('head',20,18,3)
        self.add_arc('shoulders',(13,34),(27,34),radius_x=7,radius_y=5,sweep=True)
        self.add_line('caption',(6,34),(34,34));self.relate('connect','caption','front');self.relate('connect','shoulders','caption')
        # head bottom 21; shoulder top 29: 8 centerline / 4 ink gap.

