import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.image import imread

root_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(root_dir, "input_svgs")
output_dir = os.path.join(root_dir, "output_svgs")

# Load the SVG (needs to be converted to PNG first for imread)
# If you want to stay SVG-native, see Option 2
img = imread("gsfit_blue_rtgsfit_orange_14684_50ms_limited_wo_legend.png")

fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(img)
ax.axis('off')  # Hide axes

# --- Create a custom legend ---
patch1 = mpatches.Patch(color='blue', label='GS Fit')
patch2 = mpatches.Patch(color='orange', label='RTG Fit')
ax.legend(handles=[patch1, patch2], loc='upper right')

plt.show()
