from lxml import etree
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(root_dir, "output_svgs")

# --- Paths ---
# input_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_50ms_limited_wo_legend.svg")
# output_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_50ms_limited_with_legend.svg")
# input_svg = os.path.join(output_dir, "rtgsfit_orange_pfit_green_14684_50ms_limitied_wo_legend.svg")
# output_svg = os.path.join(output_dir, "rtgsfit_orange_pfit_green_14684_50ms_limitied_with_legend.svg")
# input_svg = os.path.join(output_dir, "gsfit_blue_pfit_green_14684_248ms_weird_pfit_wo_legend.svg")
# output_svg = os.path.join(output_dir, "gsfit_blue_pfit_green_14684_248ms_weird_pfit_with_legend.svg")
# input_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_248ms_weird_pfit_wo_legend.svg")
# output_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_248ms_weird_pfit_with_legend.svg")
input_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_150ms_diverted_wo_legend.svg")
output_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_150ms_diverted_with_legend.svg")

# --- Parse SVG ---
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(str(input_svg), parser)
root = tree.getroot()

# --- Create a custom legend group ---
NSMAP = {"svg": "http://www.w3.org/2000/svg"}
legend_group = etree.Element("{http://www.w3.org/2000/svg}g", nsmap=NSMAP, attrib={"class": "custom-legend"})

# Move legend more to the left
legend_x = 100  # original was 500
legend_y = 50

# Background rectangle for the legend
bg_rect = etree.Element("{http://www.w3.org/2000/svg}rect", width="120", height="60",
                        x=str(legend_x), y=str(legend_y),
                        fill="white", stroke="black", stroke_width="1")
legend_group.append(bg_rect)

# Legend items with line symbols
items = [
    {"label": "GSFit", "color": "#1f77b4", "y": legend_y + 20},
    {"label": "RT-GFit", "color": "#ff7f0e", "y": legend_y + 40},
]
# items = [
#     {"label": "RT-GFit", "color": "#ff7f0e", "y": legend_y + 20},
#     {"label": "PFit", "color": "#2ca02c", "y": legend_y + 40},
# ]
# items = [
#     {"label": "GSFit", "color": "#1f77b4", "y": legend_y + 20},
#     {"label": "PFit", "color": "#2ca02c", "y": legend_y + 40},
# ]

for item in items:
    # Colored line
    line = etree.Element("{http://www.w3.org/2000/svg}line",
                         x1=str(legend_x + 5), y1=str(item["y"]),
                         x2=str(legend_x + 25), y2=str(item["y"]),
                         stroke=item["color"], **{"stroke-width": "2"})
    legend_group.append(line)
    
    # Text label
    text = etree.Element("{http://www.w3.org/2000/svg}text", x=str(legend_x + 30), y=str(item["y"] + 4),
                         fill="black", attrib={"font-family": "Arial", "font-size": "12"})
    text.text = item["label"]
    legend_group.append(text)

# --- Append the legend to the SVG ---
root.append(legend_group)

# --- Save the modified SVG ---
tree.write(str(output_svg), pretty_print=True, xml_declaration=True, encoding="utf-8")

print(f"Saved SVG with custom line-symbol legend to {output_svg}")
