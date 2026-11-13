import numpy as np
from .scene_object import SceneObject


class Camera(SceneObject):
    def __init__(self, fov=60.0, aspect=16/9, near=0.1, far=100.0, **kwargs):
        super().__init__(**kwargs)
        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

    def view_matrix(self) -> np.ndarray:
        return self.world2object()

    def projection_matrix(self) -> np.ndarray:
        fov_rad = np.radians(self.fov)
        t = np.tan(fov_rad / 2)
        n, f = self.near, self.far

        return np.array([
            [1 / (self.aspect * t), 0,     0,                  0],
            [0,                     1 / t, 0,                  0],
            [0,                     0,     -(f + n) / (f - n), -2 * f * n / (f - n)],
            [0,                     0,     -1,                 0],
        ], dtype=np.float64)
