# Screenshots Needed for DinoDB Documentation

This document lists all screenshots required for the enhanced documentation. Screenshots should be taken at **2x resolution** for crisp display on retina displays.

## File Organization
- **Location**: `/Users/vegasq/Projects/dinodbapp/mkdocs-source/assets/screenshots/`
- **Format**: PNG format preferred
- **Naming**: Use exact filename from this list
- **Resolution**: 2x/Retina resolution for clarity

## Installation Guide Screenshots

### Download & Installation
- [ ] `download-website.png` - DinoDB website download page showing "Download for macOS" button
- [ ] `dmg-installation.png` - Open DMG file showing drag-to-Applications folder
- [ ] `github-releases.png` - GitHub releases page with latest DinoDB.dmg in Assets
- [ ] `applications-folder.png` - macOS Applications folder with DinoDB app visible

### Security & First Launch
- [ ] `security-warning.png` - macOS security dialog when first opening DinoDB
- [ ] `privacy-security-settings.png` - System Settings > Privacy & Security showing DinoDB warning
- [ ] `security-confirmation.png` - Final "Open" confirmation dialog
- [ ] `right-click-open.png` - Context menu showing "Open" option for DinoDB app
- [ ] `welcome-screen.png` - DinoDB welcome screen on first successful launch

### AWS Configuration
- [ ] `aws-credentials-file.png` - Terminal/text editor showing ~/.aws/credentials file structure
- [ ] `add-account-button.png` - Main DinoDB window highlighting "Add Account" button
- [ ] `add-account-form.png` - Add Account form with sample data filled in

### Verification
- [ ] `accounts-from-aws-file.png` - DinoDB showing automatically discovered AWS profiles
- [ ] `welcome-add-account.png` - Clean welcome screen prompting to add first account
- [ ] `account-connection-status.png` - Account cards showing different connection states
- [ ] `tables-list-connected.png` - Sidebar showing DynamoDB tables after successful connection

## Quick Start Guide Screenshots

### Account Setup
- [ ] `aws-profiles-discovered.png` - Main window showing AWS profiles with document icons
- [ ] `double-click-connect.png` - Mouse cursor over account card ready to double-click
- [ ] `add-account-button-main.png` - "Add Account" button in main interface
- [ ] `quickstart-add-account-form.png` - Add account form with example development account data
- [ ] `account-save-success.png` - Success confirmation after saving account

### Connection Process
- [ ] `account-card-ready.png` - Account card in disconnected state ready to connect
- [ ] `quickstart-connection-status.png` - Account cards showing blue/red/gray border states
- [ ] `sidebar-tables-loaded.png` - Left sidebar populated with DynamoDB tables

### Table Browsing
- [ ] `table-list-sidebar.png` - Complete sidebar showing search, favorites, and table list
- [ ] `table-selection-click.png` - Mouse cursor clicking on a table name in sidebar
- [ ] `table-view-mode.png` - Main content area showing table data in spreadsheet format
- [ ] `json-view-mode.png` - Same table data displayed in JSON format with syntax highlighting
- [ ] `view-mode-toggle.png` - Toggle buttons for switching between Table/JSON views

### CRUD Operations
- [+] `item-browsing.png` - Table view with pagination controls and multiple data rows
- [+] `item-detail-popup.png` - Popup window showing detailed view of a single item
- [*] `add-item-button-toolbar.png` - Toolbar highlighting the "Add Item" button
- [*] `add-item-input-methods.png` - Add item dialog showing JSON vs Form input options
- [+] `add-item-form-fields.png` - Form-based item creation with field inputs
- [-] `add-item-save-success.png` - Success message after creating new item (no such thing)
- [+] `double-click-edit-item.png` - Mouse cursor double-clicking on table row (single click)
- [+] `edit-item-popup.png` - Edit item dialog with editable fields
- [ ] `edit-item-save-changes.png` - Save changes button in edit dialog
- [ ] `select-item-row.png` - Table row highlighted/selected for deletion
- [ ] `right-click-delete.png` - Context menu showing "Delete Item" option
- [ ] `delete-confirmation-dialog.png` - Safety confirmation dialog for item deletion

