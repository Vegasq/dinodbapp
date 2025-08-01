# Account Management

Master DinoDB's powerful account management system for seamless multi-environment AWS workflows.

## Overview

DinoDB provides flexible account management supporting both automated discovery and manual configuration:

- **🔍 AWS Profiles**: Auto-discovered from `~/.aws/credentials` (read-only)
- **🔐 Stored Accounts**: Manually added and secured in macOS Keychain
- **🔄 Unified Interface**: Both types displayed together seamlessly
- **🏷️ Rich Metadata**: Tags, descriptions, and visual organization

![Account Management Overview](../assets/screenshots/account-management-overview.png)

## Account Types Explained

### AWS Profiles (Auto-Discovered)
**Source**: `~/.aws/credentials` and `~/.aws/config` files
**Security**: Read-only access, credentials remain in AWS files
**Identification**: Document icon 📄 on account cards

**Benefits:**
- ✅ Automatic discovery and updates
- ✅ Standard AWS CLI integration
- ✅ No credential duplication
- ✅ Team-friendly (shared configs)

**Limitations:**
- ❌ Cannot edit from within DinoDB
- ❌ Limited metadata (no tags, descriptions)
- ❌ Depends on file system access

### Stored Accounts (DinoDB Native)
**Source**: Manually added through DinoDB interface
**Security**: Encrypted storage in macOS Keychain
**Identification**: No special icon, full editing capabilities

**Benefits:**
- ✅ Rich metadata (tags, descriptions, custom names)
- ✅ Full CRUD operations within DinoDB
- ✅ Enhanced security with Keychain encryption
- ✅ Independent of file system

**Limitations:**
- ❌ Manual setup required
- ❌ Separate from AWS CLI configurations

## AWS Credentials File Integration

### Understanding AWS Configuration Files

AWS uses two main configuration files in your home directory:

**`~/.aws/credentials`** - Contains access keys and secrets
```ini title="~/.aws/credentials"
[default]
aws_access_key_id = AKIA...
aws_secret_access_key = wJalr...

[production]
aws_access_key_id = AKIA...
aws_secret_access_key = wJalr...

[development] 
aws_access_key_id = AKIA...
aws_secret_access_key = wJalr...
```

**`~/.aws/config`** - Contains regions and other settings
```ini title="~/.aws/config"
[default]
region = us-east-1
output = json

[profile production] 
region = us-west-2
output = json

[profile development]
region = us-east-1
output = table
```

### Automatic Discovery Process

DinoDB automatically scans for AWS profiles on startup and when you click "Reload":

![AWS Profiles Discovery](../assets/screenshots/aws-profiles-discovery.png)

1. **File System Scan**: Reads `~/.aws/credentials` and `~/.aws/config`
2. **Profile Parsing**: Extracts profile names, regions, and settings  
3. **Validation**: Verifies required fields are present
4. **UI Update**: Displays profiles with document icons

!!! info "Profile Updates"
    Changes to AWS files are detected when you restart DinoDB or click "Reload" in the accounts view.

## Adding Accounts

### Manual Account Creation Workflow

**Step 1: Initiate Account Creation**
Click the **"Add Account"** button in the main accounts view:

![Add Account Button](../assets/screenshots/add-account-button-accounts-view.png)

**Step 2: Complete the Account Form**
Fill in all required and optional fields:

![Account Creation Form](../assets/screenshots/account-creation-form-complete.png)

**Required Fields:**
- **Name**: Descriptive account identifier (e.g., "Production East", "Dev Environment")
- **Access Key ID**: Your AWS access key (starts with `AKIA...`)
- **Secret Access Key**: Your AWS secret access key
- **Region**: Default AWS region for this account

**Optional Fields:**
- **Description**: Detailed account purpose or notes
- **Tags**: Categorization labels for organization

**Step 3: Configure Security Settings**
Choose your security preferences:

![Security Settings](../assets/screenshots/account-security-settings.png)

