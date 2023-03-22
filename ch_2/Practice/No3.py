import cv2 as cv
import sys

if __name__ == '__main__':
    img1 = cv.imread("C:\ComputerVision\source\ch2\girl_laughing.jpg")
    img2 = cv.imread("C:\ComputerVision\source\ch2\soccer.jpg")

    if img1 is None :
        sys.exit("파일1을 찾을 수 없습니다")
    elif img2 is None:
        sys.exit("파일2를 찾을 수 없습니다.")

    cv.imshow("Img1", img1)
    cv.imshow("Img2",img2)

    cv.waitKey()
    cv.destroyAllWindows()