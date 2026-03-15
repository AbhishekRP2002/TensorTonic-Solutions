def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    chunks_list = list()
    if not len(tokens):
        return []
    if chunk_size > len(tokens):
        return [tokens]
    window_start, window_end = 0, chunk_size - 1
    while window_end < len(tokens):
        new_chunk = tokens[window_start:window_end + 1]
        print(new_chunk)
        chunks_list.append(new_chunk)
        window_start = window_end - overlap + 1
        window_end = window_start + chunk_size - 1

    return chunks_list