- **Keychain Storage**: Always enabled for maximum security
- **Connection Timeout**: Adjust for your network conditions
- **Auto-Connect**: Enable to connect automatically on startup

**Step 4: Save and Verify**
1. Click **"Save"** to store the account
2. DinoDB encrypts credentials in macOS Keychain
3. Test connection automatically validates settings

![Account Save Success](../assets/screenshots/account-creation-success.png)

### Advanced Account Configuration

#### IAM Role Support (Coming Soon)
DinoDB will support AWS IAM roles for enhanced security:

```json title="Future: IAM Role Configuration"
{
  "roleArn": "arn:aws:iam::123456789012:role/DinoDBRole",
  "sessionName": "DinoDB-Session",
  "externalId": "unique-external-id"
}
```

#### Multi-Factor Authentication
For accounts requiring MFA, DinoDB can handle temporary credentials:

![MFA Configuration](../assets/screenshots/mfa-configuration-placeholder.png)

### Security Architecture

DinoDB implements multiple layers of security for stored accounts:

![Security Architecture](../assets/screenshots/security-architecture-diagram.png)

**Encryption at Rest:**
- Credentials encrypted using macOS Keychain Services
- AES-256 encryption with hardware security module integration
- Per-account encryption keys managed by macOS

**Access Control:**
- App-specific keychain access permissions
- User authentication required for credential access
- No credentials ever logged or cached in memory

**Network Security:**
- TLS 1.3 for all AWS API communications
- Certificate pinning for AWS endpoints
- Request signing using AWS Signature Version 4

!!! warning "Security Best Practice"
    Always use IAM users with minimal required permissions. Never use root account credentials with DinoDB.

## Managing Accounts

### Account Operations Overview
DinoDB provides comprehensive account management with visual feedback and intuitive controls:

![Account Management Interface](../assets/screenshots/account-management-interface.png)

### Individual Account Actions

#### Connecting to Accounts
**Double-click** any account card to establish connection:

![Account Connection Process](../assets/screenshots/account-connection-process.png)

**Connection States:**
- 🔵 **Connected**: Blue outline border, tables loaded
- ⚪ **Disconnected**: Gray border, ready to connect  
- 🔴 **Error**: Red border with error tooltip
- 🟡 **Connecting**: Yellow border, loading indicator

#### Account Context Menu
**Right-click** any account for quick actions:

![Account Context Menu](../assets/screenshots/account-context-menu.png)

**Available Actions:**
- **Connect/Disconnect**: Toggle connection state
- **Edit**: Modify account details (stored accounts only)
- **Duplicate**: Create copy with modified settings
- **Delete**: Remove account (stored accounts only)
- **Copy Credentials**: Copy access key to clipboard
- **View in AWS Console**: Open AWS Console for this account

#### Editing Account Details
**Stored accounts** support full editing capabilities:

![Edit Account Dialog](../assets/screenshots/edit-account-dialog.png)

**Editable Fields:**
- Name, description, and tags
- AWS region (triggers table refresh)
- Connection timeout settings
- Auto-connect preferences

**AWS Profiles** show read-only information:

![AWS Profile Details](../assets/screenshots/aws-profile-details.png)

### Bulk Operations

#### Toolbar Actions
Access bulk operations from the accounts view toolbar:

![Accounts Toolbar](../assets/screenshots/accounts-toolbar.png)

**Available Operations:**
- **Reload All**: Refresh AWS profiles from filesystem
- **Disconnect All**: Close all active connections
- **Import Profiles**: Convert AWS profiles to stored accounts
- **Export Settings**: Backup account configurations

#### Multi-Selection
**Select multiple accounts** for batch operations:

![Multi-Select Accounts](../assets/screenshots/multi-select-accounts.png)

**Batch Actions:**
- Connect/disconnect multiple accounts
- Apply tags to multiple accounts
- Delete multiple stored accounts
- Export selected account configurations

### Account Organization

#### Tagging System
Organize accounts with a flexible tagging system:

