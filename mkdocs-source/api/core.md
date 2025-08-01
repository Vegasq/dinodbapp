# Core Features

Overview of DinoDB's main features and capabilities.

## Account Management

DinoDB supports multiple AWS account configurations:

### AWS Credentials File Integration
- Automatically discovers accounts from `~/.aws/credentials`
- Read-only access to existing AWS profiles
- Visual distinction with document icons

### Secure Account Storage
- Store accounts directly in DinoDB
- Credentials secured in macOS Keychain
- Full editing and management capabilities

### Account Features
- Multiple account support
- Region-specific configurations
- Tag-based organization
- Connection status indicators

## Table Operations

### Data Viewing
- **Table View**: Spreadsheet-like interface with sortable columns
- **JSON View**: Syntax-highlighted DynamoDB JSON format
- **Pagination**: Configurable page sizes (10-250 items)
- **Search & Filter**: Find specific tables and data

### CRUD Operations
- **Create**: Add new items with form builder or JSON editor
- **Read**: Browse and search table data efficiently
- **Update**: Edit items with inline editing or detail views
- **Delete**: Remove items with confirmation dialogs

### Advanced Querying
- **Query Builder**: Visual interface for complex queries
- **Filter Expressions**: Attribute-based filtering
- **Index Utilization**: Automatic optimization suggestions
- **Export Options**: Multiple format support

## Monitoring & Metrics

### CloudWatch Integration
- Real-time performance metrics from AWS CloudWatch
- Interactive charts with multiple time ranges
- Automatic refresh every 60 seconds
- Historical trend analysis

### Metric Categories
- **Capacity**: Read/write capacity utilization
- **Performance**: Latency and throughput metrics
- **Errors**: User and system error tracking
- **Storage**: Item count and table size metrics

### Alert System
- Configurable threshold-based alerts
- Multiple severity levels (Info, Warning, Critical)
- Native macOS notifications
- Visual alert indicators in dashboard

## User Interface

### Modern Design
- Native macOS interface following Human Interface Guidelines
- Clean, intuitive layout optimized for productivity
- Responsive design adapting to window sizes
- Smooth animations and transitions

### Theme Support
- Light, Dark, and System theme options
- Live theme switching without restart
- Consistent styling across all views
- Accessibility support

### Navigation
- Three-column split view layout
- Sidebar for accounts and tables
- Context-sensitive detail views
- Keyboard shortcut support

*This is user-facing documentation focused on features and capabilities*