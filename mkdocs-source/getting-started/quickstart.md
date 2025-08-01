# Quick Start

Master DinoDB's core features in 10 minutes. This guide walks you through your first complete workflow from connection to querying data.

!!! tip "Prerequisites"
    Make sure you've completed the [Installation Guide](installation.md) and have AWS credentials ready.

## Step 1: Add Your First AWS Account

### Option A: Using AWS Credentials File (Automatic)
If you have `~/.aws/credentials` configured, DinoDB will automatically discover your profiles:

1. **Launch DinoDB** - Your AWS profiles appear automatically
2. **Profiles are marked** with a document icon 📄

![AWS Profiles Auto-Discovered](../assets/screenshots/aws-profiles-discovered.png)

3. **Double-click** any profile to connect

![Double Click to Connect](../assets/screenshots/double-click-connect.png)

### Option B: Manual Account Setup
For new AWS credentials or additional accounts:

1. **Click "Add Account"** in the main window

![Add Account Button Main](../assets/screenshots/add-account-button-main.png)

2. **Fill the account form** with your AWS details:

![Quick Start Add Account Form](../assets/screenshots/quickstart-add-account-form.png)

   - **Name**: "My Development Account" (descriptive name)
   - **Access Key ID**: `AKIA...` (your AWS access key)
   - **Secret Access Key**: `wJalr...` (your AWS secret key)
   - **Region**: `us-east-1` (your preferred region)
   - **Tags**: `development`, `testing` (optional labels)

3. **Click "Save"** - Credentials stored securely in Keychain

![Account Save Success](../assets/screenshots/account-save-success.png)

## Step 2: Connect to Your Account

### Connecting Process
1. **Double-click** your account card to initiate connection

![Account Card Ready](../assets/screenshots/account-card-ready.png)

2. **Watch the connection status** - The border changes color:
   - 🔵 **Blue border**: Successfully connected
   - 🔴 **Red border**: Connection error
   - ⚪ **Gray border**: Disconnected

![Account Connection Status](../assets/screenshots/quickstart-connection-status.png)

3. **Tables appear** in the sidebar once connected

![Sidebar Tables Loaded](../assets/screenshots/sidebar-tables-loaded.png)

!!! success "Connected!"
    When you see your DynamoDB tables in the left sidebar, you're successfully connected!

## Step 3: Browse Your Tables

### Understanding the Interface
DinoDB shows your tables in a clean, organized sidebar:

![Table List Sidebar](../assets/screenshots/table-list-sidebar.png)

- **Search Box**: Filter tables by name
- **Star Icon**: Mark tables as favorites
- **Table Count**: Shows total number of tables
- **Recent Tables**: Quick access to recently viewed tables

### Selecting a Table
**Click any table** to view its data in the main content area:

![Table Selection](../assets/screenshots/table-selection-click.png)

### Data View Modes
DinoDB offers two ways to view your table data:

#### Table View (Default)
Spreadsheet-like interface for easy data browsing:

![Table View Mode](../assets/screenshots/table-view-mode.png)

- **Sortable columns**: Click headers to sort
- **Row selection**: Click rows to select items
- **Pagination controls**: Navigate large datasets
- **Column resizing**: Drag column borders

#### JSON View
Raw DynamoDB JSON format with syntax highlighting:

![JSON View Mode](../assets/screenshots/json-view-mode.png)

- **Syntax highlighting**: Color-coded JSON
- **Copy functionality**: Easy copy/paste
- **Format validation**: Error highlighting
- **Expandable sections**: Collapse large objects

**Switch between views** using the toggle buttons:

![View Mode Toggle](../assets/screenshots/view-mode-toggle.png)

## Step 4: Perform Basic Operations

Now let's learn the essential CRUD operations with real examples.

### Viewing Items
Browse your table data with powerful navigation tools:

![Item Browsing](../assets/screenshots/item-browsing.png)

