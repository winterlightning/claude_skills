import json
import tempfile
import unittest
from pathlib import Path
from icon_set.scripts.deduplicate_subs import canonical_map, deduplicate_pairs, fingerprint, update_catalog

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><title>{}</title><path id="{}" d="M2 16L30 16"/></svg>'

class SubDeduplicationTests(unittest.TestCase):
    def test_metadata_is_ignored_but_geometry_and_styles_are_not(self):
        a, b = SVG.format('a','a'), SVG.format('b','b')
        self.assertEqual(fingerprint(a), fingerprint(b))
        self.assertNotEqual(fingerprint(a), fingerprint(b.replace('30 16', '29 16')))
        self.assertNotEqual(fingerprint(a), fingerprint(b.replace('<path', '<path stroke="red"')))

    def test_native_wins_and_all_pair_references_are_updated_idempotently(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            manifest = {}
            for uid, family in [('short','solo'),('native-sub32','sub')]:
                (root/(uid+'.svg')).write_text(SVG.format(uid,uid))
                manifest[uid] = dict(icon=uid,family=family,svg=uid+'.svg',export_url=uid+'.svg')
            aliases, groups = canonical_map(manifest, root)
            self.assertEqual(aliases, {'short':'native-sub32'})
            item = dict(manifest['short'], document=SVG.format('short','short'), bounds=[2,16,30,16], canvas=32)
            pairs = {'rows':[{'id':'one','subs':[item,item.copy()],'mains':[{'icon':'short'}]}]}
            self.assertEqual(deduplicate_pairs(pairs,manifest,aliases,root),1)
            row=pairs['rows'][0]
            self.assertEqual(len(row['subs']),1)
            self.assertEqual(row['subs'][0]['icon'],'native-sub32')
            self.assertEqual(row['mains'],[{'icon':'short'}])
            self.assertEqual(deduplicate_pairs(pairs,manifest,aliases,root),0)
            catalog={'rows':[{'sub_id':'source'}],'references':{'source':{'generated':[dict(icon_id='short',key='solo/short',preview_url='short.svg'),dict(icon_id='native-sub32',key='sub/native-sub32',preview_url='native-sub32.svg')]}}}
            update_catalog(catalog,manifest,aliases)
            self.assertEqual(len(catalog['rows'][0]['sub_generated']),1)
            self.assertEqual(len(catalog['references']['source']['generated']),2)
            row['subs'][0]['document']=SVG.format('short','short').replace('30 16','29 16')
            row['subs'][0]['icon']='short'
            with self.assertRaisesRegex(ValueError,'Stale pair'):
                deduplicate_pairs(pairs,manifest,aliases,root)

    def test_reviewed_merge_expires_when_either_artwork_changes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = root/'icon_set/data'
            data.mkdir(parents=True)
            a = SVG.format('a','a')
            b = a.replace('30 16', '28 16')
            (root/'a.svg').write_text(a)
            (root/'b.svg').write_text(b)
            manifest = {uid:dict(icon=uid,family='sub',svg=uid+'.svg') for uid in ('a','b')}
            self.assertEqual(canonical_map(manifest,root)[0],{})
            (data/'sub-deduplication-review.json').write_text(json.dumps({'decisions':[{
                'decision':'merge','icons':['a','b'],
                'fingerprints':{'a':fingerprint(a),'b':fingerprint(b)}}]}))
            self.assertEqual(canonical_map(manifest,root)[0],{'b':'a'})
            (root/'b.svg').write_text(b.replace('28 16','26 16'))
            self.assertEqual(canonical_map(manifest,root)[0],{})
