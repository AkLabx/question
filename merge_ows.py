import json
import spacy
import re

# Load Spacy model
print("Loading Spacy model...")
nlp = spacy.load("en_core_web_sm")

def get_pos(word, sentence):
    """
    Determines the Part of Speech (POS) of a word based on its usage in a sentence.
    """
    if not sentence:
        # Fallback if no sentence is provided
        doc = nlp(word)
        return doc[0].pos_

    doc = nlp(sentence)
    # Lemmatize the target word for comparison
    target_lemma = nlp(word)[0].lemma_.lower()

    for token in doc:
        # Check if token matches the word (considering lemma and case)
        if token.lemma_.lower() == target_lemma or token.text.lower() == word.lower():
            return token.pos_

    # Fallback: return the POS of the word in isolation if not found in sentence context
    return nlp(word)[0].pos_

def generate_note(word, meaning, origin):
    """
    Generates an educational note based on heuristics, roots, and origin.
    This simulates 'intelligent' annotation.
    """
    note_parts = []
    word_lower = word.lower()
    meaning_lower = meaning.lower()
    origin_lower = origin.lower() if origin else ""

    # 1. Etymological/Root Analysis
    if "phobia" in word_lower:
        note_parts.append("Suffix '-phobia' denotes an extreme or irrational fear.")
    if "cide" in word_lower:
        note_parts.append("Suffix '-cide' refers to the act of killing (e.g., suicide, homicide).")
    if "cracy" in word_lower or "arch" in word_lower:
        note_parts.append("Suffixes like '-cracy' or '-archy' typically refer to forms of government or rule.")
    if "logy" in word_lower:
        note_parts.append("Suffix '-logy' usually means 'the study of'.")
    if "theist" in word_lower or "theism" in word_lower:
        note_parts.append("Root 'theos' refers to God.")
    if "vorous" in word_lower:
        note_parts.append("Suffix '-vorous' indicates feeding habits (e.g., carnivorous).")
    if "ambi" in word_lower:
        note_parts.append("Prefix 'ambi-' means 'both' or 'around'.")
    if "bene" in word_lower:
        note_parts.append("Prefix 'bene-' means 'good' or 'well'.")
    if "mal" in word_lower and not word_lower.startswith("male"): # exclude male/female
        note_parts.append("Prefix 'mal-' typically means 'bad' or 'evil'.")
    if "somn" in word_lower:
        note_parts.append("Root 'somnus' relates to sleep.")
    if "bell" in word_lower and "war" in meaning_lower:
        note_parts.append("Root 'bellum' means war.")
    if "greg" in word_lower:
        note_parts.append("Root 'grex' or 'greg-' refers to a flock or herd.")

    # 2. Contextual/Usage Notes
    if "Greek" in origin_lower:
        note_parts.append("This term has its roots in Greek mythology or language.")
    elif "Latin" in origin_lower:
        note_parts.append("Derived from Latin.")

    if "med." in meaning_lower or "medicine" in meaning_lower or "disease" in meaning_lower:
        note_parts.append("Often used in medical contexts.")
    if "law" in meaning_lower or "legal" in meaning_lower:
        note_parts.append("Frequently used in legal terminology.")

    # 3. Specific Confusions (Hardcoded for common OWS)
    if word_lower == "egoist":
        note_parts.append("Don't confuse with 'egotist' (someone who talks excessively about themselves).")
    if word_lower == "immigrant":
        note_parts.append("Compare with 'emigrant' (one who leaves a country).")
    if word_lower == "emigrant":
        note_parts.append("Compare with 'immigrant' (one who enters a country).")
    if "stationary" in word_lower:
        note_parts.append("Not to be confused with 'stationery' (writing materials).")
    if "stationery" in word_lower:
        note_parts.append("Not to be confused with 'stationary' (not moving).")

    # Combine notes
    if note_parts:
        return " ".join(note_parts)
    return ""

def process_file(filepath, difficulty, start_id):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    processed_items = []
    current_id = start_id

    # Flatten the structure: The files are dicts like {"1": [...], "2": [...]}
    all_words = []
    if isinstance(data, dict):
        for page_num, items in data.items():
            if isinstance(items, list):
                all_words.extend(items)
    elif isinstance(data, list):
        all_words = data

    for item in all_words:
        word = item.get("word", "")
        meaning = item.get("meaning_en", "")
        usage_sentences = item.get("usage_sentences", [])
        origin = item.get("origin", "")

        # Intelligent POS generation
        first_sentence = usage_sentences[0] if usage_sentences else ""
        pos = get_pos(word, first_sentence)

        # Intelligent Note generation
        note = generate_note(word, meaning, origin)

        # Map POS tags to full names if possible
        pos_map = {
            "NOUN": "Noun", "VERB": "Verb", "ADJ": "Adjective", "ADV": "Adverb",
            "PROPN": "Proper Noun", "PRON": "Pronoun"
        }
        pos = pos_map.get(pos, pos.title())

        new_item = {
            "id": str(current_id),
            "sourceInfo": {
                "pdfName": "Blackbook",
                "examYear": 2025
            },
            "properties": {
                "difficulty": difficulty,
                "status": "Active"
            },
            "content": {
                "id": current_id,
                "pos": pos,
                "word": word,
                "meaning_en": meaning,
                "meaning_hi": item.get("meaning_hi", ""),
                "usage_sentences": usage_sentences,
                "note": note,
                "origin": origin
            }
        }
        processed_items.append(new_item)
        current_id += 1

    return processed_items, current_id

def main():
    files_map = [
        ("easy-ows.json", "Easy"),
        ("moderate-ows.json", "Medium"),
        ("hard-ows.json", "Hard")
    ]

    final_data = []
    global_id_counter = 1

    for filepath, difficulty in files_map:
        items, next_id = process_file(filepath, difficulty, global_id_counter)
        final_data.extend(items)
        global_id_counter = next_id

    print(f"Total items processed: {len(final_data)}")

    output_file = "final_ows.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=4, ensure_ascii=False)
    print(f"Successfully wrote to {output_file}")

if __name__ == "__main__":
    main()
