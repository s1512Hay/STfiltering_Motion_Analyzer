The goal of this project is to extract motion using spatiotemporal filtering.
While signals sampled at times to compute motion from the relations, spatiotemporal filtering offers
a fast and accurate ( in the sense of motion between more then a few frames) method.
The program consists of 3 functions- 1.GaborSTfiltering()- applies spatiotemporal filtering of the
Gabor energy to the y and time axis of the video: the video is been read into a 3D array using
vid = skvideo.io.vread("video_file.avi", outputdict={"-pix_fmt": "gray"})[:, :, :, 0];
from skvideo library.
Then applying the Gabor Energy onto the each spatiotemporal slice given in a loop, normalizing
and saving at ‘outputvid’ a3D array. After all slices have been saved- all frames are saved into an
image “outputvideo_Gabor.mp4”
2.TapSTfiltering()- applies the same as the above, only for the 9_tap filter. The output video is
saved as "outputvideo_9tap.mp4"
3. GaborEnergy- applies the Gabor Energy for an image. The even and odd parts are obtained by
creating 2 Gabor kernels- one for the even part with phase offset=0 and one for the odd part with
phase offset= pi/2.
