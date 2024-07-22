const fs = require('fs');
const path = require('path');
const pdf = require('pdf-parse');
const fastcsv = require('fast-csv');

const pdfDir = path.join(__dirname, 'pdfs');

async function extractTextFromPdf(filePath) {
    const dataBuffer = fs.readFileSync(filePath);
    const data = await pdf(dataBuffer);
    return data.text;
}

function processExtractedText(text) {
    const lines = text.split('\n').map(line => line.trim()).filter(line => line.length > 0);
    const data = lines.map(line => line.split(',')); // Adjust this line based on the structure of your PDF content

    console.log('Data: ', lines);
    return data;
}

function writeDataToCsv(data, outputFilePath) {
    const ws = fs.createWriteStream(outputFilePath);
    fastcsv
        .write(data, { headers: true })
        .pipe(ws);
}

async function extractDataFromPdfs() {
    // const files = fs.readdirSync(pdfDir).filter(file => file.endsWith('.pdf'));

    const files = fs.readdirSync(pdfDir).filter(file => file.startsWith('110101'));

    const allData = [];

    for (const file of files) {
        const filePath = path.join(pdfDir, file);
        console.log(`Extracting data from: ${filePath}`);
        const text = await extractTextFromPdf(filePath);
        const processedData = processExtractedText(text);
        allData.push(...processedData);
    }

    const outputFilePath = path.join(__dirname, 'output1.csv');
    writeDataToCsv(allData, outputFilePath);
    console.log(`Data has been written to: ${outputFilePath}`);
}

extractDataFromPdfs().catch(err => {
    console.error('Error extracting data from PDFs:', err);
});