![Account Tags System](../assets/screenshots/account-tags-system.png)

**Tag Management:**
- **Visual Categories**: Color-coded tags for quick identification
- **Custom Tags**: Create unlimited custom tags
- **Filter by Tags**: Show only accounts with specific tags
- **Bulk Tagging**: Apply tags to multiple accounts

**Common Tag Examples:**
- **Environment**: `production`, `staging`, `development`
- **Region**: `us-east-1`, `eu-west-1`, `ap-south-1`
- **Team**: `backend`, `frontend`, `devops`, `qa`
- **Project**: `mobile-app`, `web-platform`, `analytics`

#### Favorites System
**Star accounts** for quick access:

![Account Favorites](../assets/screenshots/account-favorites.png)

- **Quick Access**: Starred accounts appear at top
- **Recent Connections**: Last 5 connected accounts
- **Keyboard Navigation**: Use ⌘1-9 to connect to favorites

#### Account Grouping
Organize accounts into logical groups:

![Account Grouping](../assets/screenshots/account-grouping.png)

- **By Environment**: Production, Development, Testing
- **By Region**: Group accounts by AWS region
- **By Team**: Organize by team ownership
- **Custom Groups**: Create your own grouping logic

## Account Details & Information

### Account Card Information
Each account displays comprehensive metadata for easy identification:

![Account Card Details](../assets/screenshots/account-card-details.png)

**Standard Information:**
- **Account Name**: Primary identifier
- **Description**: Purpose or environment details
- **AWS Region**: Default region for this account
- **Connection Status**: Visual indicator with last connection time
- **Tags**: Color-coded labels for categorization

**Account Type Indicators:**
- **📄 AWS Profile**: Sourced from `~/.aws/credentials`
- **🔐 Stored Account**: DinoDB-managed with Keychain security
- **⭐ Favorite**: Quick-access starred account

**Metadata Panel:**
Click any account to view detailed information:

![Account Metadata Panel](../assets/screenshots/account-metadata-panel.png)

- **Creation Date**: When account was added to DinoDB
- **Last Connection**: Most recent successful connection
- **Total Tables**: Number of DynamoDB tables
- **IAM Permissions**: Permission validation status
- **Cost Estimation**: Monthly usage estimates (coming soon)

### Connection Health Monitoring
DinoDB continuously monitors account health:

![Account Health Status](../assets/screenshots/account-health-status.png)

**Health Indicators:**
- 🟢 **Healthy**: All systems operational
- 🟡 **Warning**: Minor issues detected
- 🔴 **Critical**: Connection or permission problems
- ⚪ **Unknown**: Not recently tested

## Best Practices Guide

### Security Best Practices

#### IAM User Configuration
**Create dedicated IAM users** for DinoDB with minimal permissions:

