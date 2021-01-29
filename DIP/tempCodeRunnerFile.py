markers3 = cv2.watershed(img, markers)
# img[markers3 == -1] = [0, 0, 255]