import cv2

def detect_pupil(image_path):
    
    frame = cv2.imread(image_path)

    if frame is None:
        return {"error": "Image not found"}

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)

    _, thresh = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return {"error": "No pupil detected"}

    largest = max(contours, key=cv2.contourArea)

    area = cv2.contourArea(largest)
    (x, y), radius = cv2.minEnclosingCircle(largest)

    # ✅ NORMALIZATION (FIXES YOUR PROBLEM)
    h, w = frame.shape[:2]
    normalized_radius = radius / min(w, h)

    # ✅ TRIAGE LOGIC
    if normalized_radius > 0.25:
        status = "Dilated pupil"
        priority = "HIGH"
    elif normalized_radius < 0.08:
        status = "Constricted pupil"
        priority = "MEDIUM"
    else:
        status = "Normal pupil"
        priority = "LOW"

    return {
        "pupil_area": int(area),
        "center_x": int(x),
        "center_y": int(y),
        "radius": int(radius),
        "normalized_radius": round(normalized_radius, 3),
        "status": status,
        "priority": priority
    }