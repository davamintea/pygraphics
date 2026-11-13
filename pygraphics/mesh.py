import numpy as np
from .scene_object import SceneObject


class Mesh(SceneObject):
    def __init__(self, vertices, faces, **kwargs):
        super().__init__(**kwargs)
        self.vertices = np.asarray(vertices, dtype=np.float64)
        self.faces = np.asarray(faces, dtype=np.int32)

    def world_vertices(self) -> np.ndarray:
        n = len(self.vertices)
        homogeneous = np.ones((n, 4), dtype=np.float64)
        homogeneous[:, :3] = self.vertices
        transformed = (self.object2world() @ homogeneous.T).T
        return transformed[:, :3]
