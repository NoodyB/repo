// Print every built HTML page (relative to _site) for the page tester.
import fs from "node:fs";
import path from "node:path";
const root = path.resolve("_site");
const out = [];
(function walk(dir) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) walk(p);
    else if (f.endsWith(".html")) out.push(path.relative(root, p));
  }
})(root);
console.log(out.sort().join(" "));
