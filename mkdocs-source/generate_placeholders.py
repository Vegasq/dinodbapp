#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(filename, text, width=1440, height=900):
    """Create a placeholder image with text"""
    img = Image.new('RGB', (width, height), color='#f0f0f0')
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fallback to default if not available
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 48)
        small_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
    except:
        font = ImageFont.load_default()
        small_font = font
    
    # Draw border
    draw.rectangle([(10, 10), (width-10, height-10)], outline='#cccccc', width=3)
    
    # Draw main text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 50
    draw.text((x, y), text, fill='#333333', font=font)
    
    # Draw filename
    filename_text = f"File: {filename}"
    fn_bbox = draw.textbbox((0, 0), filename_text, font=small_font)
    fn_width = fn_bbox[2] - fn_bbox[0]
    x_fn = (width - fn_width) // 2
    y_fn = y + text_height + 40
    draw.text((x_fn, y_fn), filename_text, fill='#666666', font=small_font)
    
    # Draw dimensions
    dim_text = f"{width}x{height}px"
    dim_bbox = draw.textbbox((0, 0), dim_text, font=small_font)
    dim_width = dim_bbox[2] - dim_bbox[0]
    x_dim = (width - dim_width) // 2
    y_dim = height - 60
    draw.text((x_dim, y_dim), dim_text, fill='#999999', font=small_font)
    
    return img

# Installation Guide Screenshots
installation_screenshots = [
    ("download-website.png", "Download Website"),
    ("dmg-installation.png", "DMG Installation"),
    ("github-releases.png", "GitHub Releases"),
    ("applications-folder.png", "Applications Folder"),
    ("security-warning.png", "Security Warning"),
    ("privacy-security-settings.png", "Privacy & Security Settings"),
    ("security-confirmation.png", "Security Confirmation"),
    ("right-click-open.png", "Right Click Open"),
    ("welcome-screen.png", "Welcome Screen"),
    ("aws-credentials-file.png", "AWS Credentials File"),
    ("add-account-button.png", "Add Account Button"),
    ("add-account-form.png", "Add Account Form"),
    ("accounts-from-aws-file.png", "Accounts from AWS File"),
    ("welcome-add-account.png", "Welcome Add Account"),
    ("account-connection-status.png", "Account Connection Status"),
    ("tables-list-connected.png", "Tables List Connected"),
]

# Quick Start Guide Screenshots
quickstart_screenshots = [
    ("aws-profiles-discovered.png", "AWS Profiles Discovered"),
    ("double-click-connect.png", "Double Click Connect"),
    ("add-account-button-main.png", "Add Account Button Main"),
    ("quickstart-add-account-form.png", "Quick Start Add Account Form"),
    ("account-save-success.png", "Account Save Success"),
    ("account-card-ready.png", "Account Card Ready"),
    ("quickstart-connection-status.png", "Quick Start Connection Status"),
    ("sidebar-tables-loaded.png", "Sidebar Tables Loaded"),
    ("table-list-sidebar.png", "Table List Sidebar"),
    ("table-selection-click.png", "Table Selection Click"),
    ("table-view-mode.png", "Table View Mode"),
    ("json-view-mode.png", "JSON View Mode"),
    ("view-mode-toggle.png", "View Mode Toggle"),
    ("item-browsing.png", "Item Browsing"),
    ("item-detail-popup.png", "Item Detail Popup"),
    ("add-item-button-toolbar.png", "Add Item Button Toolbar"),
    ("add-item-input-methods.png", "Add Item Input Methods"),
    ("add-item-form-fields.png", "Add Item Form Fields"),
    ("add-item-save-success.png", "Add Item Save Success"),
    ("double-click-edit-item.png", "Double Click Edit Item"),
    ("edit-item-popup.png", "Edit Item Popup"),
    ("edit-item-save-changes.png", "Edit Item Save Changes"),
    ("select-item-row.png", "Select Item Row"),
    ("right-click-delete.png", "Right Click Delete"),
    ("delete-confirmation-dialog.png", "Delete Confirmation Dialog"),
    ("query-button-toolbar.png", "Query Button Toolbar"),
    ("query-builder-interface.png", "Query Builder Interface"),
    ("query-preview.png", "Query Preview"),
    ("query-results.png", "Query Results"),
    ("metrics-tab-click.png", "Metrics Tab Click"),
    ("metrics-dashboard.png", "Metrics Dashboard"),
    ("setup-alerts.png", "Setup Alerts"),
    ("settings-icon-toolbar.png", "Settings Icon Toolbar"),
    ("settings-window.png", "Settings Window"),
    ("multiple-accounts.png", "Multiple Accounts"),
    ("edit-account-region.png", "Edit Account Region"),
    ("large-table-pagination.png", "Large Table Pagination"),
]

# Future User Guide Screenshots
userguide_screenshots = [
    ("account-management-overview.png", "Account Management Overview"),
    ("account-tags-system.png", "Account Tags System"),
    ("account-editing-form.png", "Account Editing Form"),
    ("credential-security-keychain.png", "Credential Security Keychain"),
    ("table-operations-overview.png", "Table Operations Overview"),
    ("crud-operations-toolbar.png", "CRUD Operations Toolbar"),
    ("bulk-operations.png", "Bulk Operations"),
    ("table-schema-view.png", "Table Schema View"),
    ("query-builder-complete.png", "Query Builder Complete"),
    ("index-selection-dropdown.png", "Index Selection Dropdown"),
    ("filter-expressions-builder.png", "Filter Expressions Builder"),
    ("saved-queries-panel.png", "Saved Queries Panel"),
    ("monitoring-dashboard-full.png", "Monitoring Dashboard Full"),
    ("alert-configuration-detailed.png", "Alert Configuration Detailed"),
    ("alert-notifications.png", "Alert Notifications"),
    ("performance-trends.png", "Performance Trends"),
]

# Create all placeholders
output_dir = "assets/screenshots"

print("Generating placeholder screenshots...")
print(f"Output directory: {output_dir}")
print()

# Installation Guide
print("Creating Installation Guide placeholders...")
for filename, title in installation_screenshots:
    img = create_placeholder(filename, title)
    img.save(os.path.join(output_dir, filename))
    print(f"  Created: {filename}")

print()

# Quick Start Guide
print("Creating Quick Start Guide placeholders...")
for filename, title in quickstart_screenshots:
    img = create_placeholder(filename, title)
    img.save(os.path.join(output_dir, filename))
    print(f"  Created: {filename}")

print()

# User Guide (Future)
print("Creating User Guide placeholders...")
for filename, title in userguide_screenshots:
    img = create_placeholder(filename, title)
    img.save(os.path.join(output_dir, filename))
    print(f"  Created: {filename}")

print()
print("All placeholder images have been created!")
print(f"Total images created: {len(installation_screenshots) + len(quickstart_screenshots) + len(userguide_screenshots)}")