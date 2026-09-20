from pathlib import Path
import json,re
P=Path(__file__).parent
raw='''0|Two Overlapping Busts with Oval Heads|Two human busts stand side by side with separate upright oval heads and broad curved shoulders. The left torso overlaps the right one, and both figures end along the same flat baseline.|people,couple,bust,shoulders,pair,spouse
2|Upright Sprinkler with Arcing Water Jets|A sprinkler rises on a narrow upright stem above a low rounded base. A shallow nozzle bowl sits at the top, with four curved water jets spreading outward around a central upright stream.|sprinkler,water,jets,nozzle,garden,irrigation
3|Left-Facing Woman with Swept Long Hair|A woman's head faces left with a plain profile, small nose and closed lips. A swept inner hairline curves from the forehead toward the back, while long hair tapers behind the neck.|woman,profile,hair,head,portrait,person
4|Ascending Staircase Side Outline|A staircase climbs from lower left to upper right through four flat steps and upright risers. A long horizontal base extends beneath it, while the highest landing continues rightward above the open side.|stairs,steps,staircase,ascent,building,architecture
5|Long Drinking Straw with Angled Bend|A long slender drinking straw rises at a slight diagonal before bending toward the upper right. Its short upper section angles more sharply than the lower stem, with a softened elbow between them.|straw,drink,bend,tube,beverage,utensil
6|Five Staggered Masonry Blocks|Five rectangular masonry blocks form three courses, with two blocks above and below a single centered block. The offset middle course leaves open recesses at both sides of the small wall fragment.|masonry,blocks,stonework,wall,brick,construction
7|Rounded Masonry Panel with Staggered Joints|A rectangular masonry panel has rounded outer corners and three horizontal courses. Offset vertical joints divide the upper and lower courses into two blocks and the middle course into three.|masonry,wall,blocks,stucco,brick,construction
8|Round Sun with Eight Separate Rays|A plain circular sun sits at the center of eight detached straight rays. Four rays point vertically and horizontally, while four shorter diagonal rays fill the spaces between them.|sun,rays,sunbeam,daylight,weather,sky
10|Church Steeple with Sloping Side Wings|A tall church tower supports a sharply pointed spire above a plain rectangular body. A narrow arched opening marks the tower front, and low sloping side wings spread outward from its base.|steeple,church,tower,spire,building,architecture
11|Round Waffle with Square Grid|A round waffle has straight horizontal and vertical grooves crossing its face in a square grid. The outer circular edge clips the corner cells, leaving a broad centered pattern without any separate topping.|waffle,stroopwafel,biscuit,grid,food,dessert
12|Closed Carton with Front Tape Tab|A closed carton has a broad rectangular front with rounded lower corners and a shallow trapezoidal top. A short central tape tab folds over the top edge onto the otherwise plain front face.|carton,box,package,tape,storage,container
13|Lidded Cooking Pot above Gas Flame|A deep cooking pot has a flat lid, a rounded knob and short side handles. A separate three-point flame burns directly beneath its rounded base, forming a simple pot-over-burner cooking scene.|pot,lid,flame,cooking,gas,kitchen
14|Lidded Pot above Heating Marks|A deep lidded pot with a rounded knob and two short side handles sits above a row of upright heating marks. A short horizontal cooking-surface line runs beneath the marks.|pot,lid,heat,induction,cooking,kitchen
15|Crescent Moon beside Five-Point Star|A broad crescent moon curves around an open space on its right, ending in two sharp tips. A separate five-pointed star sits between the tips, above the center of the crescent.|crescent,moon,star,emblem,sky,symbol
16|Rounded Horizontal Strip with Diagonal Bands|A long horizontal strip has rounded ends and three diagonal interior seams sloping upward to the right. The seams divide its plain face into alternating broad slanted sections within one continuous border.|strip,band,stripes,diagonal,rectangle,pattern
17|Diagonal Pencil above Short Written Line|A pencil lies diagonally from a sharp lower-left tip to a rounded upper-right end. Seams separate the pointed nib and short end cap, while a short horizontal written line sits below.|pencil,stylus,writing,stationery,nib,line
19|Front-Facing Woman with Flared Shoulder-Length Hair|A woman faces forward with a blank face framed by shoulder-length hair that flares outward at the ends. A central part rises above the forehead, and a rounded neckline joins the shoulders below.|woman,portrait,hair,bust,neckline,person
21|Front-Facing Woman with Rounded Bob|A blank-faced woman has a broad rounded bob that ends just above her shoulders. The hair parts at the center of her forehead, and a long neck descends into a rounded neckline.|woman,bob,hair,portrait,bust,person
22|Short-Haired Woman with Visible Sleeve Seams|A front-facing woman has a blank face beneath short hair with a slightly off-center part. Her rounded neckline meets a broad torso with two short vertical sleeve seams and a flat lower edge.|woman,bust,hair,sleeves,portrait,person
25|Curved Stocking with Broad Folded Cuff|A stocking hangs upright with a broad rounded cuff and a foot curving toward the lower left. A curved heel patch sits along the right edge where the leg narrows into the foot.|stocking,sock,cuff,heel,footwear,clothing
26|Complete Five-Point Star Outline|A complete five-pointed star has one upright point, two wide side points and two lower tips. Its inward corners are slightly softened, and the enclosed face is entirely blank.|star,outline,shape,five point,emblem,symbol
27|Bee with Spread Wings and Striped Abdomen|A bee faces upward with two antennae, a round head and a broad central thorax. Two wings spread sideways above thin bent legs, while horizontal bands cross its pointed lower abdomen.|bee,insect,wings,antennae,stripes,animal
28|Thick Steak with Oval Bone Center|A thick steak has an uneven rounded upper face with a narrow end projecting toward the lower left. An oval bone sits near the wider end, and a curved lower edge shows the cut's thickness.|steak,meat,bone,food,cut,beef
29|Front-Facing Train on Short Rails|A front-facing train has a tall rounded body, broad windshield and two circular lower headlights. A narrow roof band crosses its top, while two slanting rails and a cross-tie extend beneath it.|train,rail,headlights,transport,railway,vehicle
30|Long-Handled Pan above Open Flame|A shallow pan extends to the right of a long straight handle, with rounded lower corners beneath its flat rim. A three-point flame sits directly below the bowl as a cooking heat source.|pan,handle,flame,cooking,kitchen,gas
31|Diagonal Carrot with Three Leaf Stems|A carrot tapers toward the lower left from a broad rounded shoulder at upper right. Two short diagonal creases cross its body, and three curved leaf stems rise from the top.|carrot,vegetable,root,food,leaves,produce
32|Horizontal Strap with Broad Rounded End|A long horizontal strap has a rounded left end and a larger upright rounded terminal at the right. The terminal overlaps the narrow band, and both sections have entirely plain interiors.|strap,band,fastener,end,accessory,clothing
33|Small Gabled House with Square Window|A small house has a broad triangular roof projecting beyond its straight side walls. A single square window sits in the center of the plain front, above a level lower edge.|house,studio,roof,window,building,architecture'''
D={}
for line in raw.splitlines():
 i,n,d,t=line.split('|');i=int(i);D[i]=dict(index=i,concept=n,icon_id=re.sub('[^a-z0-9]+','-',n.lower()).strip('-'),family='solo',description=d,tags=t.split(','))
import sys
sys.path.insert(0,str(P.resolve().parents[2]))
from icon_set.model.icons.registry import families,icons_in
ids={i.icon_id for f in families() for i in icons_in(f)}
for f in P.parent.glob('todo-solo-briefs-*/sources/manifest.json'):
 if f.parent.parent!=P:ids.update(x['icon_id'] for x in json.loads(f.read_text()))
(P/'existing-ids.json').write_text(json.dumps(sorted(ids)))
print('solo',len(D),'collisions',[(i,d['icon_id']) for i,d in D.items() if d['icon_id'] in ids]);print('lengths',[(i,len(d['description'].split())) for i,d in D.items() if not 25<=len(d['description'].split())<=45])
(P/'solo-drafts.json').write_text(json.dumps(D,indent=2)+'\n')
