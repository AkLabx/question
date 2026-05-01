# Guide to Adding Questions to the UPSC Quiz App

This guide explains how developers can add more questions to the `quizData` array in the `index.html` file. 

## Where to find the data
Open `index.html` and search for `const baseData = [`. This is an array of question objects. You can add new objects to this array.

## Question Formats Supported

The quiz engine supports several question types:
1. **Standard Multiple Choice / Statements Based**
2. **Assertion-Reasoning** (`type: "assertion"`)
3. **Match the Following** (`type: "match"`)

## Basic Properties
Every question object requires these core properties:
- `q`: (String) The main question text. You can include English and Hindi separated by " / ".
- `o`: (Array of Strings) Exactly 4 options. 
- `a`: (Integer) The index of the correct option (0-based, so `0` is A, `1` is B, `2` is C, `3` is D).
- `e`: (Object) The explanation object containing:
  - `concept`: General concept or fact.
  - `correct`: Explanation of why the right answer is correct.
  - `wrong`: Explanation of why the other options are wrong.

### Optional Properties:
- `statements`: (Array of Strings) Use this for statement-based questions (e.g., "Consider the following statements...").
- `type`: Define `"assertion"` or `"match"` to trigger specialized UI layouts.

---

## 📋 SAMPLE TEMPLATE (Copy & Paste)

Here is a sample with two different question formats that you can directly insert into the `baseData` array:

```javascript
    // -------------------------------------------------------------
    // QUESTION TEMPLATE 1: Standard / Statements Based
    // -------------------------------------------------------------
    {
        q: "Consider the following statements regarding the Reserve Bank of India (RBI): / भारतीय रिज़र्व बैंक (RBI) के संबंध में निम्नलिखित कथनों पर विचार करें:",
        statements: [
            "It was established on April 1, 1935, in accordance with the provisions of the Reserve Bank of India Act, 1934. / इसकी स्थापना 1 अप्रैल, 1935 को भारतीय रिज़र्व बैंक अधिनियम, 1934 के प्रावधानों के अनुसार की गई थी।",
            "It is responsible for printing currency notes of all denominations. / यह सभी मूल्यवर्ग के मुद्रा नोट छापने के लिए जिम्मेदार है।"
        ],
        o: [
            "1 only / केवल 1", 
            "2 only / केवल 2", 
            "Both 1 and 2 / 1 और 2 दोनों", 
            "Neither 1 nor 2 / न तो 1 और न ही 2"
        ],
        a: 0, // Option A is correct (0-index)
        e: {
            concept: "The Reserve Bank of India is India's central bank and regulatory body responsible for the regulation of the Indian banking system.",
            correct: "Statement 1 is correct. RBI was established in 1935. One Rupee notes are issued by the Ministry of Finance, making Statement 2 incorrect.",
            wrong: "Statement 2 is incorrect because the One Rupee note bears the signature of the Finance Secretary of India, not the RBI Governor."
        }
    },
    // -------------------------------------------------------------
    // QUESTION TEMPLATE 2: Assertion-Reason (A/R) Type
    // -------------------------------------------------------------
    {
        type: "assertion",
        q: "Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):",
        assertion: "The Western Ghats are relatively higher in their southern region. / पश्चिमी घाट अपने दक्षिणी क्षेत्र में अपेक्षाकृत अधिक ऊँचे हैं।",
        reason: "Anaimudi is the highest peak in the Western Ghats. / अनाईमुडी पश्चिमी घाट की सबसे ऊँची चोटी है।",
        o: [
            "Both (A) and (R) are true and (R) is the correct explanation of (A) / (A) और (R) दोनों सत्य हैं और (R) (A) का सही स्पष्टीकरण है",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A) / (A) और (R) दोनों सत्य हैं लेकिन (R) (A) का सही स्पष्टीकरण नहीं है",
            "(A) is true but (R) is false / (A) सत्य है लेकिन (R) असत्य है",
            "(A) is false but (R) is true / (A) असत्य है लेकिन (R) सत्य है"
        ],
        a: 1, // Option B is correct (0-index)
        e: {
            concept: "Geography of Peninsular India and the Western Ghats.",
            correct: "Both statements are factually correct. However, Anaimudi being the highest peak is just a fact supporting the assertion, it is NOT the geological or tectonic 'reason' why the southern section is elevated.",
            wrong: "Option A is incorrect because the Reason does not explain the physical or geological cause of the height difference."
        }
    },
    // -------------------------------------------------------------
    // QUESTION TEMPLATE 3: Match the Following Type
    // -------------------------------------------------------------
    {
        type: "match",
        q: "Match List-I with List-II and select the correct answer using the code given below the lists:",
        lists: {
            list1: [
                { id: 'A', text: 'Mohenjo-Daro' },
                { id: 'B', text: 'Harappa' },
                { id: 'C', text: 'Lothal' },
                { id: 'D', text: 'Kalibangan' }
            ],
            list2: [
                { id: '1', text: 'Dockyard' },
                { id: '2', text: 'Great Bath' },
                { id: '3', text: 'Ploughed field' },
                { id: '4', text: 'Granary' }
            ]
        },
        o: [
            "A-2, B-4, C-1, D-3",
            "A-2, B-1, C-4, D-3",
            "A-4, B-2, C-1, D-3",
            "A-3, B-4, C-1, D-2"
        ],
        a: 0, // Option A is correct
        e: {
            concept: "Major Indus Valley Civilization Sites and their prominent findings.",
            correct: "Mohenjo-Daro is famous for the Great Bath. Harappa has the Great Granary. Lothal was a port city with a Dockyard. Kalibangan has evidence of a ploughed field.",
            wrong: "Match carefully: Lothal is strictly associated with the Dockyard (C-1)."
        }
    }
```

## Tips for adding questions:
- **Indices:** Ensure `a` correctly points to the 0-based index of the answer.
- **Missing Options:** Always provide exactly 4 options into the `o` array.
- **Total Questions Limits:** If you add more questions, ensure `config.totalQuestions` is updated if you want all of them to show up, else it will slice the array to the config limit.
