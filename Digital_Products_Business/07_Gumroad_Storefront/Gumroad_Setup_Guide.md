# Gumroad setup guide (for you to do after approval)

**Status: nothing has been created on Gumroad.** No account, product, price or page exists yet. The store is **not live**, and no payment system has been connected or verified. Follow these steps once you've approved the brand name, prices and refund policy.

Estimated time: 60–90 minutes. Cost: $0 up front. Gumroad charges only when you sell (10% + $0.50 per direct sale, plus card processing 2.9% + $0.30; see Pricing_Strategy.md).

> Gumroad's interface changes from time to time. If a menu name below doesn't match, search the Gumroad Help Center for the feature named in **bold**.

---

## 1. Account (you only)

1. Create a Gumroad account with the business email you'll use for support.
2. Choose your username. It becomes your store address (`https://USERNAME.gumroad.com`). Suggested: `bandofone`. Check it's available; a different one is fine.
3. Complete **payout settings** (bank account or PayPal) and any identity or tax forms Gumroad asks for. Only you can do this: it needs your legal and banking details.
4. Profile: upload `02_Branding/logo/band-of-one-mark-512.png` as the avatar and add a short bio from `Content_Automation_Business/02_Branding/Content_Brand_Strategy.md` ("Short bios for social profiles").
5. Put your store URL into `Build_Tools/launch_config.py` (`STORE_URL = "https://USERNAME.gumroad.com"`), then rebuild the landing page (`python3 Build_Tools/build_landing_page.py`) and the lead magnet (`python3 Build_Tools/build_lead_magnet.py`) so every link points to the real store.

## 2. Create the three products (repeat for A, B, C)

For each listing file in `Listings/`:

1. **New product → Digital product.** Enter the **Product name** and **Price** from the listing.
2. **Description**: paste the Description section. Use Gumroad's editor for headings, bold and lists. It won't import Markdown tables exactly, so re-create the tab table as a bulleted list if needed.
3. **Summary** and **Additional details**: paste from the listing.
4. **URL**: set the custom slug from the listing (e.g. `solo-admin-playbook`). The landing page expects these slugs.
5. **Cover**: upload the cover images in the listed order (1280×720, Gumroad's recommended minimum). **Thumbnail**: the 600×600 file.
6. **Content**: upload the product ZIP from `06_Customer_Ready_Products/`. Add the post-purchase message from the listing.
7. **Refund policy**: in Settings, turn on **Specify a refund policy for this product** and paste the 14-day policy text (Pricing_Strategy.md §4).
8. **Tags / category**: choose the closest category (e.g., Business & Money) and add tags from the listing.
9. Keep the product **unpublished** until step 5 (test purchase) passes.

## 3. Create the bundle

1. **New product → Bundle** (Gumroad Help, "Product bundles"). Add A, B and C.
2. Name, price ($49), description, covers, thumbnail, slug `complete-bundle` and refund policy from `Listings/D_Complete-Bundle.md`.

## 4. Free starter kit (optional on Gumroad)

The main home for the free kit is your email platform (see `Content_Automation_Business/07_Email_Newsletter`). If you also list it on Gumroad, create a product at **$0+** using `Listings/E_Free-Starter-Kit.md` and upload the PDF.

## 5. Test before publishing

1. Publish **one** product privately, or keep the product link unlisted, and buy it yourself at full price with your own card.
2. Check that the receipt email arrives, the download works, the ZIP opens, and START-HERE and all files open.
3. Refund yourself from the sales dashboard, then check the refund appears as expected. You'll lose the card-processing fee (about $1). That's the cost of testing.
4. Repeat for the bundle (download each product in it).
5. Only then publish the others.

## 6. Launch discount code

Create a **discount code** `FOUNDING` (Gumroad Help, "Discount codes"): $5 off A and B, $4 off C, $10 off the bundle. Limit the **validity period** to 14 days from launch. Put the real end date in your launch emails and posts.

## 7. After launch

- Record every sale, refund and fee in `09_Business_Dashboard` (weekly).
- Answer support emails within two business days.
- When you update a product, bump the version, rebuild the ZIP (`python3 Build_Tools/build_packages.py`), replace the file on Gumroad and update CHANGELOG.

## What needs your authorization

| Action | Why it needs you |
|---|---|
| Creating the Gumroad account | Legal identity, tax and banking details |
| Publishing any product | Brief: "never publish listings without my approval" |
| Setting prices and refund policy | Business decision (recommendations in Pricing_Strategy.md) |
| Test purchase with your card | Real payment |
| Creating the discount code and announcing it | External communication |
