const axios = require("axios");
const fs = require("fs");
const path = require("path");
const CENTER_NUMBERS = require("./neet_ug_ceters");

const startNumber = 110101;
const endNumber = 461312;
const baseUrl = "https://neetfs.ntaonline.in/NEET_2024_Result/";
const outputDir = path.join(__dirname, "pdfs");
const delay = 0; // 1 minute in milliseconds

// Create directory if it doesn't exist
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

async function downloadPdf(number) {
  const url = `${baseUrl}${number}.pdf`;
  const filePath = path.join(outputDir, `${number}.pdf`);

  try {
    const response = await axios({
      url,
      method: "GET",
      responseType: "stream",
    });

    response.data.pipe(fs.createWriteStream(filePath));

    return new Promise((resolve, reject) => {
      response.data.on("end", () => {
        console.log(`Downloaded: ${filePath}`);
        resolve();
      });

      response.data.on("error", (err) => {
        console.error(`Error downloading ${url}:`, err);
        reject(err);
      });
    });
  } catch (error) {
    console.error(`Failed to download ${url}:`, error.message);
  }
}

async function downloadAllPdfs() {
  for (let number = 0; number < CENTER_NUMBERS.length; number++) {
    // console.log(CENTER_NUMBERS[number]);
    await downloadPdf(CENTER_NUMBERS[number]);
    await new Promise((resolve) => setTimeout(resolve, delay)); // Wait for the specified delay
  }
}

downloadAllPdfs().catch((err) => {
  console.error("Error downloading PDFs:", err);
});
