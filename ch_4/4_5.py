import skimage
import numpy as np
import cv2 as cv

# skimgae는 RGB 순서, OpenCV는 BGR순서로 저장
img = skimage.data.coffee()
cv.imshow('Coffee image',cv.cvtColor(img,cv.COLOR_RGB2BGR))

# 슈퍼화소분할 수행후 slic1 객체에 저장
# slic(이미지, 슈퍼화소 모양 조절, 슈퍼화소의 개수)
# 슈퍼화소모양 값이 클수록 네모에 가까운 모양이 만들어지는 대신, 색상 균일성은 희생됨
slic1 = skimage.segmentation.slic(img,compactness=20, n_segments=600)
sp_img1 = skimage.segmentation.mark_boundaries(img,slic1)

# 실수로 표현된 것을 0~255로 바꾸고 uint8로 변환
sp_img1 = np.uint8(sp_img1*255.0)

slic2 = skimage.segmentation.slic(img,compactness=40, n_segments = 600)
sp_img2 = skimage.segmentation.mark_boundaries(img,slic2)
sp_img2 = np.uint8(sp_img2*255.0)

cv.imshow('Super pixels (compact 20)', cv.cvtColor(sp_img1, cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40)', cv.cvtColor(sp_img2,cv.COLOR_RGB2BGR))