

    for(x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 5)

        cv2.imshow("Video", image)
        k = cv2.waitKey(30) & 0xFF

        if k == 27:
            break

cv2.release()
