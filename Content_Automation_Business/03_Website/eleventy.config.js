import markdownItAnchor from "markdown-it-anchor";

// Heading ids: ASCII letters, digits and dashes only ("Step 1: The prompt" → "step-1-the-prompt")
const slugify = (s) => s.normalize("NFKD").toLowerCase().replace(/['’]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").replace(/^(?=[0-9])/, "s-");

const CATEGORY_ORDER = ["client-workflows", "getting-paid", "ai-done-right", "systems-sops", "tools-honestly"];

export default function (eleventyConfig) {
  // ---- Assets and downloads
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/downloads": "downloads" });
  eleventyConfig.addPassthroughCopy({ "src/_headers": "_headers" });
  // The bundle landing page is built in Digital_Products_Business and published at /bundle/
  eleventyConfig.addPassthroughCopy({ "../../Digital_Products_Business/07_Gumroad_Storefront/Bundle_Landing_Page": "bundle" });

  // ---- Markdown: heading anchors
  eleventyConfig.amendLibrary("md", (md) => {
    md.set({ typographer: true });
    md.use(markdownItAnchor, { level: [2, 3], tabIndex: false, slugify });
  });

  // ---- Collections
  eleventyConfig.addCollection("posts", (api) =>
    api.getFilteredByGlob("src/blog/posts/*.md").sort((a, b) =>
      (b.data.date - a.data.date) || a.data.title.localeCompare(b.data.title)));

  // ---- Filters
  const fmt = new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
  eleventyConfig.addFilter("readableDate", (d) => fmt.format(new Date(d)));
  eleventyConfig.addFilter("isoDate", (d) => new Date(d).toISOString().slice(0, 10));
  eleventyConfig.addFilter("readingTime", (content) => {
    const words = String(content || "").replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(words / 220));
  });
  eleventyConfig.addFilter("byCategory", (posts, slug) => (posts || []).filter((p) => p.data.category === slug));
  eleventyConfig.addFilter("bySlugs", (posts, slugs) =>
    (slugs || []).map((s) => (posts || []).find((p) => p.data.slug === s)).filter(Boolean));
  eleventyConfig.addFilter("categoryName", (slug, categories) => (categories.find((c) => c.slug === slug) || {}).name || slug);
  eleventyConfig.addFilter("absolute", (path, base) => new URL(path, base).toString());
  eleventyConfig.addFilter("json", (v) => JSON.stringify(v));
  eleventyConfig.addFilter("limit", (arr, n) => (arr || []).slice(0, n));
  eleventyConfig.addFilter("articleJsonLd", (title, description, date, updated, slug, category, catName, url, site) => {
    const abs = (u) => new URL(u, site.baseUrl).toString();
    const iso = (d) => new Date(d).toISOString().slice(0, 10);
    const org = { "@type": "Organization", name: site.name, url: abs("/") };
    return JSON.stringify({
      "@context": "https://schema.org",
      "@graph": [
        { "@type": "Article", headline: title, description, datePublished: iso(date), dateModified: iso(updated || date),
          author: org, publisher: org, mainEntityOfPage: abs(url), image: abs(`/assets/og/${slug}.png`) },
        { "@type": "BreadcrumbList", itemListElement: [
          { "@type": "ListItem", position: 1, name: "Articles", item: abs("/blog/") },
          { "@type": "ListItem", position: 2, name: catName, item: abs(`/category/${category}/`) },
          { "@type": "ListItem", position: 3, name: title } ] },
      ],
    }).replace(/</g, "\\u003c");
  });
  eleventyConfig.addFilter("orderCategories", (cats) =>
    [...cats].sort((a, b) => CATEGORY_ORDER.indexOf(a.slug) - CATEGORY_ORDER.indexOf(b.slug)));

  // ---- HTML transforms: responsive tables, task-list checkboxes, external links
  eleventyConfig.addTransform("enhance-html", function (content) {
    if (!(this.page.outputPath || "").endsWith(".html")) return content;
    let n = 0;
    return content
      .replace(/<table>/g, () => `<div class="table-wrap" role="region" aria-label="Table ${++n}" tabindex="0"><table>`)
      .replace(/<\/table>/g, "</table></div>")
      .replace(/<li>\[ \] /g, '<li class="task"><span class="box" aria-hidden="true"></span>')
      .replace(/<li>\[x\] /gi, '<li class="task done"><span class="box" aria-hidden="true"></span>')
      .replace(/<a href="(https?:\/\/[^"]+)"(?![^>]*rel=)/g, '<a href="$1" rel="noopener"');
  });

  return {
    dir: { input: "src", includes: "_includes", data: "_data", output: "_site" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"],
  };
}
