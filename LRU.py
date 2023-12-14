from Frame import Frame
def LRU(pages,frames):
    page_error=0
    current_time=0
    for page in pages:
        page_found =False
        for frame in enumerate(frames):
            if frame.page == page:
                page_found=True
                break
        if page_found:
            current_time=0
            continue

