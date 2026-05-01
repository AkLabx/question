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
            concept: "The Reserve Bank of India is India's central bank and regulatory body responsible for the regulation of the Indian banking system. / भारतीय रिज़र्व बैंक भारत का केंद्रीय बैंक है और भारतीय बैंकिंग प्रणाली के नियमन के लिए जिम्मेदार है।",
            correct: "Statement 1 is correct. RBI was established in 1935. One Rupee notes are issued by the Ministry of Finance, making Statement 2 incorrect. / कथन 1 सही है। RBI की स्थापना 1935 में हुई थी। एक रुपये के नोट वित्त मंत्रालय द्वारा जारी किए जाते हैं, जिससे कथन 2 गलत हो जाता है।",
            wrong: "Statement 2 is incorrect because the One Rupee note bears the signature of the Finance Secretary of India, not the RBI Governor. / कथन 2 गलत है क्योंकि एक रुपये के नोट पर भारतीय रिज़र्व बैंक के गवर्नर के नहीं बल्कि भारत के वित्त सचिव के हस्ताक्षर होते हैं।"
        }
    },
    // -------------------------------------------------------------
    // QUESTION TEMPLATE 2: Assertion-Reason (A/R) Type
    // -------------------------------------------------------------
    {
        type: "assertion",
        q: "Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R): / नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:",
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
            concept: "Geography of Peninsular India and the Western Ghats. / प्रायद्वीपीय भारत और पश्चिमी घाट का भूगोल।",
            correct: "Both statements are factually correct. However, Anaimudi being the highest peak is a fact supporting the assertion, it is NOT the geological reason why the southern section is elevated. / दोनों कथन तथ्यात्मक रूप से सही हैं। हालाँकि, अनाईमुडी का सबसे ऊँची चोटी होना अभिकथन का समर्थन करने वाला एक तथ्य है, यह भौगोलिक कारण नहीं है कि दक्षिणी भाग क्यों ऊँचा है।",
            wrong: "Option A is incorrect because the Reason does not explain the physical or geological cause of the height difference. / विकल्प A गलत है क्योंकि कारण ऊँचाई के अंतर के भौतिक या भूवैज्ञानिक कारण की व्याख्या नहीं करता है।"
        }
    },
    // -------------------------------------------------------------
    // QUESTION TEMPLATE 3: Match the Following Type
    // -------------------------------------------------------------
    {
        type: "match",
        q: "Match List-I with List-II and select the correct answer using the code given below the lists: / सूची-I को सूची-II के साथ सुमेलित करें और सूचियों के नीचे दिए गए कूट का उपयोग करके सही उत्तर चुनें:",
        lists: {
            list1: [
                { id: 'A', text: 'Mohenjo-Daro / मोहनजो-दड़ो' },
                { id: 'B', text: 'Harappa / हड़प्पा' },
                { id: 'C', text: 'Lothal / लोथल' },
                { id: 'D', text: 'Kalibangan / कालीबंगा' }
            ],
            list2: [
                { id: '1', text: 'Dockyard / गोदीबाड़ा' },
                { id: '2', text: 'Great Bath / विशाल स्नानागार' },
                { id: '3', text: 'Ploughed field / जुता हुआ खेत' },
                { id: '4', text: 'Granary / अन्नागार' }
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
            concept: "Major Indus Valley Civilization Sites and their prominent findings. / प्रमुख सिंधु घाटी सभ्यता स्थल और उनके प्रमुख निष्कर्ष।",
            correct: "Mohenjo-Daro is famous for the Great Bath. Harappa has the Great Granary. Lothal was a port city with a Dockyard. Kalibangan has evidence of a ploughed field. / मोहनजो-दड़ो विशाल स्नानागार के लिए प्रसिद्ध है। हड़प्पा में विशाल अन्नागार है। लोथल डॉकयार्ड (गोदीबाड़ा) वाला एक बंदरगाह शहर था। कालीबंगा में जुते हुए खेत होने के प्रमाण हैं।",
            wrong: "Match carefully: Lothal is strictly associated with the Dockyard (C-1). / सावधानी से मिलान करें: लोथल पूरी तरह से डॉकयार्ड से संबंधित है (C-1)।"
        }
    }
```

## Tips for adding questions:
- **Indices:** Ensure `a` correctly points to the 0-based index of the answer.
- **Missing Options:** Always provide exactly 4 options into the `o` array.
- **Total Questions Limits:** If you add more questions, ensure `config.totalQuestions` is updated if you want all of them to show up, else it will slice the array to the config limit.