1. **Select a table** from the sidebar
2. **Browse items** using pagination controls
3. **Click any item** to view full details in a popup

![Item Detail Popup](../assets/screenshots/item-detail-popup.png)

### Adding New Items
Create new records in your DynamoDB table:

1. **Click "Add Item"** button in the toolbar

![Add Item Button Toolbar](../assets/screenshots/add-item-button-toolbar.png)

2. **Choose your input method**:

![Add Item Input Methods](../assets/screenshots/add-item-input-methods.png)

**Option A: JSON Editor**
```json
{
  "userId": {"S": "user123"},
  "email": {"S": "john@example.com"},
  "name": {"S": "John Doe"},
  "age": {"N": "30"}
}
```

**Option B: Form Fields** (easier for beginners)

![Add Item Form Fields](../assets/screenshots/add-item-form-fields.png)

3. **Click "Save"** to create the item

![Add Item Save Success](../assets/screenshots/add-item-save-success.png)

### Editing Existing Items
Modify records with inline editing:

1. **Double-click** any item in the table view

![Double Click Edit Item](../assets/screenshots/double-click-edit-item.png)

2. **Edit values** in the detail popup

![Edit Item Popup](../assets/screenshots/edit-item-popup.png)

3. **Click "Save Changes"** to update

![Edit Item Save Changes](../assets/screenshots/edit-item-save-changes.png)

!!! tip "Undo Changes"
    Click "Cancel" to discard changes, or use **Cmd+Z** to undo individual field changes.

### Deleting Items
Remove records safely with confirmation:

1. **Select an item** by clicking its row

![Select Item Row](../assets/screenshots/select-item-row.png)

2. **Delete using**:
   - **Delete key** on keyboard
   - **Right-click** → "Delete Item"

![Right Click Delete](../assets/screenshots/right-click-delete.png)

3. **Confirm deletion** in the safety dialog

![Delete Confirmation Dialog](../assets/screenshots/delete-confirmation-dialog.png)

!!! warning "Permanent Action"
    Deleting items from DynamoDB is permanent. There's no built-in undo functionality.

## Step 5: Explore Advanced Features

### Query Builder
Build complex DynamoDB queries without writing code:

1. **Click "Query"** in the toolbar

![Query Button Toolbar](../assets/screenshots/query-button-toolbar.png)

2. **Set up your query** using the visual builder

![Query Builder Interface](../assets/screenshots/query-builder-interface.png)

   - **Partition Key**: Select from dropdown (required)
   - **Sort Key**: Add conditions (optional)
   - **Filters**: Add additional conditions
   - **Index**: Choose GSI/LSI if needed

3. **Preview the query** before running

![Query Preview](../assets/screenshots/query-preview.png)

4. **Click "Run Query"** to execute

![Query Results](../assets/screenshots/query-results.png)

!!! example "Example Query"
    **Find all orders for a customer placed after 2024-01-01:**
    - Partition Key: `customerId = "CUST123"`
    - Sort Key: `orderDate > "2024-01-01"`

### Monitoring Dashboard
Get real-time insights into your table performance:

1. **Select a table** from the sidebar
2. **Click "Metrics"** tab in the main view

![Metrics Tab Click](../assets/screenshots/metrics-tab-click.png)

3. **Explore CloudWatch metrics** with interactive charts

![Metrics Dashboard](../assets/screenshots/metrics-dashboard.png)

   - **Capacity Utilization**: Read/write usage
   - **Latency**: Request response times
   - **Errors**: Error rates and types
   - **Storage**: Table size and item count

4. **Set up alerts** for important thresholds

![Setup Alerts](../assets/screenshots/setup-alerts.png)

### Settings & Preferences
Customize DinoDB to match your workflow:

1. **Click the settings icon** ⚙️ in the toolbar

![Settings Icon Toolbar](../assets/screenshots/settings-icon-toolbar.png)

