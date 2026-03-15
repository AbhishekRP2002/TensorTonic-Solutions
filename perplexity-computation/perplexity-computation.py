def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    import numpy as np
    log_sum = sum([np.log(prob_distributions[i][actual_tokens[i]]) for i in range(0, len(actual_tokens))])
    return np.exp(-(log_sum) / len(actual_tokens))
    