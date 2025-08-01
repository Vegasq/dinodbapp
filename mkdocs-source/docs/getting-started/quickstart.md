# Quick Start

Get up and running with DinoDB in just a few minutes.

## Step 1: Add Your First AWS Account

### Using AWS Credentials File
If you have `~/.aws/credentials` configured:
1. Launch DinoDB
2. Your AWS profiles will appear automatically
3. Double-click a profile to connect

### Manual Account Setup
1. Click **"Add Account"**
2. Fill in the form:
   - **Name**: "My AWS Account"
   - **Access Key ID**: Your AWS access key
   - **Secret Access Key**: Your AWS secret key
   - **Region**: Your preferred region (e.g., us-east-1)
   - **Tags**: Optional labels (e.g., "production", "development")
3. Click **"Save"**

## Step 2: Connect to Your Account

1. Double-click your account card
2. Wait for the connection to establish
3. You'll see your DynamoDB tables in the sidebar

## Step 3: Browse Your Tables

### Table List View
- Tables appear in the left sidebar
- Click any table to view its data
- Use the search box to filter tables
- Star tables to mark as favorites

### Table Data View
- **Table View**: Spreadsheet-like interface
- **JSON View**: Raw DynamoDB JSON format
- **Pagination**: Navigate through large datasets
- **Sorting**: Click column headers to sort

## Step 4: Perform Basic Operations

### View Items
1. Select a table from the sidebar
2. Browse items in the main view
3. Click any item to see details

### Add New Item
1. Click **"Add Item"** button
2. Use the JSON editor or form fields
3. Click **"Save"** to create the item

### Edit Existing Item
1. Double-click an item in the table
2. Modify values in the detail view
3. Click **"Save Changes"**

### Delete Item
1. Select an item
2. Press **Delete** key or right-click > Delete
3. Confirm the deletion

## Step 5: Explore Advanced Features

### Query Builder
1. Click **"Query"** in the toolbar
2. Select your partition key
3. Add conditions for sort keys
4. Click **"Run Query"**

### Monitoring Dashboard
1. Select a table
2. Click the **"Metrics"** tab
3. View real-time CloudWatch metrics
4. Set up alerts for important thresholds

### Settings & Preferences
1. Click the gear icon in the toolbar
2. Customize:
   - Theme (Light/Dark/System)
   - Default page sizes
   - Auto-refresh intervals
   - Keyboard shortcuts

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