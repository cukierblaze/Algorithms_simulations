from Frame import Frame

def FIFO(num_frames, pages):
    page_errors = 0
    frames = [Frame(_) for _ in range(num_frames)]

    for page in pages:
        page_found = False
        for i, frame in enumerate(frames):
            if frame.page == page:
                page_found = True
                break
        if not page_found:
            oldest_frame_index = min(range(num_frames), key=lambda i: frames[i].index)
            frames[oldest_frame_index].page = page
            frames[oldest_frame_index].index = max(frame.index for frame in frames) + 1

            page_errors += 1

        #print([frame.page for frame in frames])

    return page_errors


