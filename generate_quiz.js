const fs = require('fs');

const templatePath = 'Html_quiz_template/QUIZ HTML tempmate.html';
const txtPath = 'Questions_text_format/20_April_GK_AEDO_BPSC.txt';
const outPath = 'Generated_Quizzes/20_April_GK_AEDO_BPSC_Quiz.html';

const templateContent = fs.readFileSync(templatePath, 'utf8');
const txtContent = fs.readFileSync(txtPath, 'utf8');

// Extract baseData from txt file
const txtMatch = txtContent.match(/const baseData = (\[[\s\S]*?\]);/);
if (!txtMatch) {
    console.error("Could not find baseData in the text file.");
    process.exit(1);
}

let baseDataString = txtMatch[1];

// Clean up OCR artifacts
baseDataString = baseDataString.replace(/\[span_\d+\]\(start_span\)/g, '');
baseDataString = baseDataString.replace(/\[span_\d+\]\(end_span\)/g, '');

const examName = "20 April GK AEDO BPSC";
const safeExamName = examName.replace(/[^a-zA-Z0-9]/g, '_');

// Update configuration
let newHtml = templateContent.replace(/const config = \{.*?\};/s, `const config = {
            examName: "${examName}",
            examDate: "20 April",
            subject: "GK/GS",
            paperName: "Mock Test",
            timeInMinutes: 150,
            totalQuestions: 100
        };`);

// Update baseData using a replacement function to avoid $ substitutions!
newHtml = newHtml.replace(/const baseData = \[.*?\];/s, () => `const baseData = ${baseDataString};`);

// Update localStorage keys so each quiz has a unique state
newHtml = newHtml.replace(/upscQuizState/g, `quizState_${safeExamName}`);
newHtml = newHtml.replace(/upscQuizHistory/g, `quizHistory_${safeExamName}`);

// Ensure mobile responsiveness viewport tag
if (!newHtml.includes('maximum-scale=1.0')) {
    newHtml = newHtml.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
    );
}

fs.writeFileSync(outPath, newHtml, 'utf8');
console.log('Successfully generated HTML with fixed string replacements and isolated storage.');
