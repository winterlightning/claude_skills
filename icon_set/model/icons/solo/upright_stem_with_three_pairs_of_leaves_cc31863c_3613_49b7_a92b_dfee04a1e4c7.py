"""Upright spelt sprig. VRECT_M (10,4)-(38,44), mirrored leaf pairs
about x=24. Two pairs replace three to preserve open leaves at 48px. All
leaves share one shape definition and spacing. Lucide wheat supplies repeated
pointed grain construction; source supplies upright paired arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'cc31863c-3613-49b7-a92b-dfee04a1e4c7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/spelt_cc31863c-3613-49b7-a92b-dfee04a1e4c7.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'upright-stem-with-three-pairs-of-leaves'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Ear of Wheat Grain']
    keywords = ['stem','leaves','plant','spelt','foliage','sprig']
    def build(self):
        ys=(4,10,18,31,39,44)
        for i,(a,b) in enumerate(zip(ys,ys[1:])):self.add_line(f'stem-{i}',(24,a),(24,b))
        for i,y in enumerate((4,25)):
            names=[]
            self.add_bezier(f'pair-{i}-left-top',(24,y+6),((20,y),(14,y),(10,y)))
            self.add_bezier(f'pair-{i}-left-bottom',(10,y),((10,y+10),(18,y+14),(24,y+14)))
            self.add_bezier(f'pair-{i}-right-bottom',(24,y+14),((30,y+14),(38,y+10),(38,y)))
            self.add_bezier(f'pair-{i}-right-top',(38,y),((34,y),(28,y),(24,y+6)))
            names=[f'pair-{i}-'+part for part in ['left-top','left-bottom','right-bottom','right-top']]
            self.add_contour(f'pair-{i}',*names,closed=True)
            for part in ['left-top','right-top']:
                for k in [2*i,2*i+1]: self.relate('connect',f'pair-{i}-{part}',f'stem-{k}')
            for part in ['left-bottom','right-bottom']:
                for k in [2*i+1,2*i+2]: self.relate('connect',f'pair-{i}-{part}',f'stem-{k}')
        for i in range(4):self.relate('connect',f'stem-{i}',f'stem-{i+1}')
