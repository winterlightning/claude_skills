import {test, expect} from 'vitest';
import {subProblems} from '../src/lib/rules.js';
test('native36 sub ink is valid on72 and remains oversized on64', () => {
 const sub={bounds:[2,2,34,34]};
 expect(subProblems({size:72},sub)).toEqual([]);
 expect(subProblems({size:64},sub)).toEqual(['Ink 36×36 exceeds 32×32']);
 expect(subProblems({size:72},{bounds:[2,2,35,34]})).toEqual(['Ink 37×36 exceeds 36×36']);
});
