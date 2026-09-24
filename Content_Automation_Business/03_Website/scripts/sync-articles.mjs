/**
 * Copy articles from ../04_Blog_Articles into src/blog/posts before each build.
 *
 * The approval gate lives here:
 *   npm run build          → only articles with `status: approved` or `status: published`
 *   npm run build:preview  → every article except `rejected` / `archived` (local review only)
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const SRC = path.resolve(here, "../../04_Blog_Articles");
const DEST = path.resolve(here, "../src/blog/posts");
const preview = process.argv.includes("--all");
const LIVE = new Set(["approved", "published"]);
const NEVER = new Set(["rejected", "archived"]);

fs.rmSync(DEST, { recursive: true, force: true });
fs.mkdirSync(DEST, { recursive: true });

const counts = {};
let copied = 0;
for (const file of fs.readdirSync(SRC).filter((f) => f.endsWith(".md") && f !== "README.md")) {
  const text = fs.readFileSync(path.join(SRC, file), "utf8");
  const status = (text.match(/^status:\s*([\w-]+)/m) || [])[1] || "missing";
  counts[status] = (counts[status] || 0) + 1;
  if (NEVER.has(status)) continue;
  if (preview || LIVE.has(status)) {
    fs.copyFileSync(path.join(SRC, file), path.join(DEST, file));
    copied += 1;
  }
}
// Directory data for the synced posts (written here because the folder is regenerated each build)
fs.writeFileSync(path.join(DEST, "posts.11tydata.js"), `export default {
  layout: "layouts/article.njk",
  templateEngineOverride: "md",
  eleventyComputed: { permalink: (data) => \`/blog/\${data.slug}/\` },
};
`);
console.log(`[sync] ${preview ? "PREVIEW" : "PRODUCTION"} build: copied ${copied} article(s). Status counts: ${JSON.stringify(counts)}`);
