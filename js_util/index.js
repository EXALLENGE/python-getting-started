const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({
    args: ["--no-sandbox", "--disable-setuid-sandbox"]
  });
  const page = await browser.newPage();
  await page.goto("https://humorous-liquor.glitch.me/");
  await page.screenshot({ path: "screenshot2.png" });

  await browser.close();
})();
