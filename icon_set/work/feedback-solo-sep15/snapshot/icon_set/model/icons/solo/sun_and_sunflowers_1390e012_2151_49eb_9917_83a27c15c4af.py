"""A half sun hangs above two unequal sunflower heads on stems. HRECT extremes (4,8)-(44,40); each flower owns its radius, four attached rays, and stem.
Reduction: Reduced toothed heads to four cardinal petal rays, omitted the sun rays, and retained one open leaf on the larger flower.
Lucide construction: sun, flower
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1390e012-2151-49eb-9917-83a27c15c4af'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors sun plants_1390e012-2151-49eb-9917-83a27c15c4af.svg'
AUTHOR = 'gpt-6'


class SunAndSunflowers(Solo48):
    icon_id = 'sun-and-sunflowers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('sun', 'sunflower', 'flowers', 'plants', 'garden', 'summer', 'outdoors', 'growth')

    def build(self) -> None:
        self.add_arc("sun",(4,16),(20,16),radius_x=8)
        self.add_line("horizon",(20,16),(4,16))
        self.add_contour("half-sun","sun","horizon",closed=True)
        for i,(cx,cy,r,extension) in enumerate(((10,32,4,2),(34,24,6,4))):
            nodes=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
            members=[]
            for j,a in enumerate(nodes):
                n=f"flower-{i}-{j}";self.add_arc(n,a,nodes[(j+1)%4],radius_x=r);members.append(n)
            self.add_contour(f"disc-{i}",*members,closed=True)
            ends=[(cx,cy-r-extension),(cx+r+extension,cy),(cx,40),(cx-r-extension,cy)]
            for j,(a,b) in enumerate(zip(nodes,ends)):
                n=f"ray-{i}-{j}";self.add_line(n,a,b)
                self.relate("connect",n,members[j]);self.relate("connect",n,members[(j-1)%4])
            if i==1:
                self.add_line(f"leaf-{i}",(cx,40),(42,36))
                self.relate("connect",f"leaf-{i}",f"ray-{i}-2")
