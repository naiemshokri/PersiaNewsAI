from rapidfuzz import fuzz


def is_duplicate(new_title, existing_titles, threshold=92):

    for title in existing_titles:

        score = fuzz.ratio(
            new_title.lower(),
            title.lower()
        )

        if score >= threshold:
            return True

    return False
