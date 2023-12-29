from Frame import Frame
import random
class Frame_Generator:
    def frame_generator(self,num_frames,num_pages):
        pages=[]
        for i in range(1,num_pages+1):
            page=random.randint(1,5)
            pages.append(page)
        frames=random.randint(1,10)
        return pages,frames