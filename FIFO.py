from Frame import Frame

def FIFO(pages, n):
    page_errors = 0
    frames = [Frame() for _ in range(n)]

    for page in pages:
        page_found = False
        for i, frame in enumerate(frames):
            if frame.page == page:
                page_found = True
                break
        if not page_found:
            oldest_frame_index = min(range(n), key=lambda i: frames[i].index)
            frames[oldest_frame_index].page = page
            frames[oldest_frame_index].index = max(frame.index for frame in frames) + 1

            page_errors += 1

        print([frame.page for frame in frames])
    return page_errors

if __name__ == "__main__":
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    n = 3
    errors = FIFO(pages, n)
    print(f"Total page faults: {errors}")
