// Progression › Side pairs as a Svelte app: builds published/gallery/side-pairs-app.js and side-pairs-app.css,
// which primitives.html loads after the plain scripts it reuses (combine-side.js, side-pairs-data.js, the review
// buttons, the combined popup and the stroke editor).
//   npm run build      (from web/)
//   npm test
import {defineConfig} from 'vite';
import {svelte} from '@sveltejs/vite-plugin-svelte';
import {fileURLToPath} from 'node:url';

const here = path => fileURLToPath(new URL(path, import.meta.url));

export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: here('../../published/gallery'),
    emptyOutDir: false,
    cssCodeSplit: false,
    lib: {entry: here('src/main.js'), name: 'SidePairsApp', formats: ['iife'], fileName: () => 'side-pairs-app.js', cssFileName: 'side-pairs-app'},
    rollupOptions: {output: {assetFileNames: 'side-pairs-app[extname]'}},
    minify: false,
  },
  test: {environment: 'jsdom', include: [here('tests/**/*.test.js')]},
  resolve: process.env.VITEST ? {conditions: ['browser']} : undefined,
});
