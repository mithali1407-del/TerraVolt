def suggest(score, backup, growth):

    suggestions = []

    if score < 80:
        suggestions.append(
            "Increase renewable capacity."
        )

    if backup < 6:
        suggestions.append(
            "Consider larger battery storage."
        )

    if growth > 20:
        suggestions.append(
            "Future expansion planning advised."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Current design looks sustainable."
        )

    return suggestions