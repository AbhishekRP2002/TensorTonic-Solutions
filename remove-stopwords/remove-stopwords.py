def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    for word in stopwords:
        while tokens.count(word) >= 1:
            tokens.remove(word)
    return tokens