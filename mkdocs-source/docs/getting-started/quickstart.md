# Quick Start

Get up and running with DinoDB in just a few minutes.

## Step 1: Add Your First AWS Account

### Using AWS Credentials File
If you have `~/.aws/credentials` configured:
1. Launch DinoDB
2. Your AWS profiles will appear automatically

![AWS Profiles Discovered](../assets/screenshots/aws-profiles-discovered.png)

3. Double-click a profile to connect

### Manual Account Setup
1. Click **"Add Account"**

![Add Account Button](../assets/screenshots/add-account-button.png)

2. Fill in the form:
   - **Name**: "My AWS Account"
   - **Access Key ID**: Your AWS access key
   - **Secret Access Key**: Your AWS secret key
   - **Region**: Your preferred region (e.g., us-east-1)
   - **Tags**: Optional labels (e.g., "production", "development")

![Add Account Form](../assets/screenshots/quickstart-add-account-form.png)

3. Click **"Save"

## Step 2: Connect to Your Account

1. Double-click your account card

![Double Click Connect](../assets/screenshots/double-click-connect.png)

2. Wait for the connection to establish

![Connection Status](../assets/screenshots/quickstart-connection-status.png)

3. You'll see your DynamoDB tables in the sidebar

![Tables List Connected](../assets/screenshots/tables-list-connected.png)

## Step 3: Browse Your Tables

### Table List View
- Tables appear in the left sidebar
- Click any table to view its data
- Use the search box to filter tables
- Star tables to mark as favorites

![Table List Sidebar](../assets/screenshots/table-list-sidebar.png)

### Table Data View
- **Table View**: Spreadsheet-like interface
- **JSON View**: Raw DynamoDB JSON format
- **Pagination**: Navigate through large datasets
- **Sorting**: Click column headers to sort

![Table View Mode](../assets/screenshots/table-view-mode.png)

## Step 4: Perform Basic Operations

### View Items
1. Select a table from the sidebar
2. Browse items in the main view
3. Click any item to see details

### Add New Item
1. Click **"Add Item"** button

![Add Item Button](../assets/screenshots/add-item-button-toolbar.png)

2. Use the JSON editor or form fields

![Add Item Form](../assets/screenshots/add-item-form-fields.png)

3. Click **"Save"** to create the item

### Edit Existing Item
1. Double-click an item in the table

![Double Click Edit Item](../assets/screenshots/double-click-edit-item.png)

2. Modify values in the detail view

![Edit Item Popup](../assets/screenshots/edit-item-popup.png)

3. Click **"Save Changes"

### Delete Item
1. Select an item
2. Press **Delete** key or right-click > Delete

![Right Click Delete](../assets/screenshots/right-click-delete.png)

3. Confirm the deletion

![Delete Confirmation Dialog](../assets/screenshots/delete-confirmation-dialog.png)

## Step 5: Explore Advanced Features

### Query Builder
1. Click **"Query"** in the toolbar

![Query Button Toolbar](../assets/screenshots/query-button-toolbar.png)

2. Select your partition key
3. Add conditions for sort keys

![Query Builder Interface](../assets/screenshots/query-builder-interface.png)

4. Click **"Run Query"

### Monitoring Dashboard
1. Select a table
2. Click the **"Metrics"** tab

![Metrics Tab Click](../assets/screenshots/metrics-tab-click.png)

3. View real-time CloudWatch metrics

![Metrics Dashboard](../assets/screenshots/metrics-dashboard.png)

4. Set up alerts for important thresholds

### Settings & Preferences
1. Click the gear icon in the toolbar

![Settings Icon Toolbar](../assets/screenshots/settings-icon-toolbar.png)

2. Customize:
   - Theme (Light/Dark/System)
   - Default page sizes
   - Auto-refresh intervals
   - Keyboard shortcuts

![Settings Window](../assets/screenshots/settings-window.png)

## Common Tasks

### Switching Between Accounts
- Click different account cards to switch contexts
- Each account maintains its own connection state
- Visual indicators show active connections

### Managing Multiple Regions
- Add separate accounts for different regions
- Or edit account settings to change regions
- Tables will refresh automatically

### Keyboard Shortcuts
- **⌘N**: Add new item
- **⌘R**: Refresh tables
- **⌘F**: Focus search
- **Delete**: Delete selected item
- **⌘,**: Open settings

## Tips for Success

!!! tip "Performance"
    - Use pagination for large tables
    - Set appropriate page sizes in settings
    - Use queries instead of scans when possible

!!! warning "Security"
    - Never share AWS credentials
    - Use IAM roles with minimal required permissions
    - Regularly rotate access keys

!!! info "Monitoring"
    - Set up CloudWatch alerts for important metrics
    - Monitor capacity utilization regularly
    - Watch for throttling events

## Next Steps

Now that you're familiar with the basics:

- Read the [User Guide](../user-guide/account-management.md) for detailed features
- Learn about [Account Management](../user-guide/account-management.md)
- Explore [Advanced Querying](../user-guide/query-builder.md)
- Set up [Monitoring & Alerts](../user-guide/monitoring.md)