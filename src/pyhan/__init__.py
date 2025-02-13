from .han import Han


def add_rule(rule):
    return Han().add_rule(rule)


def to_traditional(original):
    return Han().to_traditional(original)
