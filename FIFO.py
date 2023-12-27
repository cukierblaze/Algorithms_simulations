from Frame import Frame
from frame_generator import Frame_Generator
def FIFO(num_frames, pages):
    page_errors = 0
    frames = [Frame() for _ in range(num_frames)]

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

        print([frame.page for frame in frames])
    return page_errors

if __name__ == "__main__":
    frame_gen = Frame_Generator()
    pages, frames = frame_gen.frame_generator(3, 10)  # Adjust the parameters as needed
    #pages=[1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    #num_frames=3
    errors = FIFO(frames, pages)
    print(f"Total page faults: {errors}")
