
"""
@author: Sanan Suleymanov
"""
import numpy as np
import math


class convolution():
    
      def __init__(self, image):
          self.image = image
    
      def convol(self, kernel, kernel_width : int,
                kernel_height : int) -> np.ndarray :
        
         if (kernel_width%2 ==0 & kernel_height%2==0):
            
            print("Kernel sizes are odd")
            
         image_pad = np.zeros((self.image.shape[0] + (kernel_height - 1), 
                          self.image.shape[1]+(kernel_width-1)))
    
         image_pad[(kernel_height-1)//2: image_pad.shape[0]-(kernel_height-1)//2, 
              (kernel_width-1)//2:image_pad.shape[1]-(kernel_width-1)//2]=self.image
         image_new = np.zeros((self.image.shape[0], self.image.shape[1]))
         for i in range (image_pad.shape[0]-kernel_height+1):
            for j in range (image_pad.shape[1]-kernel_width+1):
                image_new[i,j] = (np.multiply(image_pad[i:i+kernel_height, j:j+kernel_width], kernel)).sum()
        
        
         return image_new

class gaussian_blur(convolution):
    
    def gaus(self, sigma):
        radius = int(math.ceil(3*sigma))
    
        size=2*radius+1
    
        x = np.arange(-radius, radius+1 , 1)
        y = np.arange(-radius, radius+1, 1)
        xx,yy = np.meshgrid(x,y)
        h = np.exp(-(xx*xx+yy*yy)/(2*sigma*sigma))
   
        sumh = h.sum()
        if sumh != 0:
          h /= sumh
   
        return super().convol(h, size, size)    
    

