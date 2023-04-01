import cv2 as cv

img = cv.imread("C:/ComputerVision/source/ch3/rose.png")

def draw(event, x, y, flags, param):
    global ix,iy,patch

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy),(x,y),(255,0,0),3)
        patch = img[ix:x, iy:y,:]
        patch1 = cv.resize(patch, dsize=(0,0),fx = 0.5, fy = 0.5, interpolation = cv.INTER_NEAREST)
        patch2 = cv.resize(patch, dsize=(0,0),fx = 0.5, fy = 0.5, interpolation = cv.INTER_LINEAR)
        patch3 = cv.resize(patch, dsize=(0,0),fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)

        cv.imshow('Resize nearest', patch1)
        cv.imshow('Resize bilinear', patch2)
        cv.imshow('Resize bicublic', patch3)


    cv.imshow('Drawing',img)


cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


