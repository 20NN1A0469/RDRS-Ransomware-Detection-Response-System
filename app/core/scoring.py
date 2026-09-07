def calculate_score(
    rapid_encryption=False,
    mass_rename=False,
    high_entropy=False,
    cpu_spike=False,
    unknown_process=False
):

    score = 0
    reasons = []

    if rapid_encryption:
        score += 40
        reasons.append("Rapid encryption activity")

    if mass_rename:
        score += 30
        reasons.append("Mass file rename activity")

    if high_entropy:
        score += 25
        reasons.append("High file entropy")

    if cpu_spike:
        score += 15
        reasons.append("CPU spike")

    if unknown_process:
        score += 10
        reasons.append("Unknown/suspicious process")

    score = min(score, 100)

    if score < 40:
        level = "NORMAL"

    elif score < 70:
        level = "WARNING"

    else:
        level = "CRITICAL"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }