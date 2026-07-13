import numpy as np
import av
import av.datasets

container = av.open(av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4"))

frames = [frame for frame in container.decode(video=0)]
frames[0].to_image().save("/images/first_frame.png")
