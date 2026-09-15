from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-failed-batch-100/before.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
notes={
1:'The bent rifle arm and forward leg remain distinct at native size; preserve the firing pose.',
2:'The tapered aircraft wing retains a readable opening and flat tip; preserve its silhouette.',
3:'The far wing approaches the tail shoulder but stays readable as a separate branch of the aircraft.',
4:'The far wing and tail shoulder have a visible gap; retain the takeoff silhouette.',
5:'The two inner lobes intentionally converge around the central circular ornament; both sides remain readable.',
7:'The head and shoulder curves meet as one bust; retain the visible continuous contact.',
8:'The apple stalk curls back over its attached fruit; the stalk remains clear at native size.',
9:'The raised ear approaches the shell without losing the ear outline or the shell contour.',
10:'The converging strokes form the intended narrow upper stem of the numeral four; preserve the numeral.',
11:'The diagonal scarf joins the shoulder and remains a clear clothing cue.',
12:'The rim and tub converge at their right attachment; the bowl opening is still readable.',
13:'The loose strand departs the yarn ball tangentially; its external tail remains distinct.',
14:'The bamboo leaf narrows into its stalk attachment; the leaf counter remains open.',
15:'The two diagonal lightning strokes form a compact zigzag with a readable turn.',
19:'The short mouth stroke sits inside the rounded jaw end; preserve the simple dinosaur profile.',
20:'The arm and upper leg converge around the bent torso; preserve the compact board-riding pose.',
21:'The page curve joins the spine while the book and page opening remain legible.',
22:'The leaning book narrows toward the right shelf wall; the two books remain recognizable.',
23:'The short brain stem narrows below the brain; preserve the broad brain silhouette and stem cue.',
25:'The crest and inside curl converge at the breaking wave tip; the main curl stays open.',
27:'The dinosaur tail tapers deliberately to a short point; its legs and belly remain clear.',
29:'The raised shutter button attaches beside the sloping camera shoulder; preserve both features.',
30:'The side viewfinder and sloping shoulder form a compact stepped camera top.',
32:'The suspended ball is close to its bent support but remains circular and distinguishable.',
34:'The smile boundary and short interior mouth divider meet as a readable smiling mouth.',
35:'The bent arm approaches the seated torso; preserve the small seated pose and potty silhouette.',
36:'The lower branch narrows toward the ring attachment; the astrological symbol remains recognizable.',
37:'The far wing and tail shoulder converge as the airliner silhouette turns; retain the recognizable wing layout.',
38:'The angular upper wing and tail close form a taper; preserve the rounded-nose aircraft.',
39:'The beak hook and chin merge locally at the mouth; the open bird profile remains readable.',
40:'The neighboring gear flanks narrow into a deliberate tooth valley; the center hole stays open.',
41:'The wrench neck narrows into the open jaw; both working ends stay recognizable.',
43:'The crank bend approaches the handle end; preserve the stepped crank and closed grip.',
44:'The hanging ball and moon approach each other but retain distinct shapes.',
45:'The bent arm approaches the angled torso; retain the skier’s pose and pole.',
46:'The tail curves into the mouse body as a continuous animal silhouette.',
47:'The sail base and board run close near their attachment; the sail remains a distinct large triangle.',
48:'The crystal ball rests on its stand with overlapping ink at the contact; preserve the seated orb.',
49:'The raised thumb tapers between its inner and outer curves; preserve the recognizable thumbs-up.',
50:'The bent arm and torso remain distinguishable above the separate wheels.',
51:'The jagged tear intentionally converges into the box corner; preserve the damaged-box cue.',
52:'The curved arrow shaft merges into the arrowhead; preserve the broad head and motion dashes.',
53:'The cylinder rim and side meet at a curved corner; the database remains a readable cylinder.',
55:'The folded thumb meets the handshake outline; the central grasp remains recognizable.',
56:'The adult’s bent arm meets the infant’s body at the supported contact; preserve the care scene.',
57:'The body stroke approaches the wheel at the seated hip; retain the recognizable wheelchair silhouette.',
58:'The flag pole passes into the buoy attachment; preserve the marker’s physical connection.',
59:'The dog’s angular rear leg tapers toward the paw; the carried ball and body remain readable.',
60:'The dog’s bent rear leg narrows at its turn; preserve the jumping pose and large hoop.',
61:'The dog head and recovery cone approach at the neck attachment; the cone stays recognizable.',
62:'The dolphin body tapers naturally into the tail; the hoop remains separate and clear.',
63:'The bus window row meets a rounded body corner; the two decks and wheels remain clear.',
64:'The bent leg meets the ski at the boot; preserve the downhill stance.',
65:'The lip meets the rounded mouth at its left side; the mouth opening and drool stroke remain legible.',
66:'The short tail tapers into the duck body; preserve the bird’s outline above the water.',
67:'The lower scoop curves into the duck belly as intentional connected ink.',
68:'The beak and forehead converge into the hooked beak; preserve the eagle’s pointed facial silhouette.',
69:'The bent forearm narrows around the elbow; preserve the deity’s pose beneath the sun disk.',
70:'The slanted and vertical strokes converge into the numeral four; the 404 label remains readable.',
71:'The vest centerline meets the circular device attachment; the vest and its central detail stay clear.',
72:'The inner eye contour and short crossbar form the compact eye-strain cue.',
74:'The bent arm and torso converge at the shoulder; preserve the fast-running pose.',
76:'The thumb turns into the palm at the grip; the pointing finger and ballot option remain distinct.',
77:'The diagonal thumb narrows toward the hand outline; retain the touching gesture.',
78:'The pole meets the moon surface; preserve the planted-flag contact.',
79:'The flag pole meets the round float; the circular buoy and flag remain legible.',
80:'The pole continues into the elliptical golf hole; preserve the planted-flag construction.',
81:'The wing fold narrows into the neck; the flying-bird silhouette stays readable.',
82:'The triangular fin narrows into the rocket body; the fin and body remain distinct.',
83:'The bike frame joins the wheel near the hub area; both wheels and folding frame stay recognizable.',
84:'The blade back and heel taper at the pivot; preserve the folding-knife blade.',
87:'The short fossil spine and branch converge as a connected skeletal mark.',
88:'The filler opening turns into its neck attachment; the removed cap remains separate and clear.',
89:'The handle loop touches the lamp bowl; the lamp retains an open handle and long spout.',
90:'The glove’s outer finger and palm merge at the knuckle; the finger outline remains clear.',
91:'The gripping thumb approaches the chip edge while the chip and hand remain recognizable.',
92:'The axe neck and closed fist meet at the held handle; preserve the tool grip.',
94:'The fingertips meet the heart’s lower side; preserve the hand supporting the heart.',
95:'The curled thumb meets the outside of the hand beside the remote; the remote remains readable.',
96:'The wrist stroke approaches the phone corner at the grip; preserve the held-device silhouette.',
97:'The wrist meets the phone near its lower corner; the home indicator remains separate.',
98:'The two grip runs share a horizontal ink segment as part of the clenched hand.',
99:'The thumb outline merges along its short return into the palm; preserve the pointing gesture.',
100:'The narrow handle tapers at the saw’s grip; the blade teeth and handle remain readable.'
}
rows=json.loads((W/'before.json').read_text());repairs={r['number']:r for r in json.loads((W/'repairs.json').read_text())}
records={'version':1,'scope':'Visual review of the first 100 failed solo icons, 2026-09-15. User requested retaining good drawings with opposing-edge advisories.','icons':{}}
log=[]
for n,row in enumerate(rows,1):
 if n in repairs:
  log.append(dict(number=n,icon_id=row['id'],decision='reconstructed',replacement=repairs[n]['icon_id'],reason='Shared-ink reconstruction.' if n not in (26,33) else 'Opened the small enclosed counter.'));continue
 assert n in notes,n
 icon=create(row['id']);metric=json.loads((ROOT/'icon_set/dist/qa/solo'/row['id']/'metrics.json').read_text())
 svg_hash=hashlib.sha256(icon.to_svg().encode()).hexdigest();assert svg_hash==metric['svg_sha256']
 assert not metric['errors'] and metric['negative_space']['status']=='pass'
 findings=metric['internal_spacing']['findings'];assert findings
 record=dict(svg_sha256=svg_hash,rules_sha256=metric['rules_sha256'],elements=[f['elements'] for f in findings],reviewer=AUTHOR,reason=notes[n],evidence=f'icon_set/work/solo-failed-batch-100/centerlines-{(n-1)//20+1}.png',reviewed_at='2026-09-15')
 records['icons']['solo/'+row['id']]=record
 log.append(dict(number=n,icon_id=row['id'],decision='retain-reviewed-advisory',reason=notes[n],finding= row['issues'][0]['text']))
(ROOT/'icon_set/model/contracts/spacing-reviews.v1.json').write_text(json.dumps(records,indent=2)+'\n')
(W/'review-decisions.json').write_text(json.dumps(log,indent=2)+'\n')
print(len(records['icons']),'specific drawing reviews recorded')
