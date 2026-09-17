import json
import unittest
from icon_set.scripts.combination_experiment import DATA, POSITIONS, number, placement, render, custom_item

class CombinationExperimentTests(unittest.TestCase):
    def test_every_pair_every_anchor(self):
        for row in json.loads(DATA.read_text())['rows']:
            for ax,ay in POSITIONS.values():
                for role,size,anchor in [('mains',48,(1-ax,1-ay)),('subs',32,(ax,ay))]:
                    for item in row[role]:
                        box=placement(item,size,anchor,(0,0))['painted_box']
                        for k,e,a in [('x','w',anchor[0]),('y','h',anchor[1])]:
                            self.assertAlmostEqual(box[k]+box[e]*a,2+60*a)

    def test_keyshape_does_not_change_origin_or_scale(self):
        for w,h in [(36,36),(40,32),(32,40),(40,40)]:
            item={'bounds':[(48-w)/2,(48-h)/2,(48+w)/2,(48+h)/2],'canvas':48}
            p=placement(item,48,(0,0),(0,0))
            self.assertEqual(p['canvas_box'],dict(x=2,y=2,w=48,h=48))
            self.assertEqual(p['painted_box'],dict(x=2,y=2,w=w+4,h=h+4))
            shifted=placement(item,48,(0,0),(2.5,3))
            self.assertEqual(shifted['painted_box'],dict(x=4.5,y=5,w=w+4,h=h+4))

    def test_zero_padding_and_invalid_padding(self):
        item={'bounds':[4,4,44,44],'canvas':48}
        self.assertEqual(placement(item,48,(0,0),(0,0),padding=0)['painted_box']['x'],0)
        row=json.loads(DATA.read_text())['rows'][0]
        for padding in [-1,9]:
            with self.assertRaises(ValueError):render({'id':row['id'],'padding':padding})

    def test_invalid_manual_uploads(self):
        for document in ['not svg','<!DOCTYPE svg><svg/>',
                         '<svg viewBox="0 0 48 32"/>',
                         '<svg viewBox="0 0 48 48"><script>alert(1)</script></svg>']:
            with self.assertRaises(ValueError):custom_item({'document':document},'main')

    def test_reject_invalid_values(self):
        for v in ['invalid','NaN','Infinity',100]:
            with self.assertRaises(ValueError):number(v)
        with self.assertRaises(ValueError):render({'id':'not-a-pair'})

if __name__=='__main__':unittest.main()
