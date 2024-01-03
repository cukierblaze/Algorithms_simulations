from Frame import Frame
import random
from FIFO import FIFO
from LRU import  LRU


class Frame_Generator:
    def frame_generator(num_frames,num_pages,num_ref):
        pages=[]
        frames=[]
        for i in range(1,num_ref+1):
            page=random.randint(1,num_pages)
            pages.append(page)
        print("Ref to pages",pages)
        print('Fifo er', FIFO(num_frames, pages))
        print('LRU er', LRU(num_frames, pages))

Frame_Generator.frame_generator(3, 10, 5)