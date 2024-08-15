#   Source:
#!  https://github.com/amitt1236/Gaze_estimation/blob/master/gaze.py
import cv2
import numpy as np
from helpers import relative, relativeT


def gaze(frame, points):
    """
    The gaze function gets an image and face landmarks from mediapipe framework.
    The function draws the gaze direction into the frame.
    """

    '''
    2D image points.
    relative takes mediapipe points that is normalized to [-1, 1] and returns image points
    at (x,y) format
    '''
    image_points = np.array([
        relative(points.landmark[4], frame.shape),  # Nose tip
        relative(points.landmark[152], frame.shape),  # Chin
        relative(points.landmark[263], frame.shape),  # Left eye left corner
        relative(points.landmark[33], frame.shape),  # Right eye right corner
        relative(points.landmark[287], frame.shape),  # Left Mouth corner
        relative(points.landmark[57], frame.shape)  # Right mouth corner
    ], dtype="double")

    '''
    2D image points.
    relativeT takes mediapipe points that is normalized to [-1, 1] and returns image points
    at (x,y,0) format
    '''
    image_points1 = np.array([
        relativeT(points.landmark[4], frame.shape),  # Nose tip
        relativeT(points.landmark[152], frame.shape),  # Chin
        relativeT(points.landmark[263], frame.shape),  # Left eye, left corner
        relativeT(points.landmark[33], frame.shape),  # Right eye, right corner
        relativeT(points.landmark[287], frame.shape),  # Left Mouth corner
        relativeT(points.landmark[57], frame.shape)  # Right mouth corner
    ], dtype="double")

    # 3D model points.
    model_points = np.array([
        (0.0, 0.0, 0.0),  # Nose tip
        (0, -63.6, -12.5),  # Chin
        (-43.3, 32.7, -26),  # Left eye, left corner
        (43.3, 32.7, -26),  # Right eye, right corner
        (-28.9, -28.9, -24.1),  # Left Mouth corner
        (28.9, -28.9, -24.1)  # Right mouth corner
    ])

    '''
    3D model eye points
    The center of the eye ball
    '''
    Eye_ball_center_right = np.array([[-29.05], [32.7], [-39.5]])
    Eye_ball_center_left = np.array([[29.05], [32.7], [-39.5]])  # the center of the left eyeball as a vector.

    '''
    camera matrix estimation
    '''
    focal_length = frame.shape[1]
    center = (frame.shape[1] / 2, frame.shape[0] / 2)
    camera_matrix = np.array(
        [[focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]], dtype="double"
    )

    dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
    (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix,
                                                                dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

    # 2d pupil location
    left_pupil = relative(points.landmark[468], frame.shape)
    right_pupil = relative(points.landmark[473], frame.shape)

    # Transformation between image point to world point
    _, transformation, _ = cv2.estimateAffine3D(image_points1, model_points)  # image to world transformation

    if transformation is not None:  # if estimateAffine3D secsseded
        # project pupil image point into 3d world point 
        l_pupil_world_cord = transformation @ np.array([[left_pupil[0], left_pupil[1], 0, 1]]).T
        r_pupil_world_cord = transformation @ np.array([[right_pupil[0], right_pupil[1], 0, 1]]).T

        # 3D gaze point (10 is arbitrary value denoting gaze distance)
        L_S = Eye_ball_center_left + (l_pupil_world_cord - Eye_ball_center_left) * 10
        R_S = Eye_ball_center_right + (r_pupil_world_cord - Eye_ball_center_right) * 10

        # Project a 3D gaze direction onto the image plane.
        (l_eye_pupil2D, _) = cv2.projectPoints((int(L_S[0]), int(L_S[1]), int(L_S[2])), rotation_vector,
                                            translation_vector, camera_matrix, dist_coeffs)
        (r_eye_pupil2D, _) = cv2.projectPoints((int(R_S[0]), int(R_S[1]), int(R_S[2])), rotation_vector,
                                            translation_vector, camera_matrix, dist_coeffs)
        # project 3D head pose into the image plane
        (l_head_pose, _) = cv2.projectPoints((int(l_pupil_world_cord[0]), int(l_pupil_world_cord[1]), int(40)),
                                        rotation_vector,
                                        translation_vector, camera_matrix, dist_coeffs)
        (r_head_pose, _) = cv2.projectPoints((int(r_pupil_world_cord[0]), int(r_pupil_world_cord[1]), int(40)),
                                        rotation_vector,
                                        translation_vector, camera_matrix, dist_coeffs)
        # correct gaze for head rotation
        l_gaze = left_pupil + (l_eye_pupil2D[0][0] - left_pupil) - (l_head_pose[0][0] - left_pupil)
        r_gaze = right_pupil + (r_eye_pupil2D[0][0] - right_pupil) - (r_head_pose[0][0] - right_pupil)


        # Draw gaze line into screen
        lp1 = (int(left_pupil[0]), int(left_pupil[1]))
        lp2 = (int(l_gaze[0]), int(l_gaze[1]))
        cv2.line(frame, lp1, lp2, (0, 0, 255), 2)
        rp1 = (int(right_pupil[0]), int(right_pupil[1]))
        rp2 = (int(r_gaze[0]), int(r_gaze[1]))
        cv2.line(frame, rp1, rp2, (0, 255, 0), 2)
        return get_gaze_distance(lp1, lp2, rp1, rp2)

def gaze_distance(position1, position2):
    """
    The function calculates the distance between two points in 2D space.
    """
    return np.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)


def gaze_direction(position1, position2):
    """
    The function calculates the direction of gaze in 2D space.
    """
    return np.arctan2(position2[1] - position1[1], position2[0] - position1[0]) * 180 / np.pi

def get_gaze_distance(lp1, lp2, rp1, rp2):
    """
    The function calculates the distance between two points in 2D space.
    """
    return np.sqrt((lp1[0] - lp2[0]) ** 2 + (lp1[1] - lp2[1]) ** 2), np.sqrt((rp1[0] - rp2[0]) ** 2 + (rp1[1] - rp2[1]) ** 2)
