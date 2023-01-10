import cv2
import numpy as np


class Vision:
    
    needle_img = None
    needle_w = 0
    needle_h = 0

    
    
    def __init__(self, needle_img_path, method=cv2.TM_CCOEFF_NORMED):
        self.needle_img = cv2.imread(needle_img_path)
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]
        self.method = method
        
    
        
    def find(self, img_base, threshold=0.5, debug_mode=None):
        
        result = cv2.matchTemplate(img_base, self.needle_img, self.method)
        
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        
        rectangles = []

        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            rectangles.append(rect)
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        points = []
        if len(rectangles):
            print('Ladybug found')
            line_color = (0, 255, 0)
            line_type = cv2.LINE_4
            marker_color = (0, 255, 0)
            marker_type = cv2.MARKER_CROSS
                
            for (x, y, w,h) in rectangles:
                
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                points.append ((center_x, center_y))
                
                if debug_mode == 'rectangles':

                    top_left = (x, y)
                    bottom_right = (x + w , y + h)
                    cv2.rectangle(img_base, top_left, bottom_right, line_color, line_type)
                elif debug_mode == 'points':
                    cv2.drawMarker(img_base, (center_x, center_y), marker_color, marker_type)                
                
        if debug_mode:
            cv2.imshow('result', img_base)
            #cv2.waitKey(0)
        
        return points