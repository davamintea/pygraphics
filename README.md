# pygraphics

A Python rendering pipeline built on NumPy.

## Architecture

```
SceneObject
├── Mesh
└── Camera
```

### SceneObject

Base primitive for anything placed in a scene. Stores transformation as three components:

| Property   | Type        | Default         | Description                  |
|------------|-------------|-----------------|------------------------------|
| `position` | `float64[3]`| `[0, 0, 0]`    | World-space translation      |
| `rotation` | `float64[3]`| `[0, 0, 0]`    | Euler angles in degrees (XYZ)|
| `scale`    | `float64[3]`| `[1, 1, 1]`    | Per-axis scale factors       |

**`object2world()`** — Builds a 4×4 matrix: `T · Rz · Ry · Rx · S`

**`world2object()`** — Returns the inverse.

### Mesh

Extends `SceneObject` with geometry data.

| Property   | Type          | Description                              |
|------------|---------------|------------------------------------------|
| `vertices` | `float64[N,3]`| Vertex positions in object space         |
| `faces`    | `int32[F,K]`  | Face indices into the vertex array       |

**`world_vertices()`** — Transforms all vertices to world space via a single batched matrix multiply.

### Camera

Extends `SceneObject` with projection parameters.

| Property | Type    | Default | Description                       |
|----------|---------|---------|-----------------------------------|
| `fov`    | `float` | `60.0`  | Vertical field of view in degrees |
| `aspect` | `float` | `16/9`  | Width / height ratio              |
| `near`   | `float` | `0.1`   | Near clipping plane               |
| `far`    | `float` | `100.0` | Far clipping plane                |

**`view_matrix()`** — The world-to-camera transform (inverse of object2world).

**`projection_matrix()`** — OpenGL-style perspective projection matrix.

## Usage

```python
from pygraphics import Mesh, Camera

triangle = Mesh(
    vertices=[[0, 1, 0], [-1, -1, 0], [1, -1, 0]],
    faces=[[0, 1, 2]],
    position=[0, 0, -5],
    rotation=[0, 45, 0],
)

cam = Camera(fov=60, position=[0, 0, 0])

world_verts = triangle.world_vertices()
view = cam.view_matrix()
proj = cam.projection_matrix()
```

## Requirements

- Python 3.10+
- NumPy