2. **Explore customization options**:

![Settings Window](../assets/screenshots/settings-window.png)

**General Settings:**
- **Theme**: Light, Dark, or System
- **Default Page Size**: 10, 25, 50, 100, 250 items
- **Auto-refresh**: Metrics update interval

**Advanced Settings:**
- **Debug Logging**: Enable for troubleshooting
- **Performance Mode**: Optimize for large datasets
- **Network Timeout**: AWS API timeout values

**Keyboard Shortcuts:**
- **⌘N**: Add new item
- **⌘R**: Refresh current view
- **⌘F**: Focus search box
- **Delete**: Delete selected item
- **⌘,**: Open settings

## Common Workflows

### Switching Between AWS Accounts
Work with multiple environments seamlessly:

![Multiple Accounts](../assets/screenshots/multiple-accounts.png)

- **Click different account cards** to switch contexts
- **Active account** shows blue border
- **Each account** maintains independent connection state

### Managing Multiple Regions
Access tables across different AWS regions:

1. **Add separate accounts** for each region
2. **Or edit account settings** to change region

![Edit Account Region](../assets/screenshots/edit-account-region.png)

3. **Tables refresh automatically** after region change

### Working with Large Tables
Optimize performance for large datasets:

![Large Table Pagination](../assets/screenshots/large-table-pagination.png)

- **Adjust page size** based on your needs
- **Use queries** instead of scans when possible
- **Enable filters** to reduce data transfer

## Essential Keyboard Shortcuts

Master these shortcuts to work faster:

| Shortcut | Action |
|----------|--------|
| **⌘N** | Add new item |
| **⌘R** | Refresh current view |
| **⌘F** | Focus search box |
| **Delete** | Delete selected item |
| **⌘,** | Open settings |
| **⌘⇧T** | Switch table view mode |
| **⌘1-9** | Switch between accounts |
| **⌘Q** | Quit DinoDB |

## Success Tips

!!! tip "Performance Best Practices"
    - **Use pagination** for large tables (>1000 items)
    - **Set appropriate page sizes** in settings (25-50 for most use cases)
    - **Use queries with partition keys** instead of full table scans
    - **Monitor capacity utilization** to avoid throttling

!!! warning "Security Guidelines"
    - **Never share AWS credentials** with others
    - **Use IAM roles** with minimal required permissions
    - **Regularly rotate access keys** (every 90 days)
    - **Enable AWS CloudTrail** for audit logging

!!! info "Monitoring Recommendations"
    - **Set up CloudWatch alerts** for capacity utilization >80%
    - **Monitor error rates** and investigate spikes
    - **Watch for throttling events** in metrics dashboard
    - **Review costs** regularly in AWS Cost Explorer

## What's Next?

🎉 **Congratulations!** You've mastered DinoDB basics. Here's what to explore next:

### Immediate Next Steps
1. **[Account Management](../user-guide/account-management.md)** - Advanced account features
2. **[Table Operations](../user-guide/table-operations.md)** - Deep dive into CRUD operations
3. **[Query Builder](../user-guide/query-builder.md)** - Master complex queries

### Advanced Features
4. **[Monitoring & Metrics](../user-guide/monitoring.md)** - Set up comprehensive monitoring
5. **Performance Optimization** - Tune your queries and capacity
6. **Data Export/Import** - Bulk operations and backups

### Get Help
- 📖 **Browse User Guide** for detailed tutorials
- 🐛 **Report Issues** on [GitHub](https://github.com/vegasq/dinodbapp/issues)
- 💬 **Join Community** for tips and best practices

---

### Video Tutorial
🎥 **Watch the complete quick start walkthrough** (10 minutes):
[DinoDB Quick Start Tutorial](https://youtu.be/PLACEHOLDER_VIDEO_ID)

**Ready to become a DinoDB power user?** Continue to the detailed [User Guide](../user-guide/account-management.md)!