import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os
import random
import math

# ===============================
# PARAMETERS
# ===============================

canvas_size = 800          # width and height (pixels)
dot_radius = 10            # SMALL fixed radius
edge_margin = 10            # space from canvas edge
min_spacing = 4            # extra space between dots
output_folder = "dot_stimuli"

os.makedirs(output_folder, exist_ok=True)

# ===============================
# DOT GENERATION FUNCTION
# ===============================

def generate_dots(n_dots):

    dots = []
    attempts = 0
    max_attempts = 20000

    while len(dots) < n_dots and attempts < max_attempts:
        attempts += 1

        # Safe placement boundaries
        x = random.uniform(
            -canvas_size/2 + dot_radius + edge_margin,
             canvas_size/2 - dot_radius - edge_margin
        )
        y = random.uniform(
            -canvas_size/2 + dot_radius + edge_margin,
             canvas_size/2 - dot_radius - edge_margin
        )

        valid = True
        for dx, dy in dots:
            distance = math.sqrt((x - dx)**2 + (y - dy)**2)

            # STRICT non-touch condition
            if distance < (2 * dot_radius + min_spacing):
                valid = False
                break

        if valid:
            dots.append((x, y))

    if len(dots) < n_dots:
        raise RuntimeError("Could not place all dots without overlap.")

    return dots

# ===============================
# GENERATE IMAGES
# ===============================

for n in range(5, 21):

    dots = generate_dots(n)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-canvas_size/2, canvas_size/2)
    ax.set_ylim(-canvas_size/2, canvas_size/2)
    ax.set_aspect('equal')
    ax.axis('off')

    for x, y in dots:
        circle = Circle((x, y), dot_radius, color='black')
        ax.add_patch(circle)

    plt.savefig(
        f"{output_folder}/V{n}.png",
        dpi=300,
        bbox_inches='tight',
        pad_inches=0
    )

    plt.close()

print("Stimuli generated successfully.")
