

### INTRODUCTION

I built a face morphing tool in opencv/c++ which nicely morphs one's face to the other's using the delaunauy triangulation and  affine transformations.

### HOW TO RUN

1) To complie type:g++ facemorph.cpp ‘pkg-config –cflags opencv –libs opencv

2) ./a.out

3) Then choose the various options that are clearly specified in command promts.
##

### Implementation Details

I identified and marked important points that define the structure of a face manually to get a correspondece between the points. 
I then used sampled points from images to get the the delaunauy triangulation in opencv using opencv functions:-
subdiv.getTriangleList() for getting the triangulation in the intermediate image frames. Then we need to do two steps -1. Cross Dissolve 2.Wrapping  

For Cross Dissolve i finded the intermediate points between source and destination matching points using interpolation and then made the triangulation for the intermediate points collected.Then i found the inverse affine mapping for each of those triangles and got the colors for these pixels using these  affine mappings.

For Wrapping i used the calulated inverse mapping to get images in correct intermediate shape.
##

### Issues 

I observed that the image morphing quality totally depends on the tie points accuracy and the images selected
for morphing and needs to be replaced by automated selection of simultaneous tie points from the images.


### Refernces Used
[Face_morphing](https://www.learnopencv.com/face-morph-using-opencv-cpp-python/.)
