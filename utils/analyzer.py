def count_fillers(text):

    fillers = [
        "um",
        "uh",
        "like",
        "actually",
        "basically",
        "you know"
    ]

    text = text.lower()

    count = 0

    for filler in fillers:
        count += text.count(filler)

    return count


def generate_score(filler_count):

    score = 100

    if filler_count > 5:
        score -= 20

    elif filler_count > 2:
        score -= 10

    return score


def generate_feedback(filler_count):

    if filler_count <= 2:

        return (
            "Excellent communication with minimal filler words. "
            "Your speaking fluency appears strong."
        )

    elif filler_count <= 5:

        return (
            "Good communication skills. "
            "Try reducing filler words to improve fluency."
        )

    else:

        return (
            "High filler word usage detected. "
            "Practice mock interviews to improve confidence and clarity."
        )


def calculate_confidence(
    interview_score,
    eye_contact_score
):

    confidence_score = (
        interview_score * 0.5
        + eye_contact_score * 0.5
    )

    return round(
        confidence_score,
        2
    )