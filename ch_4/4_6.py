import skimage
import numpy as np
import cv2 as cv
import time

#coffee 영상을 익어온다.
coffee = skimage.data.coffee()

# 분할하는 시작 시간을 측정
start = time.time()

# 영상을 600개의 슈퍼 화소로 분할해 slic1 객체에 저장
slic = skimage.segmentation.slic(coffee, compactness=20, n_segments = 600, start_label=1)

# rag_mean_color = 슈퍼 화소를 노드로 사용하고
# similarity를 에지 가중치로 사용한 그래프를 구성하여 g 객체에 저장
g = skimage.future.graph.rag_mean_color(coffee, slic, mode = 'similarity')

# cut_normalized 함수: slic1과 g 객체 정보를 이용하여 정규화 절단 수행, ncut에 객체 저장
ncut = skimage.future.graph.cut_normalized(slic,g)
print(coffee.shape, 'Coffee 영상을 분할하는 데', time.time()- start, '초 소요')

# 원래 영상 coffee에 영역 분할 정보를 담은 ncut 맵을 이용하여 영역 경계 표시하고 marking 객체에 저장
marking = skimage.segmentation.mark_boundaries(coffee,ncut)

# 실수를 가진 marking을 0~255 사이의 uint8형으로 변환
ncut_coffee = np.uint8(marking*255.0)

# RGB를 BGR로 변환하여 윈도우에 디스플레이
cv.imshow('Normalized cut', cv.cvtColor(ncut_coffee, cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()
