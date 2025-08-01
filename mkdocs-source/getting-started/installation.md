# Installation

Get DinoDB up and running on your Mac in just a few minutes.

## System Requirements

- **macOS**: 14.0 (Sonoma) or later
- **Architecture**: Intel or Apple Silicon (M1/M2/M3/M4)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 100MB free space
- **Network**: Internet connection for AWS API access

!!! info "Compatibility Check"
    Not sure about your macOS version? Click the Apple menu → About This Mac to check your version.

## Download Options

### Option 1: Direct Download (Recommended)
1. Visit [dinodb.app](https://dinodb.app)
2. Click **"Download for macOS"**
3. Wait for the `DinoDB.dmg` file to download

![Download from website](../assets/screenshots/download-website.png)

4. Open the downloaded DMG file by double-clicking it
5. Drag **DinoDB** to your **Applications** folder

![DMG Installation](../assets/screenshots/dmg-installation.png)

### Option 2: GitHub Releases
1. Go to [GitHub Releases](https://github.com/vegasq/dinodbapp/releases)
2. Download the latest `DinoDB.dmg` file from the Assets section

![GitHub Releases](../assets/screenshots/github-releases.png)

3. Follow the same installation steps as above

## First Launch

### Opening DinoDB
1. Open **Finder** → **Applications**
2. Double-click **DinoDB** to launch

![Applications Folder](../assets/screenshots/applications-folder.png)

### Security Warning (First Time Only)
If you see a security warning on first launch:

![Security Warning](../assets/screenshots/security-warning.png)

**Solution:**
1. Go to **System Settings** → **Privacy & Security**
2. Scroll down to find the DinoDB warning
3. Click **"Open Anyway"** next to the DinoDB entry

![Privacy Security Settings](../assets/screenshots/privacy-security-settings.png)

4. Confirm by clicking **"Open"** in the confirmation dialog

![Security Confirmation](../assets/screenshots/security-confirmation.png)

### Successful Launch
When DinoDB launches successfully, you'll see the welcome screen:

![Welcome Screen](../assets/screenshots/welcome-screen.png)

## AWS Prerequisites

Before using DinoDB, ensure you have AWS access configured.

### AWS Account Requirements
- **Active AWS Account** with DynamoDB service access
- **IAM User or Role** with appropriate permissions
- **Access Keys** or AWS credentials file configured

!!! warning "AWS Account Required"
    DinoDB requires an AWS account to connect to DynamoDB. If you don't have one, [create a free AWS account](https://aws.amazon.com/free/) first.

### Required AWS Permissions

DinoDB needs these IAM permissions to function properly:

```json title="DinoDB IAM Policy"
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:ListTables",
                "dynamodb:DescribeTable",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "dynamodb:CreateTable",
                "dynamodb:DeleteTable",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

!!! tip "Minimal Permissions"
    For read-only access, you can remove `PutItem`, `UpdateItem`, `DeleteItem`, `CreateTable`, and `DeleteTable` permissions.

### AWS Credentials Setup

Choose the method that works best for your workflow:

#### Method 1: AWS Credentials File (Recommended)
This method automatically discovers your AWS profiles.

1. **Create the credentials file** at `~/.aws/credentials`:

```ini title="~/.aws/credentials"
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1

[production]
aws_access_key_id = PROD_ACCESS_KEY
aws_secret_access_key = PROD_SECRET_KEY
region = us-west-2
```

2. **Create the config file** at `~/.aws/config` (optional):

```ini title="~/.aws/config"
[default]
region = us-east-1
output = json

[profile production]
region = us-west-2
output = json
```

![AWS Credentials File](../assets/screenshots/aws-credentials-file.png)

#### Method 2: DinoDB Account Storage
Store credentials securely in DinoDB using macOS Keychain:

1. Launch DinoDB
2. Click **"Add Account"** button

![Add Account Button](../assets/screenshots/add-account-button.png)

3. Fill in the account form:

![Add Account Form](../assets/screenshots/add-account-form.png)

4. Click **"Save"** to store securely in Keychain

!!! info "Security"
    Credentials stored in DinoDB are encrypted and saved in macOS Keychain for maximum security.

## Installation Verification

### Step 1: Launch DinoDB
After installation, launch DinoDB. You should see one of these screens:

**With AWS Credentials File:**
![Accounts from AWS File](../assets/screenshots/accounts-from-aws-file.png)

**Without Credentials (First Time):**
![Welcome Add Account](../assets/screenshots/welcome-add-account.png)

### Step 2: Connect to AWS
1. **Double-click** an account card to connect
2. Watch for the connection status indicator

![Account Connection Status](../assets/screenshots/account-connection-status.png)

### Step 3: Verify Table Access
Once connected, you should see your DynamoDB tables:

![Tables List Connected](../assets/screenshots/tables-list-connected.png)

!!! success "Installation Complete"
    If you can see your DynamoDB tables, installation was successful!

## Troubleshooting

### Common Installation Issues

#### "DinoDB can't be opened" Error
**Cause:** macOS Gatekeeper security protection

**Solution:**
1. Control-click the DinoDB app in Applications
2. Select **"Open"** from the context menu
3. Click **"Open"** in the security dialog

![Right Click Open](../assets/screenshots/right-click-open.png)

#### "No tables showing" after connection
**Possible Causes & Solutions:**

1. **Wrong AWS Region**
   - Check if your tables are in a different region
   - Switch regions in account settings

2. **Insufficient Permissions**
   - Verify IAM policy includes `dynamodb:ListTables`
   - Check AWS CloudTrail for access denied errors

3. **No Tables Exist**
   - Create a test table in AWS Console first
   - Verify you're connected to the correct AWS account

#### Connection timeout or errors
**Troubleshooting Steps:**

1. **Check Internet Connection**
   ```bash
   ping dynamodb.us-east-1.amazonaws.com
   ```

2. **Verify AWS Credentials**
   ```bash
   aws dynamodb list-tables --region us-east-1
   ```

3. **Check AWS Service Status**
   - Visit [AWS Service Health Dashboard](https://status.aws.amazon.com/)

#### "Invalid credentials" error
**Common Solutions:**

1. **Regenerate Access Keys** in AWS IAM Console
2. **Check for typos** in access key or secret key
3. **Verify account hasn't been suspended**

### Getting Help

If you're still having issues:

1. **Check Debug Logs** - Enable debug mode in DinoDB settings
2. **Review AWS CloudTrail** - Check for API call errors
3. **Contact Support** - Include error messages and debug logs

## Next Steps

✅ **Installation Complete!** 

Continue to the [Quick Start Guide](quickstart.md) to learn DinoDB's core features and start managing your DynamoDB tables.

---

### Video Tutorial
🎥 **Watch the complete installation walkthrough** (5 minutes):
[DinoDB Installation Tutorial](https://youtu.be/PLACEHOLDER_VIDEO_ID)