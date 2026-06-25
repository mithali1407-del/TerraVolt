# sustainability.py


def score(backup,growth):

    s=100


    if backup<6:

        s=s-15


    if growth>20:

        s=s-10


    if backup>=8:

        s=s+5


    return s

def category(score):

    if score >= 90:
        return "Excellent"

    elif score >= 80:
        return "Good"

    elif score >= 70:
        return "Moderate"

    else:
        return "Needs Improvement"