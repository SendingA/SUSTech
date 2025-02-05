import cv2
from train import processFiles, trainSVM
from detector import Detector

# Replace these with the directories containing your
# positive and negative sample images, respectively.
pos_dir = "samples/vehicles"
neg_dir = "samples/non-vehicles"

# Replace this with the path to your test video file.
video_file = "videos/test_video.mp4"


def experiment1():
    """
    Train a classifier and run it on a video using default settings
    without saving any files to disk.
    """
    # TODO: You need to adjust hyperparameters
    # Extract HOG features from images in the sample directories and 
    # return results and parameters in a dict.
    # feature_data = processFiles(pos_dir, neg_dir, recurse=True,hog_features=True)
    feature_data = processFiles(pos_dir, neg_dir, recurse=True, hog_features=True, pix_per_cell=(4,4), cells_per_block=(4,4))


    # Train SVM and return the classifier and parameters in a dict.
    # This function takes the dict from processFiles() as an input arg.
    classifier_data = trainSVM(feature_data=feature_data)


    # TODO: You need to adjust hyperparameters of loadClassifier() and detectVideo()
    #       to obtain a better performance

    # Instantiate a Detector object and load the dict from trainSVM().
    detector = Detector().loadClassifier(classifier_data=classifier_data)
  
    # Open a VideoCapture object for the video file.
    cap = cv2.VideoCapture(video_file)

    # Start the detector by supplying it with the VideoCapture object.
    # At this point, the video will be displayed, with bounding boxes
    # drawn around detected objects per the method detailed in README.md.
    detector.detectVideo(video_capture=cap, write=False)


def experiment2():
    # 提取HOG特征和直方图特征
    feature_data = processFiles(pos_dir, neg_dir, recurse=True,
                                hog_features=True,hist_features=True,spatial_features=False,
                                pix_per_cell=(4,4), cells_per_block=(4,4))

    classifier_data = trainSVM(feature_data=feature_data)
    # 滑动窗口初始大小为32*32，x方向重叠0.9，y方向步长0.008，x方向搜索范围为0.66-0.9，y方向搜索范围为0.52-0.67，缩放因子为1.2
    detector = Detector(init_size=(32,32), x_overlap=0.9, y_step=0.008,
            x_range=(0.66, 0.9), y_range=(0.52, 0.67), scale=1.2)
    detector.loadClassifier(classifier_data=classifier_data)
    cap = cv2.VideoCapture(video_file)
    detector.detectVideo(video_capture=cap,write=True)
    print('video has saved')
    

if __name__ == "__main__":
    experiment2()
    # experiment2() may you need to try other parameters
    # experiment3 ...


