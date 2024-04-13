from Frame import Frame


def LRU(num_frames, pages):
    page_errors = 0
    current_time = 0
    # Create Frame instances with additional attribute to track last used time
    frames = [(Frame(), -1) for _ in range(num_frames)]

    for page in pages:
        page_found = False

        for index, (frame, last_used_time) in enumerate(frames):
            if frame.page == page:
                page_found = True
                frames[index] = (frame, current_time)
                break

        if page_found:
            current_time += 1
            #print([frame[0].page for frame in frames])
            continue

        for index, (frame, last_used_time) in enumerate(frames):
            if frame.page is None:
                frame.set_page(page, current_time)
                frames[index] = (frame, current_time)
                page_errors += 1
                page_found = True
                break

        if page_found:
            current_time += 1
            #print([frame[0].page for frame in frames])
            continue

        # If no empty frame is found, find the least recently used frame
        min_index = min(range(len(frames)), key=lambda i: frames[i][1])
        frame, _ = frames[min_index]
        frame.set_page(page, current_time)
        frames[min_index] = (frame, current_time)
        page_errors += 1
        current_time += 1
        #print([frame[0].page for frame in frames])
    return page_errors