### Advanced Features
- [ ] `query-button-toolbar.png` - Toolbar showing "Query" button
- [ ] `query-builder-interface.png` - Query builder with partition key, sort key, and filter options
- [ ] `query-preview.png` - Generated query preview before execution
- [ ] `query-results.png` - Query results displayed in table format
- [ ] `metrics-tab-click.png` - Table detail view showing "Metrics" tab
- [ ] `metrics-dashboard.png` - CloudWatch metrics dashboard with charts
- [ ] `setup-alerts.png` - Alert configuration dialog
- [ ] `settings-icon-toolbar.png` - Settings gear icon in toolbar
- [ ] `settings-window.png` - Settings window with tabs and options

### Workflows
- [ ] `multiple-accounts.png` - Main window showing multiple account cards
- [ ] `edit-account-region.png` - Edit account dialog highlighting region dropdown
- [ ] `large-table-pagination.png` - Table view with pagination controls for large dataset

## User Guide Screenshots (Future)

### Account Management
- [ ] `account-management-overview.png` - Accounts view with mixed AWS profiles and stored accounts
- [ ] `account-tags-system.png` - Account cards showing various colored tags
- [ ] `account-editing-form.png` - Edit account dialog with all fields visible
- [ ] `credential-security-keychain.png` - macOS Keychain showing DinoDB entries

### Table Operations
- [ ] `table-operations-overview.png` - Complete table operations interface
- [ ] `crud-operations-toolbar.png` - Table toolbar with all CRUD action buttons
- [ ] `bulk-operations.png` - Multi-select with bulk operation options
- [ ] `table-schema-view.png` - Table information panel showing schema details

### Query Builder
- [ ] `query-builder-complete.png` - Fully configured complex query
- [ ] `index-selection-dropdown.png` - GSI/LSI selection dropdown
- [ ] `filter-expressions-builder.png` - Visual filter expression builder
- [ ] `saved-queries-panel.png` - Saved query templates and history

### Monitoring
- [ ] `monitoring-dashboard-full.png` - Complete monitoring dashboard with all metrics
- [ ] `alert-configuration-detailed.png` - Detailed alert setup with all options
- [ ] `alert-notifications.png` - macOS notification for triggered alert
- [ ] `performance-trends.png` - Long-term performance trend charts

## Screenshot Guidelines

### Technical Requirements
- **Resolution**: Capture at 2x/Retina resolution (minimum 1440px wide for main windows)
- **Format**: PNG with transparency where appropriate
- **Quality**: Lossless compression, no artifacts
- **Consistency**: Same window size and zoom level across related screenshots

### Content Requirements
- **Sample Data**: Use realistic but generic sample data (no real customer information)
- **Clean Interface**: No debug panels, temporary notifications, or error states unless specifically required
- **Consistent Theme**: Use the same theme (light/dark) throughout a section
- **Cursor Position**: Show mouse cursor in screenshots demonstrating click actions

### Sample Data Suggestions
```json
// Sample DynamoDB table data
{
  "userId": {"S": "user123"},
  "email": {"S": "john@example.com"},  
  "name": {"S": "John Doe"},
  "age": {"N": "30"},
  "department": {"S": "Engineering"},
  "lastLogin": {"S": "2024-01-15T10:30:00Z"}
}
```

**Table Names**: `Users`, `Orders`, `Products`, `Analytics`
**Account Names**: `Development`, `Production`, `Staging`, `Personal`
**Tags**: `dev`, `prod`, `testing`, `us-east-1`, `critical`

## Priority Order
1. **Installation screenshots** (highest priority - blocks user onboarding)
2. **Quick start screenshots** (high priority - enables basic usage)
3. **User guide screenshots** (medium priority - enhances advanced features)

## Checklist Status
- [ ] All installation screenshots captured
- [ ] All quick start screenshots captured  
- [ ] Screenshots reviewed for consistency
- [ ] Sample data verified as generic/safe
- [ ] File naming verified against documentation links
- [ ] 2x resolution confirmed for all images

---
**Total Screenshots Needed**: 51
**Installation Guide**: 13 screenshots
**Quick Start Guide**: 38 screenshots
**Future User Guide**: TBD (additional sections)
