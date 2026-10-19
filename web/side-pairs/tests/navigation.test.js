import {afterEach, beforeEach, expect, test, vi} from 'vitest';
import {render, cleanup} from '@testing-library/svelte';
import App from '../src/components/App.svelte';
import {LayoutEditor} from '../src/lib/editor.svelte.js';
beforeEach(() => vi.stubGlobal('ResizeObserver', class { observe() {} unobserve() {} disconnect() {} }));
afterEach(() => { cleanup(); vi.unstubAllGlobals(); });
for (const size of [64, 72]) test(`side navigation preserves the ${size}px canvas`, () => {
  const store = {size, version: 0, ready: false, pairs: new Map(), sizes: () => ({main: size === 72 ? 54 : 48, sub: size === 72 ? 36 : 32})};
  const page = {query: () => '', page: () => 1};
  const view = render(App, {store, editor: new LayoutEditor(), page, params: new URLSearchParams()});
  expect(view.getByRole('link', {name: 'Container layouts'}).getAttribute('href')).toBe(`container-pairs.html?size=${size}`);
  expect(view.getByRole('link', {name: 'All side combinations'}).getAttribute('href')).toBe(`combinations.html?kind=side&size=${size}`);
});
