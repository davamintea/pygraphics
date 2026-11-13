import numpy as np


class SceneObject:
    def __init__(self, position=None, rotation=None, scale=None):
        self.position = np.array(position if position is not None else [0.0, 0.0, 0.0], dtype=np.float64)
        self.rotation = np.array(rotation if rotation is not None else [0.0, 0.0, 0.0], dtype=np.float64)
        self.scale = np.array(scale if scale is not None else [1.0, 1.0, 1.0], dtype=np.float64)

    def object2world(self) -> np.ndarray:
        sx, sy, sz = self.scale
        rx, ry, rz = np.radians(self.rotation)

        S = np.diag([sx, sy, sz, 1.0])

        cx, sx_ = np.cos(rx), np.sin(rx)
        Rx = np.array([
            [1,   0,    0, 0],
            [0,  cx, -sx_, 0],
            [0, sx_,   cx, 0],
            [0,   0,    0, 1],
        ])

        cy, sy_ = np.cos(ry), np.sin(ry)
        Ry = np.array([
            [ cy, 0, sy_, 0],
            [  0, 1,   0, 0],
            [-sy_, 0,  cy, 0],
            [  0, 0,   0, 1],
        ])

        cz, sz_ = np.cos(rz), np.sin(rz)
        Rz = np.array([
            [cz, -sz_, 0, 0],
            [sz_,  cz, 0, 0],
            [ 0,    0, 1, 0],
            [ 0,    0, 0, 1],
        ])

        T = np.eye(4)
        T[:3, 3] = self.position

        return T @ Rz @ Ry @ Rx @ S

    def world2object(self) -> np.ndarray:
        return np.linalg.inv(self.object2world())
