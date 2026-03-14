const puppeteer = require("puppeteer");

(async () => {

  const url = process.argv[2];

  if (!url) {
    console.error("Usage: node pdf.js <url>");
    process.exit(1);
  }

  console.log("Launching browser...");

  const browser = await puppeteer.launch({
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH,
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox"
    ]
  });

  const page = await browser.newPage();

  console.log("Opening page:", url);

  await page.goto(url, {
    waitUntil: "networkidle0"
  });

//  console.log("Waiting for ReSpec...");

//  await page.waitForFunction(() => {
//    return document.respec && document.respec.ready;
//  });

  console.log("Waiting for title...");

  await page.waitForSelector("h1", { timeout: 60000 });

  const title = await page.evaluate(() =>
    document.querySelector("h1").innerText
  );

  const filename = await page.evaluate(() => {

    // zoek de PDF link die Respec genereert
    const link = document.querySelector('a[href$=".pdf"]');

    if (link) {
      const parts = link.getAttribute("href").split("/");
      return parts[parts.length - 1];
    }

    // fallback
    const title = document.querySelector("h1").innerText;
    return title.replace(/\s+/g, "-") + ".pdf";
  });

  console.log("Generating PDF:", filename);

  await page.pdf({
    path: filename,
    format: "A4",
    printBackground: true,
    margin: {
      top: "20mm",
      bottom: "20mm",
      left: "15mm",
      right: "15mm"
    }
  });

  await browser.close();

  console.log("PDF generated:", filename);

})();
