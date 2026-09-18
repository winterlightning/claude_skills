"""Build the defined container pairs; shared cached vector-geometry helpers.
Run: python3 -m icon_set.scripts.build_all_container_combinations
"""
from pathlib import Path
import base64,hashlib,json
from collections import Counter
from shapely.affinity import translate
from shapely.geometry import shape,box
from icon_set.scripts.container_placement import Artwork,artwork_group,root_svg
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,reject_effects,check_pair,vector_zone
from icon_set.scripts.suggest_container_sub_size import transform,recommendation
import xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'work/all-container-combinations'


def uri(text):return 'data:image/svg+xml;base64,'+base64.b64encode(text.encode()).decode()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

class PreparedSub:
    def __init__(self,art,size):
        self.ink=VectorInk.from_art(art,transform(size,[0,0]))
        self.inner=self.ink.envelope(2,False);self.outer=self.ink.envelope(2,True)
    def at(self,center):
        return PlacedSub(self,center)

class PlacedSub:
    def __init__(self,source,center):
        self.source=source;self.center=center;self.lines=translate(source.ink.lines,*center);self.error=source.ink.error
    def envelope(self,radius,outer):
        if radius!=2:raise ValueError('Prepared sub supports 4-unit strokes only')
        return translate(self.source.outer if outer else self.source.inner,*self.center)


def main():
    # Compatibility entry point: combinations are defined pairs, never a Cartesian product.
    from icon_set.scripts.build_paired_container_combinations import main as build_pairs
    return build_pairs()

if __name__=='__main__':main()
