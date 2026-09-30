from author import make,ROOT
import json
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(6,'VRECT_L',N[5]+ ' Rebalance bow to a wider, shallower form and taper the jacket sides.','''
poly('bow-left',(8,4),(24,10),(8,16),closed=True)
poly('bow-right',(40,4),(24,10),(40,16),closed=True);join('bow-left','bow-right')
poly('lapels',(8,16),(24,36),(40,16));join('lapels','bow-left');join('lapels','bow-right')
path('jacket',(8,16),[('L',(8,24)),('L',(13,44)),('L',(35,44)),('L',(40,24)),('L',(40,16))]);join('jacket','bow-left');join('jacket','bow-right');join('jacket','lapels')
line('seam',(24,36),(24,44));join('seam','jacket');join('seam','lapels')
''','Shared center axis and mirrored bow/lapels; no useful exact Lucide match.')
make(7,'SQUARE',N[6]+ ' Enlarge both heads and slope the outside arms while keeping symmetric joined hands.','''
for x in [14,34]:
 circle(f'head-{x}',x,11,5)
 line(f'torso-{x}',(x,24),(x,33))
 poly(f'legs-{x}',(x-6,42),(x,33),(x+6,42));join(f'torso-{x}',f'legs-{x}')
 self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
poly('arms',(6,29),(14,24),(24,31),(34,24),(42,29))
join('arms','torso-14');join('arms','torso-34')
''','human_ref/full_body_ref.png: equal radius5 heads, lower16 to neck24 gives exact4 ink gap; mirrored anatomy.')
make(8,'SQUARE',N[7]+ ' Restore parted bangs in both heads and a curled ponytail on the lower child.','''
circle('upper-head',16,16,10)
poly('upper-hair',(6,16),(10,16),(16,12),(22,16),(26,16));join('upper-hair','upper-head')
circle('lower-head',30,32,10)
poly('lower-hair',(20,32),(24,32),(30,28),(36,32),(40,32));join('lower-hair','lower-head')
join('upper-head','lower-head')
path('ponytail',(36,24),[('C',(42,18),(36,16),(40,14))]);join('ponytail','lower-head')
''','human_ref/user.svg circular head proportions; source offset pair and parted hair.')
make(9,'HRECT_L',N[8]+ ' Use two equal circular outlines with a broad central overlap.','''
circle('left',20,24,16)
circle('right',28,24,16)
join('left','right')
''','Two equal radius16 circles on a shared horizontal axis. Actual circle crossings form the central lens.')
make(10,'SQUARE',N[9]+ ' Round the front corners and restore a rear flap descending behind the foreground envelope.','''
path('rear',(6,30),[('L',(6,9)),('A',(9,6),3,3,True),('L',(29,6)),('A',(32,9),3,3,True),('L',(32,18))])
poly('rear-flap',(6,10),(17,19),(23,14));join('rear','rear-flap')
box('front',16,18,42,42,3);join('front','rear')
poly('flap',(17,19),(29,30),(41,19));join('flap','front');join('rear-flap','front')
''','Lucide mail original and atomic geometry: rounded envelope corners with diagonal flap folds; overlapping pair per source.')
