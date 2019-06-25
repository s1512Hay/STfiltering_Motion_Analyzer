# -*- coding: utf-8 -*-
"""Created on Sun Dec  9 11:19:50 2018

@author: Shay Aharon"""
import cv2 as cv
import numpy as np 
import skvideo.io


def GaborSTfiltering():      
    vid = skvideo.io.vread("video_file.avi", outputdict={"-pix_fmt": "gray"})[:, :, :, 0]; #reading video    
    outputvid = np.zeros(np.shape(vid));
    for y in range(np.shape(vid)[1]):#this loop applies applies gabor energy for every t,x slice and normalizes        
        outputvid[:,y,:]= GaborEnergy(vid[:,y,:], (15, 15), 10.0, np.pi/2, 10.0, 1.0);
        cv.normalize(outputvid[:,y,:],outputvid[:,y,:],0,255,cv.NORM_MINMAX);
        skvideo.io.vwrite("outputvideo_Gabor.mp4", outputvid);#saving output video
        
        
def TapSTfiltering():
     f1  =  [0.0094,  0.1148,  0.3964, -0.0601, -0.9213, -0.0601,  0.3964,  0.1148, 0.0094];
     f2 = [0.0008, 0.0176, 0.1660, 0.6383, 1.0, 0.6383, 0.1660, 0.0176, 0.0008];
     tapkernel = np.outer(f1,f2);
     vid = skvideo.io.vread("video_file.avi", outputdict={"-pix_fmt": "gray"})[:, :, :, 0];#reading video    
     outputvid = np.zeros(np.shape(vid));
     for y in range(np.shape(vid)[1]):        
         outputvid[:,y,:] = cv.filter2D(vid[:,y,:], -1,cv.flip(tapkernel,-1));#kernel needs to be mirrored forconvolution    
     skvideo.io.vwrite("outputvideo_9tap.mp4", np.square(outputvid));#saving output 
            
def GaborEnergy(img, ksize, sigma, theta, lambd, gamma):    
     GaborKernelReal = cv.getGaborKernel(ksize, sigma, theta, lambd, gamma, 0, ktype=cv.CV_32F);#even part ofthe filter    
     GaborKernelIm = cv.getGaborKernel(ksize, sigma, theta, lambd, gamma, np.pi/2 , ktype=cv.CV_32F);#odd part    
     ConImageReal = cv.filter2D(img, -1, cv.flip(GaborKernelReal,-1));#kernel mirrored for convolution    
     ConImageIm = cv.filter2D(img, -1, cv.flip(GaborKernelIm,-1));        
     ConImageReal=np.square(ConImageReal);    
     ConImageIm=np.square(ConImageIm);
     return np.sqrt(ConImageReal+ConImageIm)
    
GaborSTfiltering()
TapSTfiltering()