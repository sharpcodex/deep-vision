import cv2


def put_text(frame, text, x=10, y=10, font_scale=0.4, font_thickness=1, font_color=(0, 0, 255),
             font_face=cv2.FONT_HERSHEY_SIMPLEX, fill_background=True, background_color=(0, 0, 0)):
    if fill_background:
        (w, h) = cv2.getTextSize(text, fontFace=font_face, fontScale=font_scale, thickness=font_thickness)[0]
        box_coords = ((x, y + 4), (x + w - 2, y - h - 4))
        cv2.rectangle(frame, box_coords[0], box_coords[1], background_color, cv2.FILLED)
    cv2.putText(frame, text, (x, y), font_face, fontScale=font_scale, color=font_color, thickness=font_thickness)
    return frame
