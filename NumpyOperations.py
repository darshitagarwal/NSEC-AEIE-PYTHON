import numpy as np
class NumpyArrays:
    def MultiDimArrays():
        array_1=np.array([[1,2,3],[3,1,5],[4,5,6]])
        array_2=np.array([[[1,2,3],[3,1,5]],[[1,2,3],[9,8,7]],[[9,5,1],[1,5,9]]])
        ShapeCheck=np.shape(array_1)
        ShapeCheck_2=np.shape(array_2)
        print(array_1,"\n",array_1.ndim,ShapeCheck)
        print("\n")
        print(array_2,"\n",array_2.ndim,ShapeCheck_2)
        print("\n")
        print("----2D array-----")
        for x in array_1:
            for y in x:
                print(y,end=" ")
        print("\n")
        print("----3D array-----")
        for z in array_2:
            for a in z:
                for b in a:
                    print(b,end=" ")
NumpyArrays.MultiDimArrays()
