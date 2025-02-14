#!/usr/bin/env python3

import os
import time
import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader

# =========================
# CONFIGURATION
# =========================
# OUTPUT_DIR = "docs"
# MKDOCS_CONFIG = "mkdocs.yml"
# TEMPLATE_DIR = "docs/templates"
# TEMPLATE_FILE = "table_template.html"
# LEADERBOARD_FILE = f"{OUTPUT_DIR}/leaderboard.md"

# # =========================
# # SAMPLE DATA
# # =========================
# data = {
#     "Model Name": ["AI Model 1", "AI Model 2", "AI Model 3"],
#     "Accuracy (%)": [94.5, 92.3, 90.8],
#     "MSE": [0.0034, 0.0051, 0.0078],
#     "RMSE": [0.058, 0.071, 0.089],
#     "MAE": [0.042, 0.054, 0.065]
# }
# df = pd.DataFrame(data)

# # =========================
# # TEMPLATE FUNCTION
# # =========================
# def create_markdown_table(template_path, template_file, table_data):
#     """
#     Generate a Markdown table using Jinja2 template.

#     Args:
#         template_path (str): Path to template directory.
#         template_file (str): Template file name.
#         table_data (pd.DataFrame): Data to populate the table.

#     Returns:
#         str: Rendered Markdown content.
#     """
#     # Set up Jinja2 environment
#     env = Environment(loader=FileSystemLoader(template_path))
#     template = env.get_template(template_file)

#     # Render template
#     return template.render(
#         current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
#         table_headers=table_data.columns.tolist(),
#         table_rows=table_data.values.tolist()
#     )

# # =========================
# # WRITE MARKDOWN FILE
# # =========================
# def save_markdown(content, output_file):
#     """
#     Save rendered Markdown content to file.

#     Args:
#         content (str): Markdown content.
#         output_file (str): Output Markdown file path.
#     """
#     os.makedirs(os.path.dirname(output_file), exist_ok=True)
#     with open(output_file, "w", encoding="utf-8") as file:
#         file.write(content)
#     print(f"✅ Generated: {output_file}")

# # =========================
# # UPDATE MKDOCS NAVIGATION
# # =========================
# def update_mkdocs_nav(config_file, page_name, page_path):
#     """
#     Update MkDocs navigation by adding a new page.

#     Args:
#         config_file (str): MkDocs YAML configuration file.
#         page_name (str): Display name of the page.
#         page_path (str): File path of the new page.
#     """
#     with open(config_file, "r", encoding="utf-8") as file:
#         config = yaml.safe_load(file)

#     # Add to navigation if not already present
#     if "nav" not in config:
#         config["nav"] = []
    
#     if {page_name: page_path} not in config["nav"]:
#         config["nav"].append({page_name: page_path})

#         with open(config_file, "w", encoding="utf-8") as file:
#             yaml.dump(config, file, default_flow_style=False, sort_keys=False)
#         print(f"✅ Updated: {config_file} (Added {page_name})")

# # =========================
# # MAIN EXECUTION
# # =========================
# if __name__ == "__main__":
#     # Generate leaderboard markdown content
#     markdown_content = create_markdown_table(TEMPLATE_DIR, TEMPLATE_FILE, df)

#     # Save to Markdown file
#     save_markdown(markdown_content, LEADERBOARD_FILE)

#     # Update MkDocs navigation
#     update_mkdocs_nav(MKDOCS_CONFIG, "Leaderboard", "leaderboard.md")

#     print("\n🎉 Leaderboard successfully generated! Run `mkdocs serve` to preview.")
import os
import time
import pandas as pd
from jinja2 import Environment, FileSystemLoader

def create_table_from_template(template, table_data, table_headers):
    """
    Generate an HTML table using Jinja2 template.

    Args:
        template (tuple): Tuple containing template path and template filename.
        table_data (list of dicts): List where each dict represents a table row.
        table_headers (list): List of column headers.

    Returns:
        str: Rendered HTML content.
    """
    environment = Environment(loader=FileSystemLoader(template[0]))
    template = environment.get_template(template[1])
    content = template.render(
        current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        table_headers=table_headers,
        table_data=table_data
    )
    return content

if __name__ == "__main__":
    # Example Table Headers
    headers = ["Col Num", "Species Name", "No. of Species", "No. of Param"]
    
    # Example Data (Each dictionary is a row in the table)
    table_data = [
        {"col_num": 1, "species_name": "Species A", "no_of_species": 25, "no_of_param": 4},
        {"col_num": 2, "species_name": "Species B", "no_of_species": 40, "no_of_param": 6},
        {"col_num": 3, "species_name": "Species C", "no_of_species": 15, "no_of_param": 3}
    ]

    # Define template path (ensure the correct directory)
    template_path = "docs/templates"
    template_file = "table_template.html"

    # Generate the HTML table content
    html_table = create_table_from_template((template_path, template_file), table_data, headers)

    # Save output to a file
    output_file = "./output_table.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_table)
    
    print(f"Table generated and saved in {output_file}")
