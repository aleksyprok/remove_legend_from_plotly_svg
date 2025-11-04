import os

from lxml import etree

root_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(root_dir, "input_svgs")
output_dir = os.path.join(root_dir, "output_svgs")


# --- input and output files ---
# input_svg = os.path.join(input_dir, "gsfit_blue_rtgsfit_orange_14684_50ms_limited_w_legend.svg")
# output_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_50ms_limited_wo_legend.svg")
# input_svg = os.path.join(input_dir, "rtgsfit_orange_pfit_green_14684_50ms_limitied_w_legend.svg")
# output_svg = os.path.join(output_dir, "rtgsfit_orange_pfit_green_14684_50ms_limitied_wo_legend.svg")
# input_svg = os.path.join(input_dir, "gsfit_blue_pfit_green_14684_248ms_weird_pfit_w_legend.svg")
# output_svg = os.path.join(output_dir, "gsfit_blue_pfit_green_14684_248ms_weird_pfit_wo_legend.svg")
# input_svg = os.path.join(input_dir, "gsfit_blue_rtgsfit_orange_14684_248ms_weird_pfit_w_legend.svg")
# output_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_248ms_weird_pfit_wo_legend.svg")
input_svg = os.path.join(input_dir, "gsfit_blue_rtgsfit_orange_14684_150ms_diverted_w_legend.svg")
output_svg = os.path.join(output_dir, "gsfit_blue_rtgsfit_orange_14684_150ms_diverted_wo_legend.svg")

# --- parse SVG ---
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(input_svg, parser)
root = tree.getroot()

# --- find and remove legend groups ---
legends = root.xpath(".//svg:g[@class='legend']", namespaces={"svg": "http://www.w3.org/2000/svg"})
print(f"Found {len(legends)} legend(s)")

for legend in legends:
    parent = legend.getparent()
    if parent is not None:
        parent.remove(legend)

# --- save cleaned SVG ---
tree.write(output_svg, pretty_print=True, xml_declaration=True, encoding="utf-8")
print(f"Saved cleaned SVG to {output_svg}")
