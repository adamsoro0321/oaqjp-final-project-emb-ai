from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        """
        test 
        """
        #1.  case  1
        response_1 =emotion_detector("I am glad this happened")
        self.assertEqual(response_1['dominant_emotion'] ,"joy")


         #2.  case  2
        response_2 =emotion_detector("I am really mad about this")
        self.assertEqual(response_2['dominant_emotion'] ,"anger")

         #3. case  3
        response_3 =emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response_3['dominant_emotion'] ,"disgust")

         #4  case  4
        response_4 =emotion_detector("I am so sad about this")
        self.assertEqual(response_4['dominant_emotion'] ,"sadness")

         #5  case  5
        response_5 =emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response_5['dominant_emotion'] ,"fear")

      

unittest.main()