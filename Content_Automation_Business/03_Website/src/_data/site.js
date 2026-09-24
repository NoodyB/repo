/**
 * Site settings. Launch values (store, site URL, newsletter, support email) are read from
 * Build_Tools/launch_config.py so the whole business has ONE place to set them.
 * Environment variables with the same names override them (e.g. on Cloudflare Pages).
 * Never put API keys or passwords here: this file and launch_config.py are committed.
 */
import fs from "node:fs";

const cfgPath = new URL("../../../../Build_Tools/launch_config.py", import.meta.url);
const cfg = fs.existsSync(cfgPath) ? fs.readFileSync(cfgPath, "utf8") : "";
const read = (name) => process.env[name] || (cfg.match(new RegExp(`^${name}\\s*=\\s*"([^"]*)"`, "m")) || [])[1] || "";
const strip = (u) => u.replace(/\/+$/, "");

const url = strip(read("SITE_URL"));
const store = strip(read("STORE_URL"));

export default {
  name: "Band of One",
  tagline: "Practical AI systems for businesses of one.",
  description: "Practical, no-hype guides to running client admin with AI and simple systems, for freelancers, consultants, coaches and VAs.",
  lang: "en",
  url,                                   // "" until a domain is bought
  isPreview: !url,                       // preview builds are noindex + show a banner
  baseUrl: url || "http://localhost:8080",
  storeUrl: store,
  storeLink: (slug) => (store ? `${store}/l/${slug}` : "/resources/#products"),
  newsletterUrl: read("NEWSLETTER_URL"),
  supportEmail: read("SUPPORT_EMAIL"),
  cfAnalyticsToken: process.env.CF_ANALYTICS_TOKEN || "",  // optional; Pages one-click analytics needs no token
  year: 2026,
};
