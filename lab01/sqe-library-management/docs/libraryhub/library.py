def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")

    if days_overdue == 0:
        return "None"

    if 1 <= days_overdue <= 7:
        return "Low"

    if 8 <= days_overdue <= 14:
        return "Medium"

    if 15 <= days_overdue <= 30:
        return "High"

    return "Severe"