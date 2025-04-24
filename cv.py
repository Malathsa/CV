import cv2
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from mediapipe.python.solutions.drawing_styles import get_default_hand_landmarks_style

# فتح الكاميرا
cap = cv2.VideoCapture(0)

with Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        # تحويل الصورة إلى RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # تحليل اليد
        result = hands.process(image_rgb)

        # عرض المعالم إذا تم اكتشاف يد
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                draw_landmarks(
                    image,
                    hand_landmarks,
                    get_default_hand_landmarks_style()
                )

        # عرض الإطار
        cv2.imshow("Hand Tracking", image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()