```json title="Recommended IAM Policy"
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:ListTables",
                "dynamodb:DescribeTable",
                "dynamodb:Query",
                "dynamodb:Scan",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

#### Access Key Management
**Rotate access keys regularly**:

![Access Key Rotation](../assets/screenshots/access-key-rotation.png)

- **Frequency**: Every 90 days minimum
- **Process**: Create new → Test → Update DinoDB → Delete old
- **Automation**: Set calendar reminders for rotation
- **Backup**: Keep backup keys during transition

#### Environment Separation
**Use separate AWS accounts** for different environments:

| Environment | AWS Account | DinoDB Name | Tags |
|-------------|-------------|-------------|------|
| Development | 111111111111 | "Dev Environment" | `dev`, `testing` |
| Staging | 222222222222 | "Staging/QA" | `staging`, `qa` |
| Production | 333333333333 | "Production" | `prod`, `critical` |

### Organization Best Practices

#### Naming Conventions
**Use consistent, descriptive names**:

✅ **Good Examples:**
- "Production East (us-east-1)"
- "Development Environment"
- "Staging - Mobile Team"
- "Analytics Prod (eu-west-1)"

❌ **Poor Examples:**
- "Account 1"
- "My AWS"
- "Test"
- "AKIA1234567890"

#### Tagging Strategy
**Implement a consistent tagging system**:

![Tagging Strategy](../assets/screenshots/tagging-strategy.png)

**Recommended Tag Categories:**
- **Environment**: `prod`, `staging`, `dev`, `test`
- **Team**: `backend`, `frontend`, `mobile`, `data`
- **Region**: `us-east-1`, `eu-west-1`, `ap-south-1`
- **Criticality**: `critical`, `important`, `development`
- **Cost Center**: `engineering`, `marketing`, `operations`

### Performance Best Practices

#### Connection Management
**Optimize connection usage**:

![Connection Optimization](../assets/screenshots/connection-optimization.png)

- **Concurrent Connections**: Limit to 3-5 active accounts
- **Regional Proximity**: Use accounts in your closest AWS region
- **Connection Pooling**: DinoDB automatically manages connection pools
- **Timeout Settings**: Adjust based on network conditions

#### Cost Optimization
**Monitor and optimize AWS costs**:

- **CloudWatch Costs**: Monitor CloudWatch API usage
- **DynamoDB Costs**: Track read/write capacity consumption
- **Data Transfer**: Minimize cross-region data transfer
- **Reserved Capacity**: Consider reserved capacity for production

## Troubleshooting Guide

### Common Connection Issues

#### "No tables showing" Error
**Symptoms**: Account connects but no tables appear

**Troubleshooting Steps:**
1. **Check IAM Permissions**:
   ```bash
   aws dynamodb list-tables --profile your-profile
   ```

2. **Verify Region Settings**:
   - Ensure account region matches where tables exist
   - Check `~/.aws/config` for region overrides

3. **Test AWS CLI Access**:
   ```bash
   aws dynamodb describe-table --table-name YourTable --profile your-profile
   ```

#### "Connection timeout" Error
**Symptoms**: Account fails to connect with timeout

**Solutions:**
1. **Network Connectivity**:
   ```bash
   ping dynamodb.us-east-1.amazonaws.com
   ```

2. **Firewall/Proxy Settings**:
   - Check corporate firewall rules
   - Configure proxy settings if needed

3. **AWS Service Status**:
   - Visit [AWS Service Health Dashboard](https://status.aws.amazon.com/)

#### "Invalid credentials" Error
**Symptoms**: Authentication failures

**Resolution Steps:**
1. **Regenerate Access Keys** in AWS IAM Console
2. **Update DinoDB** with new credentials
3. **Test credentials** with AWS CLI first
4. **Check for typos** in access key or secret

### Advanced Troubleshooting

#### Debug Mode
Enable debug logging for detailed diagnostics:

![Debug Mode](../assets/screenshots/debug-mode.png)

1. **Settings** → **Advanced** → **Enable Debug Logging**
2. **Reproduce the issue** with debug mode active
3. **Check logs** in Console.app or export debug information
4. **Contact support** with debug logs if needed

#### Connection Diagnostics
DinoDB provides built-in connection testing:

![Connection Diagnostics](../assets/screenshots/connection-diagnostics.png)

**Diagnostic Tests:**
- **DNS Resolution**: Can resolve AWS endpoints
- **Network Connectivity**: Can reach AWS services  
- **Authentication**: Credentials are valid
- **Permissions**: Required IAM permissions present
- **Service Availability**: AWS services are operational

### Getting Additional Help

#### Community Resources
- **GitHub Issues**: [Report bugs and feature requests](https://github.com/vegasq/dinodbapp/issues)
- **Documentation**: Comprehensive guides and tutorials
- **AWS Documentation**: [DynamoDB Developer Guide](https://docs.aws.amazon.com/dynamodb/)

#### Professional Support
- **AWS Support**: For AWS service-related issues
- **Enterprise Support**: Contact for enterprise-specific needs
- **Training**: AWS certification and training resources

---

**Next Steps**: Now that you've mastered account management, explore [Table Operations](table-operations.md) to work with your DynamoDB data.